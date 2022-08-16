

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

# Merge Sort
def mergeSort(left, right, nums): 
    if left < right: 

        # Same as (left + right // 2), but this avoids overflow 
        mid = left + (right - left) // 2

        # Sort first and second halves, then merge
        mergeSort(nums, left, mid)
        mergeSort(nums, mid+1, right)
        merge(nums, left, mid, right)

def merge(left, mid, right, nums): 
    leftSize = mid - left + 1
    rightSize = right - mid 

    # Create temporary arrays
    leftArray = [0] * leftSize
    rightArray = [0] * rightSize

    # Copy data to temporary arrays L[] and R[]
    for i in range(0, leftSize): 
        leftArray[i] = nums[left + i]
    
    for j in range(0, rightSize): 
        rightArray[j] = nums[mid + 1 + j]

    # Merge the temporary arrays back into nums[left...right]
    i = 0 
    j = 0       # Initial index of second subarray
    k = left    # Initial index of merged subarray

    while i < leftSize and j < rightSize: 
        if leftArray[i] <= rightArray[j]: 
            nums[k] = leftArray[i]
            i += 1
        else: 
            nums[k] = rightArray[j]
            j += 1
        k += 1
    
    # Copy any remaining elements of L[]
    while i < leftSize: 
        nums[k] = leftArray[i]
        i += 1
        k += 1
    
    # Copy any remaining elements of R[]
    while j < rightSize: 
        nums[k] = rightArray[j]
        j += 1
        k += 1
    

    
