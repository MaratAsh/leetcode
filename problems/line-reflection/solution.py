from typing import Optional, Tuple, List


X, Y = 0, 1


class Solution:
    @staticmethod
    def getMinAndMaxByX(points: Optional[list[list[int]]]) -> Tuple[List[int]]:
        _max = _min = points[0]
        for point in points:
            if point[X] > _max[X]:
                _max = point
            if point[X] < _min[X]:
                _min = point
        return _min, _max
    

    def lineReflection(self, points: Optional[list[list[int]]]) -> bool:
        _min, _max = Solution.getMinAndMaxByX(points)
        
        middle_x_diff = (_max[X] - _min[X]) // 2
        middle_x = _min[X] + middle_x_diff

        points_set = set()
        for point in points:
            reflection_point = [
                point[X] + 2 * middle_x - point[X],
                point[Y]
            ]
            if point[X] == middle_x:
                pass
            elif reflection_point in points_set:
                points_set.remove(reflection_point)
            else:
                points_set.add(point)
        return len(points_set) == 0
