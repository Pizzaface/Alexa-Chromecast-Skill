import pychromecast
import os
import subprocess
import MySQLdb
import re
import sched, time
from subprocess import call
from decimal import *
from gmusicapi import *
from difflib import SequenceMatcher

call("cls", shell=True)
status = ""
chromecast_name = "DEFAULT_CHROMECAST_NAME"




def setup(chromecast_name):
	chromecastList = list(pychromecast.get_chromecasts_as_dict().keys())
	if chromecastList == []:
		print "Shit, we didn't find any Chromecasts..."
		setup(chromecast_name)
	else:
		print "Found ChromeCast: " + str(chromecastList)
	chromecast_name = str(chromecast_name).decode('string_escape')
	
	cast = pychromecast.get_chromecast(friendly_name=chromecast_name)

######  PRE-RUN CODE ######
setup(chromecast_name)

### SETS Database Variable ###

db = MySQLdb.connect(host="MYSQL_HOST", user='MYSQL_USER', passwd="MYSQL_PASS", db='MYSQL_NAME')


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

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
def getKey(item):
    return item[3]
def getTrackNum(item):
    return item[3]

def gpMusicPlaySong(songName, type_of_media):
	try:
		cast.wait()
	except Exception, e:
		print ("There was a problem connecting to the Chromecast.")
		print str(e)
		setup()
		return "error"
	else:
		songs = []
		gmusic = Mobileclient()
		if gmusic.login('', '', Mobileclient.FROM_MAC_ADDRESS) == True:
			searchQuery = songName
			lib = gmusic.get_all_songs()

			if type_of_media == "artist":
				for track in lib:
					if similar(track['artist'],searchQuery) > 0.8:
						songs.append([track['id'], track['title'], track['durationMillis'], similar(track['title'],searchQuery)])

			if type_of_media == "song":
				for track in lib:
					if similar(track['title'],searchQuery) > 0.8:
						songs.append([track['id'], track['title'], track['durationMillis'], similar(track['title'],searchQuery)])

			if type_of_media == "album":
				for track in lib:
					if similar(track['album'],searchQuery) > 0.8:
						songs.append([track['id'], track['title'], track['durationMillis'], track['trackNumber'], similar(track['title'],searchQuery)])

			if not type_of_media == "album":
				songs = list(sorted(songs, key=getKey))
			else:
				songs = list(sorted(songs, key=getTrackNum))

			if songs == []:
				print "We didn't find any songs with that name..."
				return "errorNoSong"

			for x in range(len(songs)):
				streamID = songs[x][0]
				titleOfSong = songs[x][1]
				duration = songs[x][2]
				actual_duration = int(int(duration) / 1000)
				url = gmusic.get_stream_url(streamID)
				print url

				if url == "":
					print "Either Someone else is streaming, or something happened."
				else:
					mc = cast.media_controller
					mc.play_media(url, "audio/mp3")
					print "Song " + titleOfSong + " Sent"
					if not type_of_media == "song":
						time.sleep(actual_duration)
						continue
			else:
				return "success"

		else:
			print "Could not login, did you use an app specific password?."
			return "error"

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
	status = ""
	cur = db.cursor()

	# Use all the SQL you like
	cur.execute("SELECT * FROM commands ORDER BY TIMESTAMP DESC LIMIT 1 ;")

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

	    if row[1] == "connectToChromeCast":
	    	idOfQuert = row[0]
	    	castName = row[2]
	    	print "user wants to switch to Chromecast: " + castName
	    	status = setup(castName)
	    	cur.execute("DELETE FROM commands WHERE id=" + str(idOfQuert))
	    	
	    if row[1] == "gPlayMusic":
	    	idOfQuert = row[0]
	    	songName = row[2]
	    	print "user wants to play song: " + songName
	    	status = gpMusicPlaySong(songName)
	    	if status == "errorNoSong":
	    		cur.execute("DELETE FROM commands WHERE id=" + str(idOfQuert))
	    		print "Song Deleted, since we can't find it."

	   

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



cast = pychromecast.get_chromecast(friendly_name="Jordan's Chromecast")
while True:
    dbConnect()
    time.sleep(2)


