# To download single video..
import os
from urllib.parse import urlparse, parse_qs
from flask import jsonify
from yt_dlp import YoutubeDL


def downloadSingleVideo(videoUrl):
    # print("Downloading the video...",videoUrl)

    print(videoUrl)
    try:
        parsed_url = urlparse(videoUrl)
        query_param = parse_qs(parsed_url.query)
        video_id = query_param.get("v", [""])[0]
        ydl_opts = {
            "format": "best",  # Best quality video
            "outtmpl": f"./downloads/{video_id}.%(ext)s",  # Save with video title as filename at ./downloads folder
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(videoUrl, download=False)
            video_ext = info_dict.get("ext")
            video_filename = f"{video_id}.{video_ext}"

            if os.path.isfile(os.path.join(os.getcwd(), "downloads", video_filename)):
                return {"downloadUrl": f"{video_filename}"}

            ydl.download([videoUrl])
        # print(video_filename)
        downloadUrl = f"{video_filename}"
        return {"downloadUrl": downloadUrl}
    except Exception as e:
        print(e)
        return {"Error": "Error Downloading file."}
