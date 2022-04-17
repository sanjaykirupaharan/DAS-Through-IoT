<h1 align="center">Computer vision and Deep learning-based Driver Assistant System using IoT</h1>

> The whole system was run and tested on Pycharm IDE except 'FirebasePiLocationUpdate.py' which is tested on Raspberry pi.

With the exponential growth of vehicles, there is also a rapid increase in road accidents, about 80% of which are caused by human error. To ensure the safety of the user and the vehicle, it is important to develop a system that continuously guides the driver or automatically drives the vehicle. The vehicle industry and the government are therefore focusing more on accident prevention by introducing better road safety systems for the public. A driver assistance system is an intelligent development of road safety that detects the environment of a moving vehicle, helps the driver to avoid danger and warns the driver of impending danger. With the advancement of current technology, the automotive industry is equipped with IoT-based data transfer mechanisms, under the concept of a “connected car”, passengers and other vehicles connected to the internet can share data with backend applications. Data includes the current location, the distance travelled by the vehicle, whether the vehicle needs emergency services and more. This prototype is mainly focused on developing intelligent driver assistance systems based on computer vision and deep learning, which can prevent accidents by detecting drowsy, harmful objects at an early stage and warning drivers with the traffic signs and road lane lines. The system is capable of passing emergency messages to drivers and other connected vehicles via a website and communicating in the real-time map generated within the system. The proposed system was implemented and tested in multiple detection scenarios, where machine learning improved the accuracy of the results.

![Proposed-Image_Real](https://user-images.githubusercontent.com/84900433/163723748-727ca9a9-8642-4578-a60d-40a5b5ff1471.jpg)

## Table of content

- [Overview](#overview)
- [Results](#results)
- [Usage](#usage)
- [License](#license)
- [Links](#links)

## Overview

With the rapid development of science and technology, every year we are losing so many human lives due to automobile accidents and disabling a much more. Those losses are costing nations, losing human capital and cause for individual families are insurmountable- non-calculable. According to statistics from the world health organization (WHO), approximately 1.3 million people will die each year in traffic accidents by 2021. 93% of deaths on the world's roads occur in low- and middle-income countries, even though these countries own about 60% of the world's vehicles. Therefore, the automobile industry and governments are paying more attention to accident prevention by introducing improved road safety systems for the public. Due to technological advances in the embedded systems, artificial intelligence (AI) and computer vision industries, and the internet of things (IoT), we can save millions of lives. Therefore, new trends such as driver assistance systems (DAS) and autonomous driving have been explored over the past decade.

Self-driving cars recognize the unavoidable accidents that can happen, regardless of the quality of the electronic components or systems, there is no guarantee that failures will not occur. Compared to DAS, self-driving cars have less impact on the prevention of traffic accidents, because they cannot operate like humans and make accurate decisions. The sole motivation behind the development of DAS is that it helps drivers drive more safely by working before something happens. Therefore, with the development of telecommunication services, embedded systems and computer vision technology, DAS is an essential part of smart transport. Recently, the development of DAS has shown positive results in the integration of traffic sources, real-time vehicle status and monitoring of the driving environment.

DAS generally consists of two parts: active safety and passive safety. Passive safety relies on certain devices, such as seat belts, airbags and bumpers, to protect passengers and reduce injuries. Passive safety alone cannot improve driving safety. 93% of road accidents are due to a lack of awareness among drivers while driving. In addition, it is reported that if the driver is warned just 1.5 seconds before the incident, 90% of dangerous accidents can be avoided. In the automotive industry, a small mistake can cause personal injury or death, so extreme safety precautions must be taken.

Recently, the IoT has continued to evolve, with the concept of connecting everything to everyone via the internet. The integration of machine learning and the IoT has great potential to improve the performance of different systems. According to the research available in the current literature, distraction is considered the leading cause of traffic accidents and can be avoided by deploying IoT-based DAS.

As mentioned above, future technological developments can solve all the inconveniences caused and able to improve the efficiency of the system. In addition, major high-end car brands such as BMW, Volvo and Tesla have delivered more advanced driver assistance features and achieved significant success. The problem is that these brands are unaffordable for drivers in underdeveloped countries or the developing world. That is why we provide creative and innovative technical support to the mass market for car owners in less developed countries. This is a hybrid mode intelligent DAS with reliable and stable operation. The hybrid model of autonomous systems and human decision-making processes has surpassed the operation of a single autonomous system or human vehicle. The proposed system is fully aimed at improving safety by preventing accidents while also warning the driver. Most accidents that we believe, can be avoided provide technical support which could be affordable for a mass market of vehicle owners.

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


## Results

https://user-images.githubusercontent.com/84900433/163723299-8d3c127b-5dba-4b3a-83a8-8ac69fa138dc.mp4

https://user-images.githubusercontent.com/84900433/163722127-ce9f5669-18b5-4758-8977-d8b9a2d11556.mp4

## Usage

In this repository, we provide codes for real-time location detection, object detection, lane line detecion, traffic sign detection and the 

- 0.2.1
- 0.2.0


_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

- 0.2.1
  - CHANGE: Update docs (module code remains unchanged)
- 0.2.0
  - CHANGE: Remove `setDefaultXYZ()`
  - ADD: Add `init()`
- 0.1.1
  - FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
- 0.1.0
  - The first proper release
  - CHANGE: Rename `foo()` to `bar()`
- 0.0.1
  - Work in progress

## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See `LICENSE` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
