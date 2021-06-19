import cv2
from time import sleep


class CV2Parser:
    cap = cv2.VideoCapture('video.mp4')

    def __init__(self):
        pass

    def parse_by_open_cv(self, element_to_parse):
        if not self.cap:
            self.cap = cv2.VideoCapture('video.mp4')
        if element_to_parse == 'web_cam':
            self.stop_parsing()
            self.cap = cv2.VideoCapture(0)

        while True:
            sleep(.8)
            success, frame = self.cap.read()  # read the camera frame
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        self.stop_parsing()

    def gen_video_frames(self):
        return self.parse_by_open_cv('video.mp4')

    def stop_parsing(self):
        # When everything done, release the video capture object
        self.cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()
