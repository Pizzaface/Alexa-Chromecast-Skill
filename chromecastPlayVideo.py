import pychromecast
import os
import subprocess
import MySQLdb
import sched, time

def sendVideo(url):
	print list(pychromecast.get_chromecasts_as_dict().keys())
	p = subprocess.check_output("youtube-dl -g " + url, shell=True)

	cast = pychromecast.get_chromecast(friendly_name="")
	try:
		cast.wait()
	except:
		print ("There was a problem connecting to the Chromecast.")
		return "error"
	else:
		if not cast.is_idle:
		    print("Killing current running app")
		    cast.quit_app()
		    time.sleep(5)
		mc = cast.media_controller
		mc.play_media(p, 'video/mp4')
		cast.disconnect()
		return "success"


def dbConnect():
	db = MySQLdb.connect(host="", user='', passwd="", db='')
	cur = db.cursor()

	# Use all the SQL you like
	try:
		cur.execute("SELECT * FROM commands ORDER BY TIMESTAMP DESC LIMIT 1 ;")
	except:
		print "Nothing to Cast."
	else:
		# print all the first cell of all the rows
		for row in cur.fetchall():
		    if row[1] == "play":
		    	url = row[2]
		    	idOfQuert = row[0]
		    	status = sendVideo(url)
		    	print status
		    	if status == "success":
		    		cur.execute("DELETE FROM commands WHERE id=" + str(idOfQuert))

		    if row[1] == "pause":
		    	pauseVideo()
		db.close()

while True:
    dbConnect()


