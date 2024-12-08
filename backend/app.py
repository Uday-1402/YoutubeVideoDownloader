from flask import Flask
from flask_cors import CORS
from routes.video import video

app = Flask(__name__)
CORS(app)

app.register_blueprint(video,url_prefix='/api');

if __name__ == "__main__":
    app.run(debug=True)