
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Big O Notation Practice '''

# Example 1
def foo(array):  
    sum = 0 
    product = 1
    
    # O(N)
    for i in range(0, len(array), 1): 
        sum += array[i]
    
    # O(N)
    for i in range(0, len(array), 1): 
        product *= array[i]
    
    print(sum + ", " + product)

    ''' This function requires O(N) time'''

# Example 2
def printPairs(array): 

    for i in range(0, len(array), 1): # O(N) called N times --> N * N
        for j in range(0, len(array), 1):   # O(N)
            print(array[i] + "," + array[j])
    
    '''This function requires O(N^2) time'''