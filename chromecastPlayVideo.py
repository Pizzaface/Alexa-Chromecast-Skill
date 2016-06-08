import pychromecast
import os
import subprocess
import MySQLdb
import re
import sched, time

chromecastList = list(pychromecast.get_chromecasts_as_dict().keys())
if chromecastList == []:
	print "Shit, we didn't find any Chromecasts..."
else:
	print "Found ChromeCast: " + str(chromecastList)

cast = pychromecast.get_chromecast(friendly_name="CHROMECAST_FRIENDLY_NAME")

def sendVideo(url):
	try:
		cast.wait()
	except:
		print ("There was a problem connecting to the Chromecast.")
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
	except:
		print ("There was a problem connecting to the Chromecast.")
		return "error"
	else:
		mc = cast.media_controller
		time.sleep(2)
		mc.pause()

		print "Video Paused."
		return "success"

def resumeVideo():
	try:
		cast.wait()
	except:
		print ("There was a problem connecting to the Chromecast.")
		return "error"
	else:
		mc = cast.media_controller
		time.sleep(2)
		mc.play()
		print "Video Resumed."
		return "success"


def dbConnect():
	db = MySQLdb.connect(host="MYSQL_HOST", user='MYSQL_USER', passwd="MYSQL_PASSWORD", db='MYSQL_DB')
	cur = db.cursor()

	# Use all the SQL you like
	try:
		cur.execute("SELECT * FROM commands WHERE run = 0 ORDER BY TIMESTAMP DESC LIMIT 1 ;")
	except:
		print "Nothing to Cast."
	else:
		# print all the first cell of all the rows
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

		    if status == "success":
		    	cur.execute("DELETE FROM commands WHERE id=" + str(idOfQuert))
		    	print "Command Completed."
		db.close()

## FOR FUTURE DEVELOPMENTS ##
def checkChromeCasts():
	chromecastList = list(pychromecast.get_chromecasts_as_dict().keys())
	if chromecastList == []:
		print "Shit, we didn't find any Chromecasts..."
	for x in range(len(chromecastList)):
		db = MySQLdb.connect(host="MYSQL_HOST", user='MYSQL_USER', passwd="MYSQL_PASSWORD", db='MYSQL_DB')
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
				print "INSERT INTO  `saved_chromecasts` (`friendly_name`) VALUES (`"+ str(escaped) + "`);"
				cur.execute("INSERT INTO  `saved_chromecasts` (`friendly_name`) VALUES (`"+ str(escaped) + "`);")

while True:
    dbConnect()


