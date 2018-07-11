#!python3.5

# Prerequisites :
# 1.SetUp dropbox sdk to be able to use Dropbox Api's
# $ sudo pip install dropbox
# By default python dropbox sdk is based upon the python 3.5
#
# 2. Create an App on dropbox console (https://www.dropbox.com/developers/apps) which will be used and validated to do
# the file upload and restore using dropbox api. Mostly you need an access token to connect to Dropbox before actual file/folder operations.
#
# 3. Once done with code, run the script by following command
# $ python SFileUploader.py // if python3.5 is default


import sys
import dropbox
import time
import os
import urllib
import pathlib

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# Access token
TOKEN = 'Add Dropbox Access Token Here'

LOCALFILE = os.path.dirname(__file__ ) + '/Gemini/Gemini - 20180709-150502.jpg'
print(LOCALFILE)
BACKUPPATH = '/Master Scraper/Gemini ' +  str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg" # Keep the forward slash before destination filename

#Create Directory Structure if doesn't exist in working Directory.
dirpath = os.path.dirname(__file__ )+ "/Plates34_37"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
dirpath = os.path.dirname(__file__ )+ "/Plates22_25"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
dirpath = os.path.dirname(__file__ )+ "/KWcam"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
dirpath = os.path.dirname(__file__ )+ "/KEcam"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
dirpath = os.path.dirname(__file__ )+ "/KIcam"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
dirpath = os.path.dirname(__file__ )+ "/F1cam"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
dirpath = os.path.dirname(__file__ )+ "/PGcam"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
dirpath = os.path.dirname(__file__ )+ "/Hwy130camSouth"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
dirpath = os.path.dirname(__file__ )+ "/Hwy130camNorth"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
dirpath = os.path.dirname(__file__ )+ "/MaunaKea"
pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

starttime=time.time()
minuteCount5 = 4
minuteCount12 = 11

# Uploads contents of LOCALFILE to Dropbox
def backup():
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()

# Run this script independently
if __name__ == '__main__':
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            "ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

    print("Entering Loop for web scraper")
    # Begin loop to grab images from linked webcameras. 
    while True:
        try:

            minuteCount5+=1
            minuteCount12+=1

            #Thermal Plates - 1 minute delay
            currentName1 = "Plates34_37/Plate34-37" + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg" #Generates file name
            urllib.request.urlretrieve("http://images.punatraffic.com/SnapShot/320x240/TL-11.jpg", currentName1) #gets the image and stores in approriate directory
            LOCALFILE = os.path.dirname(__file__) + '/' + currentName1 #stores file location and name 
            BACKUPPATH = '/Master Scraper/Plates34_37/Plate34-37 ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg" #generates backup path for Dropbox upload
            backup() 
            print('Backup Completed.')

            currentName2 = "Plates22_25/Plate22-25" + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
            urllib.request.urlretrieve("http://images.punatraffic.com/SnapShot/320x240/TL-10.jpg", currentName2)
            print("Thermal: "+currentName1 + " - " + currentName2)
            LOCALFILE = os.path.dirname(__file__) + '/' + currentName2
            BACKUPPATH = '/Master Scraper/Plates22_25/Plate22-25 ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
            backup()
            print('Backup Completed.')

            if(minuteCount5==5):
                #KWcam - 5 minute delays
                currentName = "KWcam/KWcam - " + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                urllib.request.urlretrieve("https://volcanoes.usgs.gov/observatories/hvo/cams/KWcam/images/M.jpg", currentName)
                print(currentName)
                LOCALFILE = os.path.dirname(__file__) + '/' + currentName
                BACKUPPATH = '/Master Scraper/KWcam/KWcam ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                backup()
                print('Backup Completed.')

                # KIcam- 5 minute delays
                currentName = "KIcam/KIcam - " + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                urllib.request.urlretrieve("https://volcanoes.usgs.gov/observatories/hvo/cams/KIcam/images/M.jpg", currentName)
                print(currentName)
                LOCALFILE = os.path.dirname(__file__) + '/' + currentName
                BACKUPPATH = '/Master Scraper/KIcam/KIcam ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                backup()
                print('Backup Completed.')

                #PGcam- 5 minute delays
                currentName = "PGCam/PGcam - " + str(time.strftime("%Y%m%d-%H%M%S")) +".jpg"
                urllib.request.urlretrieve("https://volcanoes.usgs.gov/observatories/hvo/cams/PGcam/images/M.jpg", currentName)
                print(currentName)
                LOCALFILE = os.path.dirname(__file__) + '/' + currentName
                BACKUPPATH = '/Master Scraper/PGCam/PGcam ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                backup()
                print('Backup Completed.')

                minuteCount5=0

            if(minuteCount12==12):
                #DOT hwy130 cams
                currentName = "Hwy130camSouth/Hwy130 South - " + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                urllib.request.urlretrieve("http://images.punatraffic.com/SnapShot/320x240/TL-206.jpg", currentName)
                print(currentName)
                LOCALFILE = os.path.dirname(__file__) + '/' + currentName
                BACKUPPATH = '/Master Scraper/Hwy130camSouth/Hwy130 South ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                backup()
                print('Backup Completed.')

                # DOT hwy130 cams
                currentName = "Hwy130camNorth/Hwy130 North - " + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                urllib.request.urlretrieve("http://images.punatraffic.com/SnapShot/320x240/TL-207.jpg", currentName)
                print(currentName)
                LOCALFILE = os.path.dirname(__file__) + '/' + currentName
                BACKUPPATH = '/Master Scraper/Hwy130camNorth/Hwy130 North ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                backup()
                print('Backup Completed.')

                # F1cam- 12 minute delays
                currentName = "F1cam/F1cam - " + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                urllib.request.urlretrieve("https://volcanoes.usgs.gov/observatories/hvo/cams/F1cam/images/M.jpg", currentName)
                print(currentName)
                LOCALFILE = os.path.dirname(__file__) + '/' + currentName
                BACKUPPATH = '/Master Scraper/F1cam/F1cam ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                backup()
                print('Backup Completed.')

                # KEcam- 12 minute delays
                currentName = "KEcam/KEcam - " + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                urllib.request.urlretrieve("https://volcanoes.usgs.gov/observatories/hvo/cams/KEcam/images/M.jpg", currentName)
                print(currentName)
                LOCALFILE = os.path.dirname(__file__) + '/' + currentName
                BACKUPPATH = '/Master Scraper/KEcam/KEcam ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                backup()
                print('Backup Completed.')

                minuteCount12=0

            #Gemini images - only operates at night.
            TimeString = str(time.strftime('%Y%m%d-%H%M%S'))
            TimeString = TimeString[9] + TimeString[10] + TimeString[11] + TimeString[12]
            if  int(TimeString) < 800:
                currentName = "MaunaKea/Gemini - " + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                urllib.request.urlretrieve("http://www.cfht.hawaii.edu/en/gallery/cloudcams/cloudcam1/movies/Jul09-2018-CFHT-CC1-large.mp4.keyframe.jpg", currentName)
                print(currentName)
                LOCALFILE = os.path.dirname(__file__) + '/' + currentName
                BACKUPPATH = '/Master Scraper/MaunaKea/Gemini ' + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
                backup()
                print('Backup Completed.')

            time.sleep(60.0 - ((time.time() - starttime) % 60.0)) #loop every minute delay

        except:
            print("Error detected")


