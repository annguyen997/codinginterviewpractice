
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
# You are given the source to an application which crashes when it is run. 
# After running it ten times in a debugger, you find it never crashes in the same place. 
# The application is single threaded, and uses only the C standard library. 
# What programming errors could be casuing this crash? How would you test each one? 