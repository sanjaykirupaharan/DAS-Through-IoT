Drowsiness detection

  We used MediaPipe face mesh which is a face geometry solution that estimates 468 3D face landmarks in real-time even on mobile devices. It uses machine learning (ML) to derive 3D surface geometry and requires only a camera input without a dedicated depth sensor. By using lightweight model architecture and GPU acceleration throughout the process, the solution can deliver critical real-time performance for the live experience. The face geometry data is composed of common 3D geometric primitives, including face position transformation matrix and triangular face mesh.

  The inbuilt camera will detect the face and start by localizing the facial landmarks by extracting the eye regions to determine if either the eyes are opened or closed. we will be monitoring the eye aspect ratio to see if the defined threshold value raise which is 0.5 in our case but does not increase again for a sufficiently long amount of consecutive frames, thus implying that the driver/user has closed their eyes. Then, the system will raise the alarm and also will inform the responsible person on behalf of the driver to avoid any mistakes. Here we used 3rd party cloud library package called Twilio to send SMS alerts.

  ![DrowsiImage_m](https://user-images.githubusercontent.com/84900433/163725357-54a37569-2764-4e22-9ed1-3efdb0094ef4.png)
