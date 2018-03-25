Alexa-Chromecast-Skill
======================

**THIS PROJECT HAS BEEN DEPRECIATED, AND I WILL NO LONGER BE WORKING ON IT, AS A NEW VERSION IS IN THE WORKS.**

Allows Alexa to interact with the Google ChromeCast using PHP and PyChromeCast Running on a Computer.

Current Features
----------------

#### Play Youtube Videos (Based on Sample Utterances)

By saying "Alexa, ask ChromeCast play Jontron Home Improvement", Alexa will send the video URL to your Chromecast Python Script.

#### Play Google Play Music (All-Access Not Supported)

By asking Alexa, "Play Never gonna give you up" you can play a song.

By asking Alexa, "Play the artist Two Steps from Hell", you can play an artist.

By asking Alexa, "Play the album 99 luftbullons", you can play an album.

#### Specificing Chromecasts (UNTESTED)

By asking Alexa, "Connect to Living Room", she should set the casting Chromecast to "Living Room"

#### Pause Videos

By saying "Alexa, ask ChromeCast to Pause", Alexa will pause the Chromecast.

#### Resume Videos

By saying "Alexa ask ChromeCast to resume", Alexa will resume playback.

#### Changing the Volume

By saying "Alexa ask ChromeCast to change the volume to 50", Alexa will change the volume to the specified volume

#### Clearing the Queue (Useful for future releases)

By saying "Alexa ask ChromeCast to clear", Alexa will resume playback.

Explanation
-----------

#### PHP

Visiting: yourwebsite.com/playVideo.php?searchString=YOUR_SEARCH_STRING_FOR_YOUTUBE triggers the script to add the video to your database.

#### Python

Using PyChromeCast (https://github.com/balloob/pychromecast), the python script will run at a set interval, continuously checking the database for new videos. When it detects a new row has been added, it loads youtube-dl, a command-line program to grab the stream URL and passes it to PyChromeCast, which sends it to your ChromeCast.

Issues
------

- Sometimes PyChromecast doesn't detect the chromecasts.

To-do
-----

  - Kill ChromeCast App
  - Get Duration of Media and allow for playlist.
  - Allow for interuptions in internet and keep running

Setup
-----

  - Install PyChromecast to your Desired PC (pip install pychromecast)
  - Install build.sql to your MySQL server
  - Get a Youtube API Key (Available [here](https://console.developers.google.com))
  - Replace all connection strings using set-up.py
  - Setup Skill.js In [Lambda](http://aws.amazon.com/)
  - Set up skill in the Alexa Portal at http://developer.amazon.com using sample-utterances.txt and intentSchema.json
  - Run Python Script.
  - Voila!

