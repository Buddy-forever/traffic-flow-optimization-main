class VehicleCounter:
    def __init__(self):
        self.counts = {}

    def count_vehicles(self, detections, lane_regions):
        lane_counts = {lane_id: 0 for lane_id in lane_regions}
        for cls, box in detections:
            for lane_id, (x1, y1, x2, y2) in lane_regions.items():
                bx1, by1, bx2, by2 = box
                if x1 < (bx1 + bx2) // 2 < x2 and y1 < (by1 + by2) // 2 < y2:
                    lane_counts[lane_id] += 1
        self.counts = lane_counts
        return lane_counts
