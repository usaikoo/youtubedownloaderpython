# Youtube Downloader with Python

## In Docker

```
docker run --rm -d -v {your-download-folder-path}:/app/Videos pyaephyohein/ --network=host pyaephyohein/youtubedownloadpython:latest
```

## Run
http://{your-ip-address}:5000

After download, check your videos in {your-download-folder-path}

## In local machine

```
python3 -m pip install -r  requirements.txt
```
```
python3 main.py
```

## Run

http://{your-ip-address}:5000


After download, check your videos in Videos folder of Webapp.



