<h1 align="center">Computer vision and Deep learning-based Driver Assistant System using IoT</h1>

> The whole system was run and tested on Pycharm IDE except 'FirebasePiLocationUpdate.py' which is tested on Raspberry pi.

With the exponential growth of vehicles, there is also a rapid increase in road accidents, about 80% of which are caused by human error. To ensure the safety of the user and the vehicle, it is important to develop a system that continuously guides the driver or automatically drives the vehicle. The vehicle industry and the government are therefore focusing more on accident prevention by introducing better road safety systems for the public. A driver assistance system is an intelligent development of road safety that detects the environment of a moving vehicle, helps the driver to avoid danger and warns the driver of impending danger. With the advancement of current technology, the automotive industry is equipped with IoT-based data transfer mechanisms, under the concept of a “connected car”, passengers and other vehicles connected to the internet can share data with backend applications. Data includes the current location, the distance travelled by the vehicle, whether the vehicle needs emergency services and more. This prototype is mainly focused on developing intelligent driver assistance systems based on computer vision and deep learning, which can prevent accidents by detecting drowsy, harmful objects at an early stage and warning drivers with the traffic signs and road lane lines. The system is capable of passing emergency messages to drivers and other connected vehicles via a website and communicating in the real-time map generated within the system. The proposed system was implemented and tested in multiple detection scenarios, where machine learning improved the accuracy of the results.

