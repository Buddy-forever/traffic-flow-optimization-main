from ultralytics import YOLO

class VehicleDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)
        self.vehicle_classes = [2, 3, 5, 7]  # car, motorcycle, bus, truck

    def detect_vehicles(self, frame):
        results = self.model(frame)
        detections = []
        for r in results:
            for box in r.boxes:
                cls = int(box.cls)
                if cls in self.vehicle_classes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detections.append((cls, (x1, y1, x2, y2)))
        return detections
