def feedDog(hunger_level, biscuit_size):
    # Sort both arrays in non-decreasing order
    hunger_level.sort()
    biscuit_size.sort()
    
    # Initialize variables to keep track of satisfied dogs and available biscuits
    satisfied_dogs = 0
    num_biscuits = len(biscuit_size)
    
    # Iterate through each hungry dog
    for hunger in hunger_level:
        # Find the smallest available biscuit that can satisfy the current hungry dog
        for i in range(num_biscuits):
            if biscuit_size[i] >= hunger:
                # Give the biscuit to the dog and remove it from the available biscuits
                num_biscuits -= 1
                biscuit_size.pop(i)
                satisfied_dogs += 1
                break
    
    return satisfied_dogs
