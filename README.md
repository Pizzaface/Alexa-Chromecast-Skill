# Alexa-Chromecast-Skill
Allows Alexa to interact with the Google ChromeCast using PHP and PyChromeCast Running on a Computer.

#Explanation

##PHP
  Visiting: yourwebsite.com/playVideo.php?searchString=YOUR_SEARCH_STRING_FOR_YOUTUBE triggers the script to add the video to your database.

##Python
  Using PyChromeCast (https://github.com/balloob/pychromecast), the python script will run at a set interval, continuously checking the database for new videos. When it detects a new row has been added, it loads youtube-dl, a command-line program to grab the stream URL and passes it to PyChromeCast, which sends it to your ChromeCast.
  
#Current Problems
  - PyChromeCast doesn't always detect the ChromeCast, leading the script to fail.

#To Do
  - Pause ChromeCast
  - Kill ChromeCast App
  - Get Duration of Media and allow for playlist.