![Proposed-Image_Real](https://user-images.githubusercontent.com/84900433/163723748-727ca9a9-8642-4578-a60d-40a5b5ff1471.jpg)

## Table of content

- [Overview](#overview)
- [Results](#results)
- [Usage](#usage)
- [Reference](#reference)

## Overview

![Intro](https://user-images.githubusercontent.com/84900433/163723765-b8d4712a-0ac4-4c6a-b0e0-b2686663ace8.png)

In this research, we proposed the concept of developing a DAS based on the IoT to create a large-scale wireless network by connecting drivers and data that collect and share information about your environment while driving. We propose a new driver distraction method that can detect various behaviours that distract the driver. With the emergence of deep learning methods and computer vision, the use of cameras and real-time processing of captured road scene videos has enabled extensive DAS functions.

An approach based on deep learning and computer vision is used to develop multifunctional DAS systems. It works exactly like the driver's extra eyes and brain. Our system acts as a secure human-machine interface designed to improve road and vehicle safety. The proposed system also includes various detections such as lane detection, pedestrian detection, vehicle detection, road sign detection, traffic light detection, accident detection and weather detection. The detection model is implemented by using different detection algorithms, deep neural network (DNN) architecture and other equivalent models. Our system uses pre-trained and custom-trained models. In addition, the optimized model can be implemented on a suitable hardware platform and become an inexpensive portable vehicle accessory according to the user's needs.

The proposed innovative system is equipped with cameras that would be placed inside and outside the vehicle. The cameras collect the necessary data such as; lane lines, signs, pedestrians, traffic lights, drowsiness and the accident. At the same time, the collected data will be analyzed through various computer vision and deep learning algorithms, and the processed data will be shown to the driver, and in the meantime, various data on our website will be shared via the Internet. The required output is shown to the driver or registered user of our website. 

Mainly five steps followed under this process such as
- Step 1- Detection system
  Lane line detection, object detection, drowsiness detection, road sign detection, accident detection from the video feed. The detected information along with the video captured by the camera is displayed in the user's display
- Step 2- Alert system
  The system will continuously check whether the driver making any wrong decision or not. If the system detects any anomaly then it will guide the driver through both notification and voice alert.
- Step 3- Location detection
  If traffic signs, animals or accidents are detected then the system will detect the current location of the user.
- Step 4– Database Management
  The relevant information such as Traffic sign location, accident location and animal location along with the name is stored in the database.
- Step 5- Interface Management
  When the driver enters his destination, the Google map-based custom-developed map shows all the relevant information through his journeys, such as traffic signs, accidents and animals and notify the driver.

![System Flowchart](https://user-images.githubusercontent.com/84900433/163723778-02ee7311-63cd-4697-b54b-03477fa4a76f.png)


- Drowsiness detection

  We used MediaPipe face mesh which is a face geometry solution that estimates 468 3D face landmarks in real-time even on mobile devices. It uses machine learning (ML) to derive 3D surface geometry and requires only a camera input without a dedicated depth sensor. By using lightweight model architecture and GPU acceleration throughout the process, the solution can deliver critical real-time performance for the live experience. The face geometry data is composed of common 3D geometric primitives, including face position transformation matrix and triangular face mesh.

  The inbuilt camera will detect the face and start by localizing the facial landmarks by extracting the eye regions to determine if either the eyes are opened or closed. we will be monitoring the eye aspect ratio to see if the defined threshold value raise which is 0.5 in our case but does not increase again for a sufficiently long amount of consecutive frames, thus implying that the driver/user has closed their eyes. Then, the system will raise the alarm and also will inform the responsible person on behalf of the driver to avoid any mistakes. Here we used 3rd party cloud library package called Twilio to send SMS alerts.

  ![DrowsiImage_m](https://user-images.githubusercontent.com/84900433/163725357-54a37569-2764-4e22-9ed1-3efdb0094ef4.png)


- Real-time location detection

  ![GPS_Diagram](https://user-images.githubusercontent.com/84900433/163723984-57899d82-c24a-477d-9dc8-efa5f2839581.jpg)

  The real-time location of the vehicles will be detected by using the GPS module which interferes with the raspberry pi. The algorithm will update the detected geo-coordinates of traffic signs, and accidents to the Firebase real-time database. 

  Each vehicle with our system will detect the signs and accidents and update them to our database. And also, the GPS location detection is not 100% every time. The decimal points may vary. Therefore, for the same scenario, there must be more than two coordinates in the database. For the issue, we use a simple machine learning algorithm to get the average coordinates of the same signs or accidents daily once and update the new coordinate to our database. The new coordinates will display with the custom maker in the customized google maps and according to the driver's current location. The traffic signs and the accident information will be displayed to the website authorised user and the voice alerts will be there according to the drivers' direction.

  
- Object Detection

  The most important part of DAS is detecting objects during the driver's journey and warning the driver to avoid collisions. Object detection is a computer vision technique used to locate object instances in images, and videos. It is the core technology behind applications such as surveillance systems, image retrieval systems and driver assistance systems. In our system, we tested the Haar cascade classifier, YOLOv3 and YOLOv5 methods to detect objects. Finally, we chose the YOLOv5 model since it gave a better performance than other models.

  If there are objects such as people, bicycles, cars and trucks, and animals within the visible area of the camera, our system will detect them. Our system involves identifying, classifying and locating any object in an image by extracting the appropriate bounding box enclosing the object, and we can detect several at once. If a collision is imminent, our system will notify the driver.
  
  ![ObjectImage](https://user-images.githubusercontent.com/84900433/163724275-73b81855-e453-4587-a88b-063107253f13.jpg)
  
- Lane Line Detection

  We used Mask-RCNN to recognize lanes from massive manually annotated datasets and using the custom trained model the system detects the lane lines perfectly. The system will detect straight and dot lines on the road and draw the line on the detected lines. If the driver makes a mistake, then the system will warn the driver not to make it. For example, in our country overtaking in a straight line is a traffic rule violation. When the driver tries to overtake on a straight line then the system will warn the driver not to overtake through display notification and voice alert.

  ![rcnn_lane](https://user-images.githubusercontent.com/84900433/163724291-b3bd552b-c271-4624-931b-e43c8a33d638.jpg)

- Traffic Sign Detection

  The traffic signboard detection algorithm will detect the traffic signboard using our trained model and it will update the latitude and longitude of the signboard to the database while indicating the stored value on the created google map. The user will get constant alerts about the upcoming signboard throughout the journey. Created custom traffic sign dataset and the convolutional neural network (CNN) algorithm is used in conjunction with the Google Co-laboratory to train the model.


- Custom Developed Google Maps

  Detected traffic signs along with the latitude and longitude will be stored in the Google Firebase real-time database.  All the traffic sign information is stored in the Google Firebase database and using a machine learning system that is run periodically on a daily basis or weekly basis, all the duplicated values a processed to get the average of the traffic sign location and stored in the processed traffic sign information to the Google Firebase Firestore database. From the Google Firebase Firestore database, all the required traffic sign information is displayed on the custom-developed Google map. 

  ![WebImageNew](https://user-images.githubusercontent.com/84900433/163724695-78c5b9a0-c992-4ad1-b86f-dcefc1aefadd.jpg)


## Results

https://user-images.githubusercontent.com/84900433/163723299-8d3c127b-5dba-4b3a-83a8-8ac69fa138dc.mp4

https://user-images.githubusercontent.com/84900433/163722127-ce9f5669-18b5-4758-8977-d8b9a2d11556.mp4

## Usage

In this repository, we provide real-time location detection, object detection, lane line detection, traffic sign detection and the real-time Google map. You can find the code for the above in the Detections folder. 

1. Do the below changes in [Database](Code/Detections/Database/)
  
    Create your Firebase account in [Firebase Console](https://console.firebase.google.com/)
  
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


   Run [Outside_Camera.py](Code/Outside_Camera.py)

2. Do the below changes in [Drowsiness](Code/Detections/Drowsiness/)/[drowsiness.py](Code/Detections/Drowsiness/drowsiness.py)
      
   Create your [TWILIO](https://www.twilio.com/) account. Add your credentials in 
     
     ```python
      def message():
    # Through Twilio send a message and make a call
    account_sid = "<account_sid>"  # Put your Twilio account SID here
    auth_token = "<auth_token>"  # Put your auth token here

    client = Client(account_sid, auth_token)

    # Send a message
    message = client.api.account.messages.create(
        to="+<receiver>",  # Put your cellphone number here
        from_="+<sender>",  # Put your Twilio number here
        body="Driver is Sleeping....")
    print("[INFO] sending message...")
     ```
   Run [Inside_Camera.py](Code/Inside_Camera.py)


## Reference

1. [Location Detection](https://lastminuteengineers.com/neo6m-gps-arduino-tutorial/)
2. [Custom Training With PixelLib](https://pixellib.readthedocs.io/en/latest/custom_train.html)
3. [Custom Training With YOLO](https://blog.roboflow.com/yolov5-v6-0-is-here/)
4. [Website](https://www.youtube.com/watch?v=ZBLrwThHKyM&list=PL8NTBhIXP2gHG95OHjwWtlIUvEhRRXo9F)

_For more information, refer to the [Deep Learning & Computer Vision for IoT based Intelligent Driver Assistant System](https://ieeexplore.ieee.org/abstract/document/9605823)._

## Contact

- Hirushiharan Thevendran – [LinkedIn](https://www.linkedin.com/in/hirushiharan-thevendran-a08a82152?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B54o2t%2B3cRw6IQKiNxmk27A%3D%3D) – [Email](hirushiharant@gmail.com)
- Ashaya Nagendran – [LinkedIn](https://www.linkedin.com/in/akshaya-nagendran-437557196?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BKC%2FsFC%2FSQWmXOpQ1l7dtSw%3D%3D) – [Email](akshayanagendran52@gmail.com)

<!-- Markdown link & img dfn's -->

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
