from flask import Flask, render_template, Response, json
from videoparser import CV2Parser

app = Flask(__name__)
cv2Parser = CV2Parser()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(cv2Parser.gen_video_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
