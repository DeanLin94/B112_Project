from ultralytics import YOLO
import cv2

class WeedDetector:
    def __init__(self, model_path):
        print(f"Loading Module：{model_path} ...")
        try:
            self.model = YOLO(model_path, task="detect")
            print("Susseced")
        except Exception as e:
            print(f"Failed：{e}")
            self.model = None

    def detect(self, source, conf=0.5):
        if self.model is None:
            return [], source
        
        results = self.model(source, conf=conf, verbose=False, stream=True)
        
        detections = []
        annotated_img = source.copy()

        for result in results:
            annotated_img = result.plot()
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf_score = box.conf[0].item()
                cls_id = int(box.cls[0].item())
                class_name = result.names[cls_id]

                detections.append({
                    "class": class_name,
                    "confidence": conf_score,
                    "center": (int((x1 + x2) / 2), int((y1 + y2) / 2)),
                    "box": (x1, y1, x2, y2)
                })

        return detections, annotated_img