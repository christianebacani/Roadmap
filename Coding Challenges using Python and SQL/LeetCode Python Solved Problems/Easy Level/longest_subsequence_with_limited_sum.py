# 2389.) Longest Subsequence With Limited Sum
# Categories: Array, Binary Search, Greedy, Sorting, Prefix Sum

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        answer = []

        for i in range(len(queries)):
            subsequence = []

            for j in range(len(nums)):
                if sum(subsequence) + nums[j] <= queries[i]:
                    subsequence.append(nums[j])

                else:
                    break
            
            answer.append(len(subsequence))
        
        return answer