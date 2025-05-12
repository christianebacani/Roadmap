# Question Name: Write a function to merge two sorted lists into a single sorted list
# Categories: Medium

def merge_sorted_list(lst1: list[int],lst2: list[int]) -> list[int]:
    merged_list = lst1 + lst2
    merged_list = sorted(merged_list)
    
    return merged_list