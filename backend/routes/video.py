# Download a single youtube video.
import os
from flask import Blueprint, request, jsonify, send_file
from controllers.videoController import downloadSingleVideo

video = Blueprint("video", __name__)


@video.route("/video", methods=["POST"])
def downloadVideo():
    print("Route Hit..")
    videoUrl = request.json
    # print(videoUrl['url'])
    data = downloadSingleVideo(videoUrl["url"])
    print(data)
    return jsonify({"data": data, "status": 200})


@video.route("/download", methods=["POST"])
def sendVideo():
    try:
        req_body = request.json
        filename = req_body["filename"]
        return send_file(
            os.path.join(os.getcwd(), "downloads", filename), as_attachment=True
        )
    except FileNotFoundError:
        return "File Not Found", 404
