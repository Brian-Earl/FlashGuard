# FlashGuard

## Directories and files included in this project:
```bash
FlashGuard
|-- LICENSE
|-- README.md
|-- browser
|   |-- browser.py
|   `-- client.py
|-- config.json
|-- main.py
 -- server
    |-- extension_handler.py
    |-- video_process.py
    `-- wait_for_page_change.py
```



## Installation
*  Install dependencies<br>`pip3 install opencv-python youtube_dl numpy selenium`
*  [Download chromedriver](http://chromedriver.chromium.org/downloads) and configure `chromedriver` path in config.json
*  Configure hostname of server in config.json
*  Start server:<br>`python3 server/extension_handler.py`
*  Start client:<br> `python3 main.py`

## Pop-Ups
After a video is processed, it wil respond with a reccomendation to whether the video could be potentially harmful  
or not. Videos that are processed as harmful will be paused and produce give pop-ups that look like this:  
![alt text](https://i.imgur.com/9HrRmjG.png)  
  
This project currently only supports videos that are 30fps. If a video doesn't get processed because of this, it will be paused and given this alert as a warning:  
![alt text](https://i.imgur.com/IEBbF7O.png)  
