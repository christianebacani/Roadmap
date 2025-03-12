def minOperations(nums: list[int], k: int) -> int:
    number_of_operations = 0

    for i in range(len(nums)):
        if nums[i] < k:
            number_of_operations += 1

    return number_of_operations
            