class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_indexed = []
        for i,p in enumerate(position):
            pos_indexed.append((p,i))
        sorted_p = sorted(pos_indexed, key=lambda x: x[0], reverse=True)
        stack = []
        car_fleet = len(position)
        for pos, speed_index in sorted_p:
            time = (target-pos)/speed[speed_index]
            if stack and stack[-1] >= time:
                car_fleet -= 1
            else:
                stack.append(time)
        return car_fleet

