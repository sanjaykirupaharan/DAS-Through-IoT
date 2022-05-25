- [FirebasePiLocationUpdate.py](Code/Detections/Database/FirebasePiLocationUpdate.py)
      
     This Python file can only run from Raspberry Pi. 
     Add your generated Firebase SDK JSON file and Firebase database URL to the code. 
     
     ```python
      # Fetch the service account key JSON file contents
  cred = credentials.Certificate('<firebase SDK json file>')

  # Initialize the app with a service account, granting admin privileges
  firebase_admin.initialize_app(cred, {
    'databaseURL': '<firebase database URL>'
  })
     ```
     
     Connect the Raspberry Pi and GPS module by the given [circuit diagram](https://www.hackster.io/bhushanmapari/interfacing-u-blox-neo-6m-gps-module-with-raspberry-pi-3d15a5) and run the file. The current location will be uploaded into the Firebase Real-Time database.
      
- [RetrieveDuplicateSave.py](Code/Detections/Database/RetrieveDuplicateSave.py)
  
     This Python file can run periodically. This will check for duplicated values in the Firebase Real-Time database. If any duplicated values is there, then filter the average value and store it in the Firebase Firestore.
