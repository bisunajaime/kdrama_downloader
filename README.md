# KDrama M3u8 Video downloader

Packages used:
* `m3u8_To_MP4==0.1.7`

To install requirements.txt type the command below:
* `pip3 install -r requirements.txt`

Instructions
1. go to `kdrama.json`
2. enter a `title` for the file, this will be used for filenames
3. enter .m3u8 url in the `episodes` array and also enter a `filename` for that episode under `fn`,
   1. NOTE: No need to add **.mp4** to the [fn]

Format of the downloaded file will be similar to this example:
``` json
{
    "title": "Squid Game",
    "episodes": [
        {
            "url": "https://mugeong-hwa-ko-chi-pieo-sumida.example/episode1.mp4",
            "fn": "episode1"
        }
    ]
}
```

* title: Squid Game 
* episode[0].fn = episode1

## **FORMAT**:  `squid_game_episode1.mp4`


To run the script
* `python3 kdrama.py`