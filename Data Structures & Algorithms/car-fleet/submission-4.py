class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed), reverse=True)
        cost = []
        for i in range(n):
            temp = float((target - cars[i][0])/cars[i][1])
            if cost:
                if temp > cost[-1]:
                    cost.append(temp)
            else:
                cost.append(temp)
        return len(cost)