class TrafficOptimizer:
    def __init__(self, base_green_time=30, max_green_time=60):
        self.base_green_time = base_green_time
        self.max_green_time = max_green_time

    def optimize(self, lane_counts):
        total = sum(lane_counts.values()) or 1
        optimized_times = {}
        for lane, count in lane_counts.items():
            proportion = count / total
            optimized_times[lane] = int(proportion * self.max_green_time)
        return optimized_times
