class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        cars=list(zip(position,speed))
        cars.sort(reverse=True)
        for position,speed in cars:
            time=(target-position)/speed
            # If stack is empty, this is the first fleet
            # If current car takes MORE time than the fleet ahead,
            # it cannot catch that fleet, so it forms a NEW fleet
            if not stack or stack[-1]<time:
                stack.append(time)
        return len(stack)