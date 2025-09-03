# Question: Incrementer
# Categories: 7 Kyu

def incrementer(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] + (i + 1)
        
        if nums[i] > 9:
            nums[i] = int(str(nums[i])[-1])
    
    return nums