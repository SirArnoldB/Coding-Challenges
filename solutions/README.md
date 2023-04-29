---
description: Binary Search Common Patterns
---

# 🚀 Binary Search

{% tabs %}
{% tab title="Python" %}
{% code lineNumbers="true" %}
```python
def binary_search(arr: List[int], target: int) -> int:
    # initialize left and right pointers
    left, right = 0, len(arr) - 1
    # initialize a variable to store the index of first true value
    first_true_index = -1
    
    # loop until left pointer is less than or equal to right pointer
    while left <= right:
        # calculate mid index
        mid = (left + right) // 2
        # check if mid is feasible
        if feasible(mid):
            # if mid is feasible, update first_true_index and move left pointer to mid-1
            first_true_index = mid
            right = mid - 1
        else:
            # if mid is not feasible, move left pointer to mid+1
            left = mid + 1
    
    # return the index of first true value
    return first_true_index

```
{% endcode %}
{% endtab %}

{% tab title="C++" %}
{% code lineNumbers="true" %}
```cpp
int binary_search(vector<int>& arr, int target) {
    // initialize left and right pointers
    int left = 0, right = arr.size() - 1;
    // initialize a variable to store the index of first true value
    int first_true_index = -1;
    
    // loop until left pointer is less than or equal to right pointer
    while (left <= right) {
        // calculate mid index
        int mid = left + (right - left) / 2;
        // check if mid is feasible
        if (feasible(mid)) {
            // if mid is feasible, update first_true_index and move right pointer to mid-1
            first_true_index = mid;
            right = mid - 1;
        } else {
            // if mid is not feasible, move left pointer to mid+1
            left = mid + 1;
        }
    }
    
    // return the index of first true value
    return first_true_index;
}

```
{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code lineNumbers="true" %}
```javascript
function binarySearch(arr, target) {
    // initialize left and right pointers
    let left = 0, right = arr.length - 1;
    // initialize a variable to store the index of first true value
    let firstTrueIndex = -1;
    
    // loop until left pointer is less than or equal to right pointer
    while (left <= right) {
        // calculate mid index
        let mid = Math.floor((left + right) / 2);
        // check if mid is feasible
        if (feasible(mid)) {
            // if mid is feasible, update firstTrueIndex and move right pointer to mid-1
            firstTrueIndex = mid;
            right = mid - 1;
        } else {
            // if mid is not feasible, move left pointer to mid+1
            left = mid + 1;
        }
    }
    
    // return the index of first true value
    return firstTrueIndex;
}

```
{% endcode %}
{% endtab %}
{% endtabs %}
