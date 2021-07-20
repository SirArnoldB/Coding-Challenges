# Given a list of sorted numbers and a key, 
# return the index of the key if it exists, None otherwise 

## Algorithm 
# def binary_search(nums, key):
#     if nums is empty:
#         return None
#     if middle element is equal to key:
#         return middle index
#     if middle element is greater than key:
#         binary search left half of nums
#     if middle element is less than 
#         binary search right half of nums

## Recursive Binary Search 
    # utilizes a helper function to keep track of pointers to the section of
    # the list we are currently examining
    # the seach completes when we find the key or the two pointers meet. 
def binary_search(nums, key):
    return binary_search_helper(nums, key, 0, len(nums))
    
def binary_search_helper(nums, key, start_idx, end_idx):
    middle_idx = (start_idx + end_idx) // 2
    if start_idx == end_idx:
        return None
    if nums[middle_idx] > key:
        return binary_search_helper(nums, key, start_idx, middle_idx)
    elif nums[middle_idx] < key:
        return binary_search_helper(nums, key, middle_idx + 1, end_idx)
    else:
        return middle_idx

## Iterative Binary Search
    # manually keeps track of the section of the list we are examining, using the two-pointer technique. 
    # the search either completes when we find the key, or the two pointers meet. 
def binary_search(nums, key):
    left_idx, right_idx = 0, len(nums)
    while right_idx > left_idx:
        middle_idx = (left_idx + right_idx) // 2
        if nums[middle_idx] > key:
            right_idx = middle_idx
        elif nums[middle_idx] < key:
            left_idx = middle_idx + 1
        else:
            return middle_idx
    return None 

# Binary search completes in O(log N) time because each iteration decreases the size of the list by a factor of 2. 
# Its space complexity is constant because we only need to maintain two pointers to locations in the list. 
# Even the recursive solution has constant space with tail call optimization.


