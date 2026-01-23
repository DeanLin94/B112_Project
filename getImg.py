import cv2

class CameraHandler:
    def __init__(self, source=0, width=640, height=480):
        self.cap = cv2.VideoCapture(source)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def get_frame(self):
        if not self.cap.isOpened():
            return False, None
        return self.cap.read()

    def release(self):
        self.cap.release()