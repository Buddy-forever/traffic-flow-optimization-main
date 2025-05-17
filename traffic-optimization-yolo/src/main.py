import os
import cv2
import sys

# Fix Python import path to allow running as a script
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.detector import VehicleDetector
from src.counter import VehicleCounter
from src.optimizer import TrafficOptimizer
from utils.helpers import draw_lanes, draw_counts, draw_timings  # Optional helper imports

def main(video_path):
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    detector = VehicleDetector()
    counter = VehicleCounter()
    optimizer = TrafficOptimizer()

    # Define lane regions (example values)
    lane_regions = {
        'lane1': (100, 200, 300, 400),
        'lane2': (400, 200, 600, 400)
    }

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect_vehicles(frame)
        lane_counts = counter.count_vehicles(detections, lane_regions)
        timings = optimizer.optimize(lane_counts)

        # Draw overlays (optional: use helpers.py if available)
        for lane, count in lane_counts.items():
            x1, y1, x2, y2 = lane_regions[lane]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{lane}: {count}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        cv2.imshow("Traffic Monitoring", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Adjust path as needed; this assumes running from project root
    main("dataset/sample_video.mp4")
