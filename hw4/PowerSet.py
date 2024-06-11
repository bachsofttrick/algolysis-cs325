def powerset(inputSet):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(inputSet)):
            backtrack(i + 1, path + [inputSet[i]])

    backtrack(0, [])
    return result


'''
The time complexity of this implementation is O(2^n), where n is the number of elements in the input set. This is because for each element in the set, we have two choices: either include it in the subset or exclude it. Therefore, there are 2^n possible subsets in the powerset.
'''
