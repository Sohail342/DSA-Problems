'''
You are given an integer array score of size n, where score[i] is the score of the ith athlete 
in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, 
the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number 
(i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.


'''

# Approach 1
def findRelativeRanks(score=[]) -> list[str]:
    sorted_scores = sorted(score, reverse=True)
    
    rank_dict = {}
    for i, s in enumerate(sorted_scores):
        if i == 0:
            rank_dict[s] = "Gold Medal"
        elif i == 1:
            rank_dict[s] = "Silver Medal"
        elif i == 2:
            rank_dict[s] = "Bronze Medal"
        else:
            rank_dict[s] = str(i + 1)
    
    return [rank_dict[s] for s in score]

'''
Time Complexity:

1. Sorting the score list takes 𝑂(nlogn), where n is the length of the list.
2. Filling the rank_dict dictionary takes O(n) because you iterate through the sorted_scores.
3. Constructing the final list of ranks also takes O(n), as you perform a lookup for each element in the original score list.

Overall Time Complexity: O(nlogn) (dominant term is the sorting operation)

'''

# Approach 2
import copy 

def findRelativeRanks_two(score=[]) -> list[str]:
    copy_scores = copy.deepcopy(score)
    copy_scores.sort(reverse=True)
        
    for value  in range(len(copy_scores)):
        if value == 0:
            score.insert(score.index(copy_scores[value]), "Gold Medal")
            score.remove(copy_scores[value]) 
        elif value == 1:
            score.insert(score.index(copy_scores[value]), "Silver Medal")
            score.remove(copy_scores[value]) 
        elif value == 2:
            score.insert(score.index(copy_scores[value]), "Bronze Medal")
            score.remove(copy_scores[value]) 
        else:
            score.insert(score.index(copy_scores[value]), str(value+1))
            score.remove(copy_scores[value])  
        
        
    return score

'''
Time Complexity:

1. Creating a deep copy of the score list takes O(n).
2. Sorting the copy_scores list takes O(nlogn).
3. The loop that processes each score element runs in O(n) times. However, within the loop, each insert and remove operation could take 
O(n) due to the underlying list operations, leading to a complexity of O(n^2) for these operations.

Overall Time Complexity: O(n^2) due to the costly insert and remove operations inside the loop.

'''

if __name__ == "__main__":
    print(findRelativeRanks([9,8,6,4,2,1,10]))
    print(findRelativeRanks_two([9,8,6,4,2,1,10]))
    
    # Approach 1 is generally preferable, especially for larger input sizes.