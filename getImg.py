import cv2
import threading
import time

class CameraHandler:
    def __init__(self, source=0, width=640, height=480):
        self.cap = cv2.VideoCapture(source)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        
        
        self.ret, self.frame = self.cap.read()
        self.stopped = False
        
        
        self.start_time = time.time()
        self.fps = 0

        
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True  
        self.thread.start()

    def update(self):
        while not self.stopped:
            ret, frame = self.cap.read()
            if ret:
                self.ret = ret
                self.frame = frame
            else:
                self.stopped = True

    def get_data(self):

        # 計算 FPS 的邏輯
        current_time = time.time()
        cycle_time = current_time - self.start_time
        self.fps = 1 / cycle_time if cycle_time > 0 else 0
        self.start_time = current_time
        
        return self.ret, self.frame, self.fps

    def release(self):
        self.stopped = True
        if self.thread.is_alive():
            self.thread.join() 
        self.cap.release()
        cv2.destroyAllWindows()