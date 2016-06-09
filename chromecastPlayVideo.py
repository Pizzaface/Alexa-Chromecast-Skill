import pychromecast
import os
import subprocess
import MySQLdb
import re
import sched, time
from subprocess import call
from decimal import *
call("cls", shell=True)






def setup():
	chromecastList = list(pychromecast.get_chromecasts_as_dict().keys())
	if chromecastList == []:
		print "Shit, we didn't find any Chromecasts..."
		setup()
	else:
		print "Found ChromeCast: " + str(chromecastList)

	cast = pychromecast.get_chromecast(friendly_name="")

######  PRE-RUN CODE ######
setup()

### SETS Database Variable ###
db = MySQLdb.connect(host="", user='', passwd="", db='')

def volumeSet(Volnum):
	try:
		cast.wait()
	except Exception, e:
		print ("There was a problem connecting to the Chromecast.")
		print str(e)
		setup()
		return "error"
	else:
		mc = cast.media_controller
		getcontext().prec = 3
		actual_volume = Decimal(int(Volnum)) / Decimal(100)
		actual_volume = float(actual_volume)
		cast.set_volume(actual_volume)
		print "Volume set to: " + str(Decimal(int(Volnum)) / Decimal(100))
		return "success"

def sendVideo(url):
	try:
		cast.wait()
	except Exception, e:
		print ("There was a problem connecting to the Chromecast.")
		print str(e)
		setup()
		return "error"
	else:
		mc = cast.media_controller
		p = subprocess.check_output("youtube-dl -g " + url, shell=True)
		mc.play_media(p, 'video/mp4')
		print "Video sent to Chromecast!"
		return "success"

def pauseVideo():
	try:
		cast.wait()
	except Exception, e:
		print ("There was a problem connecting to the Chromecast.")
		print str(e)
		setup()
		return "error"
	else:
		mc = cast.media_controller
		mc.pause()

		print "Video Paused."
		return "success"

def resumeVideo():
	try:
		cast.wait()
	except Exception, e:
		print ("There was a problem connecting to the Chromecast.")
		print str(e)
		setup()
		return "error"
	else:
		mc = cast.media_controller
		mc.play()
		print "Video Resumed."
		return "success"

def dbConnect():
	cur = db.cursor()

	# Use all the SQL you like
	cur.execute("SELECT * FROM commands WHERE run = 0 ORDER BY TIMESTAMP DESC LIMIT 1 ;")

	for row in cur.fetchall():
	    if row[1] == "play":
	    	url = row[2]
	    	print "user wants to watch: " + url
	    	idOfQuert = row[0]
	    	status = sendVideo(url)
	    	

	    if row[1] == "pause":
	    	idOfQuert = row[0]
	    	print "user wants to pause playback"
	    	status = pauseVideo()

	    if row[1] == "resume":
	    	idOfQuert = row[0]
	    	print "user wants to resume playback"
	    	status = resumeVideo()	

	    if row[1] == "volume":
	    	idOfQuert = row[0]
	    	volume = row[2]
	    	print "user wants to set volume to " + str(volume)
	    	status = volumeSet(volume)	

	    if status == "success":
	    	cur.execute("DELETE FROM commands WHERE id=" + str(idOfQuert))
	    	print "Command Completed."

def checkChromeCasts():
	chromecastList = list(pychromecast.get_chromecasts_as_dict().keys())
	if chromecastList == []:
		print "Shit, we didn't find any Chromecasts..."
	for x in range(len(chromecastList)):
		cur = db.cursor()
		escaped = db.escape_string(chromecastList[x])
		cur.execute("SELECT * FROM saved_chromecasts WHERE `friendly_name` = \""+ str(escaped) +"\" LIMIT 1 ;")
		print cur.fetchall()
		for row in cur.fetchall():
			if row[1] == chromecastList[x]:
				exists = True
			else:
				exists = False


			if not exists == True:
				print escaped + " was added."
				cur.execute("INSERT INTO  `saved_chromecasts` (`friendly_name`) VALUES (`"+ str(escaped) + "`);")



cast = pychromecast.get_chromecast(friendly_name="")
while True:
    dbConnect()
    time.sleep(2)


