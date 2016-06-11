youtube_api_key = raw_input("What is your Youtube API key? ")
app_specific_pass = raw_input("What is your Google App Specific Password? ")
default_chromecast = raw_input("Name of the default ChromeCast? ")
db_host = raw_input("What is your Database Host? ")
db_user = raw_input("What is your Database Username? ")
db_pass = raw_input("What is your Database Password? ")
db_name = raw_input("What is your Database Name? ")
host_name = raw_input("What is your Host Name? (Ex: yourhost.com) ")


### Checks PyChomecast ###
try:
	import pychromecast
except ImportError:
	print ("You don't have PyChromecast Installed!")
else:
    print "You have PyChromecast Installed."

try:
	import MySQLdb
except ImportError:
	print ("You don't have MySQLdb Installed!")
else:
    print ("You have MySQLdb Installed")

try:
    import gmusicapi
except ImportError:
    print ("You don't have gmusicapi Installed!")
else:
    print ("You have gmusicapi Installed")
    

def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print '"{old_string}" not found in {filename}.'.format(**locals())
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

    print "Variables Changed!"

inplace_change("playVideo.php", "MYSQL_HOST", db_host)
inplace_change("playVideo.php", "MYSQL_USER", db_user)
inplace_change("playVideo.php", "MYSQL_PASS", db_pass)
inplace_change("playVideo.php", "MYSQL_NAME", db_name)

inplace_change("chromecastPlayVideo.py", "MYSQL_HOST", db_host)
inplace_change("chromecastPlayVideo.py", "MYSQL_USER", db_user)
inplace_change("chromecastPlayVideo.py", "MYSQL_PASS", db_pass)
inplace_change("chromecastPlayVideo.py", "MYSQL_NAME", db_name)
inplace_change("chromecastPlayVideo.py", "DEFAULT_CHROMECAST_NAME", default_chromecast)

inplace_change("skill.js", "YOUR_HOST_HERE", host_name)



