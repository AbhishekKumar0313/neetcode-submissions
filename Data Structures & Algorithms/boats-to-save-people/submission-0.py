class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        light,heavy=0,len(people)-1
        boat=0
        people.sort()
        while light<=heavy:
            if people[light]+people[heavy]<=limit:
                light=light+1
            heavy-=1
            boat+=1
        return boat
            

