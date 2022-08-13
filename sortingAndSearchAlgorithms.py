

# Quick Sort
def quickSort(left, right, nums): 
    if len(nums) == 1:      # Terminating condition for recursion. 
        return nums
    
    if left < right: 
        pivot = partitionQS(left, right, nums)  # Obtain the pointer after sorting
        quickSort(left, pivot-1, nums)          # Recursively sort the left values (in relation to pointer)
        quickSort(pivot+1, right, nums)         # Recursively sort the right values
    
    return nums

def partitionQS(left, right, nums): 
    pivot = nums[right]     # Last element will be pivot
    pointer = left          # First element is the pointer

    for i in range(left, right): 
        if nums[i] <= pivot:
            # Swap values smaller than the pivot to the front
            temp = nums[i]
            nums[i] = nums[pointer]
            nums[pointer] = temp
            pointer += 1
    
    # Finally, swap the last element with pointer indexed number
    temp = nums[pointer]
    nums[pointer] = nums[right]
    nums[right] = temp

    return pointer
    
