# easy-rppg

<p align="center">
    <a href="STATUS" alt="status">
        <img src="https://img.shields.io/badge/status-inprocess-lightgray" /></a>    
    <a href="LICENSE" alt="License">
        <img src="https://img.shields.io/badge/license-GPL3-blue" /></a>
    <a href="PLATFORM" alt="Platform">
        <img src="https://img.shields.io/badge/platform-linux--64-lightgrey" /></a>  
    <a href="CONTRIBUTORS" alt="Contributors">
        <img src="https://img.shields.io/badge/contributors-3-brightgreen" /></a>                
</p>

Camera-based Cardiac Signal Measurement: A non-invasive application for monitoring heart activity using a video/camera and image processing techniques.


<img src="media/logo.jpg" alt="easy-rppg Logo" width="384" height="576">


## Authors

- [Deivid Johan Botina Monsalve](https://linktr.ee/deividbotina?utm_source=linktree_admin_share)
- [Henry Jhoán Areiza Laverde](https://github.com/HenryAreiza)
- [Camilo Alejandro Bermúdez Mejía](https://github.com/camiloabermudez)


***easy-rppg is for research purposes only, and commercial use is not allowed.***

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [RPPG from video file](#rppg-from-video-file)
  - [RPPG from folder with enumerated images](#rppg-from-folder-with-enumerated-images)
  - [RPPG from camera (real-time)](#rppg-from-camera-(real-time))
- [License](#license)


## Getting Started

Follow these instructions to get the easy-rppg application up and running on your local machine.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python 3.10.4](https://www.python.org/downloads/release/python-3104/) or higher installed.
- [virtualenv](https://virtualenv.pypa.io/en/latest/) installed (for creating a virtual environment).

### Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/deividbotina-alv/easy-rppg.git
```

2. Navigate to the project directory:
```bash
cd easy-rppg
```

3. Create a virtual environment (recommended):
```bash
virtualenv venv
```

4. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- macOS and Linux:
```bash
source venv/bin/activate
```

5. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

You can run easy-rppg by executing the main.py script in the src directory. The script accepts the following command-line arguments to configure the RPPG measurement.

|    Input        | Tag         | Type         | Description  | Default |Required|
| :-------------- |:-------------|:-------------|:-------------|:--------|:-------|
| `--method` | `-m`    |    str       |RPPG measurement method (Green, GR) | Green | True   |
| `--face_detector`|  `-fd`    |    str       |Face detection method (mediapipe or haarcascade) | mediapipe | True   |
| `--path`  | `-p`   |    str     | Path to the file (video or first enumerated image) | None | False   |
| `--RT`| `-r`|    flag    | Real-time processing mode| False | False   |
| `--SHOW`| `-s`|    flag    |Stream face detection| False | False   |

### RPPG from video file

To acquire the RPPG signal from a video, just follow the example below

```bash
python src/main.py --method Green --face_detector mediapipe --path /path/to/video.avi
```

### RPPG from folder with enumerated images

- [ ] In process...

### RPPG from camera (real-time)

- [ ] In process...

## References

RPPG measurement methods:

|    Method        | Article | Authors | Repository |
| :-------------- |:-------------|:-------------|:-------------|
| `Green` | [Remote plethysmo-graphic imaging using ambient light (2008)](https://opg.optica.org/oe/fulltext.cfm?uri=oe-16-26-21434&id=175396) | Verkruysse, W., Svaasand, L. O., & Nelson, J. S.|  NA| 
| `G-R` | [Remote plethysmo-graphic imaging using ambient light](https://opg.optica.org/oe/fulltext.cfm?uri=oe-16-26-21434&id=175396) | Verkruysse, W., Svaasand, L. O., & Nelson, J. S.| NA|

## License

This project is licensed under the GNU General Public License 3.0 - see the LICENSE file for details.
