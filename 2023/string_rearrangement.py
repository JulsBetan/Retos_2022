def diff(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Las cadenas no tienen la misma longitud.")
    diferences = sum(1 for a, b  in zip(str1, str2) if a != b)
    return diferences

def permutations(sequence):
    if len(sequence) == 1:
        return [sequence]   
    result = []
    for i in range(len(sequence)):
        current = sequence[i]
        remaning = sequence[:i] + sequence[i+1:]   
        for p in permutations(remaning):
            result.append([current] + p)     
    return result
    
def check_sequence(inputArray):
    lenght = len(inputArray)
    for index, value in enumerate(inputArray):
        if index < lenght-1:
            difference = diff(value,inputArray[index+1])
            if  difference != 1:
                return False            
    return True
              
def solution(inputArray):    
    for x in permutations(inputArray):
        if check_sequence(x):
            return True
    return False

print(solution(["ab", 
 "bb", 
 "aa"]))

print(solution(["aba", 
 "bbb", 
 "bab"]))