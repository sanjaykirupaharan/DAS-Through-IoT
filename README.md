<h1 align="center">Computer vision and Deep learning-based Driver Assistant System using IoT</h1>

# Computer vision and Deep learning-based Driver Assistant System using IoT
> The whole system was run and tested on Pycharm IDE except 'FirebasePiLocationUpdate.py' which is tested on Raspberry pi.

With the exponential growth of vehicles, there is also a rapid increase in road accidents, about 80% of which are caused by human error. To ensure the safety of the user and the vehicle, it is important to develop a system that continuously guides the driver or automatically drives the vehicle. The vehicle industry and the government are therefore focusing more on accident prevention by introducing better road safety systems for the public. A driver assistance system is an intelligent development of road safety that detects the environment of a moving vehicle, helps the driver to avoid danger and warns the driver of impending danger. With the advancement of current technology, the automotive industry is equipped with IoT-based data transfer mechanisms, under the concept of a “connected car”, passengers and other vehicles connected to the internet can share data with backend applications. Data includes the current location, the distance travelled by the vehicle, whether the vehicle needs emergency services and more. This prototype is mainly focused on developing intelligent driver assistance systems based on computer vision and deep learning, which can prevent accidents by detecting drowsy, harmful objects at an early stage and warning drivers with the traffic signs and road lane lines. The system is capable of passing emergency messages to drivers and other connected vehicles via a website and communicating in the real-time map generated within the system. The proposed system was implemented and tested in multiple detection scenarios, where machine learning improved the accuracy of the results.

## Table of content

- [Installation](#installation)
    - [TER](#typo3-extension-repository)
    - [Composer](#composer)
- [TYPO3 setup](#typo3-setup)
    - [Extension](#extension)
    - [Database](#database)
- [Page setup](#page-setup)
    - [Upload the page tree file](#upload-the-page-tree-file)
    - [Go to the import view](#go-to-the-import-view)
    - [Import the page tree](#import-the-page-tree)
    - [SEO-friendly URLs](#seo-friendly-urls)
- [License](#license)
- [Links](#links)

![Install Aimeos TYPO3 extension](https://aimeos.org/docs/images/Aimeos-typo3-extmngr-install.png)


Show instructions

1. Install the preset:

    ```sh
    $ npm install --save-dev size-limit @size-limit/file
    ```

2. Add the `size-limit` section and the `size` script to your `package.json`:

    ```diff
    + "size-limit": [
    +   {
    +     "path": "dist/app-*.js"
    +   }
    + ],
      "scripts": {
        "build": "webpack ./webpack.config.js",
    +   "size": "npm run build && size-limit",
        "test": "jest && eslint ."
      }
    ```



One to a two-paragraph statement about your product and what it does.

![](header.png)

## Installation

OS X & Linux:

```sh
npm install my-crazy-module --save
```

Windows:

```sh
edit autoexec.bat
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
* 0.0.1
    * Work in progress

## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

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
