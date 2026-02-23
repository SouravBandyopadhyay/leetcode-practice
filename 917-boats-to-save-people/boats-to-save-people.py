class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0 
        left, right = 0 , len(people)-1
        while left<=right:
            total = people[left] + people[right]
            if total<= limit:
                left +=1
            
            boat +=1
            right -=1
        
        return boat

                