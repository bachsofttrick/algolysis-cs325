def kthElement(arr1, arr2, k):
    # Get lengths of arrays
    len1 = len(arr1)
    len2 = len(arr2)
    # Pointer for arr1
    i = 0
    # Pointer for arr2
    j = 0
    # Counter for elements merged
    count = 0

    # Iterate through both arrays until one of them is exhausted
    while i < len1 and j < len2:
        count += 1
        if arr1[i] < arr2[j]:
            # Return whenever we reach the k-th element
            if count == k:
                return arr1[i]
            i += 1
        else:
            # Return whenever we reach the k-th element
            if count == k:
                return arr2[j]
            j += 1

    # If one array is exhausted before reaching the k-th element, continue with the other array.
    while i < len1:
        count += 1
        # Return whenever we reach the k-th element
        if count == k:
            return arr1[i]
        i += 1

    while j < len2:
        count += 1
        # Return whenever we reach the k-th element
        if count == k:
            return arr2[j]
        j += 1

    # If k is out of bounds for the combined array
    return None

print(kthElement([2,3,5],[2,6,7],3))
