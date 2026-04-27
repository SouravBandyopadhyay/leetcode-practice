class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), key=lambda x:-x[0])

        fleets = []
        for p,s in cars:
            time = (target-p)/ float(s)

            if not fleets or time> fleets[-1]:
                fleets.append(time)
        
        return len(fleets)