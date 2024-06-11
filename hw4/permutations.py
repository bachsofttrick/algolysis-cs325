def permutations(result, str):
    #base Case, print the result when we obtain the result using all characters
    if(len(result) == len(str)):
        print(''.join(result))

    for i in range(len(str)):
        current_choice = str[i]
        print(current_choice)
        
        # If the choice was not already made we chose it to include in our result
        if(current_choice not in result):
            result.append(current_choice)
            print(result)
            #recursively calling permutations function until we obtain our result
            permutations(result, str)
            #Once we have exhausted all possible paths we backtrack
            result.pop()

def permutations_backtracking(str):
    permutations([],str)

permutations_backtracking("ABC")
