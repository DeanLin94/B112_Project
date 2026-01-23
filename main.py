import time
import cv2
from detector import WeedDetector
from getImg import CameraHandler

def main():
    # 設定路徑
    MODEL_PATH = "/home/abudy/Desktop/B112Project/best.engine"
    
    cam = CameraHandler(source=0, width=640, height=480)
    detector = WeedDetector(MODEL_PATH)

    prev_time = time.time()
    print("開始執行... 按下 'q' 退出")

    while True:
        # 2. 讀取影像
        ret, frame = cam.get_frame()
        if not ret:
            print("無法讀取攝影機影像")
            break

        # 3. 執行偵測
        dets, show_frame = detector.detect(frame)

        # 4. 計算並顯示 FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        fps_text = f"FPS: {fps:.1f}"
        cv2.putText(show_frame, fps_text, (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

       
        for d in dets:
            print(f"偵測到: {d['class']} | 信心度: {d['confidence']:.2f}")

       
        cv2.imshow("Jetson Nano Detection", show_frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()