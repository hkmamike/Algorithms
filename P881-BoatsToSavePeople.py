class Solution:
    def numRescueBoats(self, people, limit):
        
        #sort people from lightest to heaviest
        people = sorted(people)
        
        #index of lightest person not boarded
        index_light = 0
        #index of heaviest person not boarded
        index_heavy = len(people)-1
        #count of boats used so far
        count = 0
				
        #while not everyone is onboard, keep going
        while index_light <= index_heavy:
            
            #of the people not boarded, if we can put the heaviest and the lightest on a boat, we do it
            if people[index_light] + people[index_heavy] <= limit:
                index_light += 1
                index_heavy -= 1
                
            #otherwise, just put the heaviest person on one boat
            else:
                index_heavy -= 1
                
            #in either case, we use one boat, so we increment the count
            count += 1
            
        return count