# Alexa-Chromecast-Skill
Allows Alexa to interact with the Google ChromeCast using PHP and PyChromeCast Running on a Computer.

#Current Features:
###Play Youtube Videos (Based on Sample Utterances)
By saying "Alexa, ask ChromeCast play Jontron Home Improvement", Alexa will send the video URL to your Chromecast Python Script.

###Pause Videos
By saying "Alexa, ask ChromeCast to Pause", Alexa will pause the Chromecast.

###Resume Videos
By saying "Alexa ask ChromeCast to resume", Alexa will resume playback.

###Clearing the Queue (Useful for future releases)
By saying "Alexa ask ChromeCast to clear", Alexa will resume playback.

#Explanation

##PHP
  Visiting: yourwebsite.com/playVideo.php?searchString=YOUR_SEARCH_STRING_FOR_YOUTUBE triggers the script to add the video to your database.

##Python
  Using PyChromeCast (https://github.com/balloob/pychromecast), the python script will run at a set interval, continuously checking the database for new videos. When it detects a new row has been added, it loads youtube-dl, a command-line program to grab the stream URL and passes it to PyChromeCast, which sends it to your ChromeCast.
  
#To Do
  - Kill ChromeCast App
  - Get Duration of Media and allow for playlist.

#Setup
  - Install PyChromecast to your Desired PC (pip install pychromecast)
  - Install build.sql to your MySQL server
  - Get a Youtube API Key (Available [here](https://console.developers.google.com))
  - Replace all connection strings
  - Setup Skill.js In [Lambda](http://aws.amazon.com/)
  - Set up skill in the Alexa Portal at http://developer.amazon.com using sample-utterances.txt and intentSchema.json
  - Run Python Script.
  - Voila!

