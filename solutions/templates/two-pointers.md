---
description: Two Pointers Common Patterns
---

# 🚀 Two Pointers

**Two pointers: One input, Opposite ends**

{% tabs %}
{% tab title="Python" %}
{% code lineNumbers="true" %}
```python
def fn(arr):
    # initialize left pointer, right pointer, and answer variable
    left = ans = 0
    right = len(arr) - 1

    # loop until left pointer is less than right pointer
    while left < right:
        # do some logic here with left and right
        if CONDITION:
            left += 1
        else:
            right -= 1
    
    # return the answer
    return ans

```
{% endcode %}
{% endtab %}

{% tab title="C++" %}
{% code lineNumbers="true" %}
```cpp
int fn(vector<int>& arr) {
    // initialize left pointer, right pointer, and answer variable
    int left = ans = 0;
    int right = arr.size() - 1;

    // loop until left pointer is less than right pointer
    while (left < right) {
        // do some logic here with left and right
        if (CONDITION) {
            left += 1;
        } else {
            right -= 1;
        }
    }
    
    // return the answer
    return ans;
}

```
{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code lineNumbers="true" %}
```javascript
function fn(arr) {
    // initialize left pointer, right pointer, and answer variable
    let left = ans = 0;
    let right = arr.length - 1;

    // loop until left pointer is less than right pointer
    while (left < right) {
        // do some logic here with left and right
        if (CONDITION) {
            left += 1;
        } else {
            right -= 1;
        }
    }
    
    // return the answer
    return ans;
}

```
{% endcode %}
{% endtab %}
{% endtabs %}
