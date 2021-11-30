'''

- Write a program that takes as input a set of sorted sequences and computes the union of these
- sequences as a sorted sequence. 
- For example, if the input is [3, 5, 7], [0, 6], and [0, 6, 28], then the
- output is 0, 0, 3, 5, 6, 6, 7, 28.

- Hint: Which part of each sequence is significant as the algorithm executes?

'''
# Solution
# -------- # 

'''

- The min-heap is initialized to the first entry of each array, i.e., it is {3, 0, 0}. 
- We extract the smallest entry, 0, and add it to the output which is [0]. 
- Then we add 6 to the min-heap which is {3, 0, 6} now.
- (We chose the 0 entry corresponding to the third array arbitrarily, it would be a perfectly acceptable
- to choose from the second array.) 
- Next, extract 0, and add it to the output which is [0, 0]; then add 6 to the min-heap which is {3, 6, 6}. 
- Next, extract 3, and add it to the output which is [0, 0, 3]; then add 5 to the min-heap which is {5, 6, 6}. 
- Next, extract 5, and add it to the output which is [0, 0, 3, 5]; then add 7 to the min-heap which is {6, 6, 7}. 
- Next, extract 6, and add it to the output which is [0, 0, 3, 5, 6]; assuming 6 is selected from the second array, which has no remaining elements, the min-heap is {7, 6}. 
- Next, extract 6, and add it to the output which is [0, 0, 3, 5, 6, 6]; then add 28 to the min-heap which is {7, 28}. 
- Next, extract 7, and add it to the output which is [0, 0, 3, 5, 6, 6, 7]; the min-heap is {28}. 
- Next, extract 28, and add it to the output which is [0, 0, 3, 5, 6, 6, 7, 28]; now, all elements are processed and the output stores the sorted elements.

Complexity Analysis:
- Let k be the number of input sequences. Then there are no more than k elements in the min-heap.
- Both extract-min and insert take O(log k) time. Hence, we can do the merge in O(n log k) time. 
- The space complexity is O(k) beyond the space needed to write the final result. 
- In particular, if the data comes from files and is written to a file, instead of arrays, we would need only O(k) additional
storage
'''
import heapq 

def merge_sorted_arrays ( sorted_arrays ):
    min_heap = []
    # Builds a list of iterators for each array in sorted_arrays .
    sorted_arrays_iters = [iter(x) for x in sorted_arrays ]

    # Puts first element from each iterator in min_heap.
    for i, it in enumerate( sorted_arrays_iters ):
        first_element = next(it , None)
        if first_element is not None:
            heapq.heappush(min_heap , (first_element , i))
    result = []
    while min_heap:
        smallest_entry , smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters [ smallest_array_i ]
        result.append( smallest_entry )
        next_element = next( smallest_array_iter , None)
        if next_element is not None:
            heapq.heappush(min_heap , (next_element , smallest_array_i ))
    return result

print(merge_sorted_arrays ([[3, 5, 7], [0, 6] , [0, 6, 28]]))
