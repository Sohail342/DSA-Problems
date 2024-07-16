'''Given an array of bird sightings where every element represents a bird 
type id, determine the id of the most frequently sighted type. If more than 1 
type has been spotted that maximum amount, return the smallest of their ids.

Example

ar = [1, 1, 2, 2, 3]
There are two each of types 1 and , 2 and one sighting of type 3. 
Pick the lower of the two types seen twice: type 1.'''

# Problem Name Migratory Birds (HackerRank)

def migratoryBirds(arr):
    # Count the Occurance of element in value ( key=element : value=element_occurence)
    duplicate = {}
    for i in arr:
        if i in duplicate:
            duplicate[i] += 1
        else:
            duplicate[i] = 1
     
    max_count = max(duplicate.values())  # Find greater occurance
    
    # Iterate over Dict (duplicate) and find the keys with greater occurance (max_count)
    most_freq = [b for b, count in duplicate.items() if count == max_count ]
    
            
    return min(most_freq)  # return minimum key Occurance
        
if __name__ == "__main__":       
    
    print(migratoryBirds([3,5,6,6,6,7,7,7]))

