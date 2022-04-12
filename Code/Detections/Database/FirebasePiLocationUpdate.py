#Get the real time location
#https://www.hackster.io/bhushanmapari/interfacing-u-blox-neo-6m-gps-module-with-raspberry-pi-3d15a5

import serial
import pynmea2

import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import firestore

from datetime import datetime

# https://morioh.com/p/a593f973aff0

# Fetch the service account key JSON file contents
cred = credentials.Certificate('<firebase SDK json file>')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': '<firebase database URL>'
})


def location(sign):
    while True:
        port = "/dev/ttyAMA0"
        ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata = ser.readline()

        # current date and time
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        date = date_time.split('/')
        # reference_name = '/{}_{}_{}'.format(date[0], date[1], date[2].split(',')[0])
        doc_name = '{}_{}_{}-{}'.format(date[0], date[1], date[2].split(',')[0], date[2].split(',')[1].strip())

        if newdata[0:6] == "$GPRMC":
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = "[INFO] Latitude=" + str(lat) + "and Longitude=" + str(lng)
            if lat != 0.0 or lng != 0.0:
                print(gps)

                firebase_admin.get_app(name='[DEFAULT]')
                ############# Save data #############
                ref = db.reference('/real-time_coordinates').update({
                    doc_name: {
                        'name': sign,
                        'lat': str(lat),
                        'lng': str(lng),
                    },
                })
            else:
                print("Zero")
