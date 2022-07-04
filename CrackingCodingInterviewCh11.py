
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 11 - Testing'''


# 11.1 - Mistake 
# Find the mistake(s) in the following code 

"""
unsigned int i; 
for (i = 100; i >= 0; --i): 
    printf("%d\n", i)

"""

"""
- By definition unsigned int is always greater or equal to zero; change the condition to just i > 0
- Change the %d to %u for proper printing. 
"""

# 11.2 - Random Crashes
