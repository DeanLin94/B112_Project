import cv2
from detector import WeedDetector
from getImg import CameraHandler
from pespective_trans import perspective_trans

def main():
    cam = CameraHandler(source=0) 
    MODEL_PATH = "/home/deanlin/Desktop/MyProject/大專生計畫/Yolo_Detection/yolo11n.pt"
    try:
        detector = WeedDetector(MODEL_PATH)
    except Exception as e:
        print(f"模型載入失敗: {e}")
        return

    while True:
        # 獲取影像與當前 FPS
        ret, frame, fps = cam.get_data()
        if not ret:
            break

        # 影像校正與偵測
        corrected_frame = perspective_trans(frame)
        dets, show_frame = detector.detect(corrected_frame)

        # FPS
        cv2.putText(show_frame, f"FPS: {fps:.1f}", (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        cv2.imshow("Jetson Nano Detection", show_frame)

        if cv2.waitKey(1) == ord('q'):
            break

    # 3. 釋放資源
    cam.release()

if __name__ == "__main__":
    main()