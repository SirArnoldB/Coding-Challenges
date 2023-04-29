def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2  # divide array length in half and use the "//" operator to *floor* the result

        left_array = array[:middle]  # fill in left array
        right_array = array[middle:]  # fill in right array

        merge_sort(left_array)  # Sorting the first half
        merge_sort(right_array)  # Sorting the second half

        left_index = 0
        right_index = 0
        current_index = 0

        # compare each index of the subarrays adding the lowest value to the current_index
        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] < right_array[right_index]:
                array[current_index] = left_array[left_index]
                left_index += 1
            else:
                array[current_index] = right_array[right_index]
                right_index += 1
            current_index += 1

        # copy remaining elements of left_array[] if any
        while left_index < len(left_array):
            array[current_index] = left_array[left_index]
            left_index += 1
            current_index += 1

        # copy remaining elements of right_array[] if any
        while right_index < len(right_array):
            array[current_index] = right_array[right_index]
            right_index += 1
            current_index += 1

if __name__ == '__main__':
    array = [12, 11, 15, 10, 9, 1, 2, 3, 13, 14, 4, 5, 6, 7, 8]
    merge_sort(array)
    print(array)