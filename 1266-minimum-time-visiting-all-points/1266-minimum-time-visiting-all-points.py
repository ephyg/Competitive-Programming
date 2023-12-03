class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        for i in range(1, len(points)):
            previous_point = points[i - 1]
            current_point = points[i]

            x_distance = abs(current_point[0] - previous_point[0])
            y_distance = abs(current_point[1] - previous_point[1])

            total_time += max(x_distance, y_distance)

        return total_time
