class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_p = list(zip(position,speed))
        sorted_p.sort( key=lambda x: x[0], reverse=True)
        prevTime = 0
        car_fleet = len(position)
        for pos, speed in sorted_p:
            time = (target-pos)/speed
            if prevTime >= time:
                car_fleet -= 1
            else:
                prevTime = time
        return car_fleet

