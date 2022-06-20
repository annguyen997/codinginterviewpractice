
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 6 - Math and Logic Puzzles'''

# 6.1 - The Heavy Pill
# You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams.
# Given a scale that provides an exact measurement, how would you find the heavy bottle?
# You can use the scale only once. 

'''
Because we can use the scale just once, 19 bottles at least must be weighted. 
If one of the bottles is heavy, the weight would be at least 19.1 grams instead of at least 19.0 grams. 

Let's say one pill is taken from one bottle and two pills from another, possibly heavier, bottle (in order to discover the difference). 
If the heavy bottle is from the first one, the weighting would be 3.1 g; if the other bottle the weight would be 3.2 g. 

It is possible to determine which pills are the heavy bottle by choosing a different number of pills each time. 
In this case, one pill from Bottle #1, two pills from Bottle #2, three pills from Bottle #3, and so on towards Bottle #20. 

20 + 21 / 2 (Based on summation rule) = 210 pills

Finding the bottle number would use differences of the weight of the pills: 1.1 grams - 1.0 gram = 0.1 gram
weight - 210 / 0.1 = bottle number

'''

# 6.2 - Basketball
# You have a basketball hoop and someone says that you can play one of two games. 
# Game #1: You get one shot to make the hoop. 
# Game #2: You get three shots and you have to make two of three shots. 
# If p is the probability of making a particular shot, for which values of p should you pick one game or the other? 

"""
Applying the laws of probability. 

Game 1: 
The probability of winning Game 1 is p, by definition. 

Game 2: 
Allow s(k, n) be the probability of making exactly k shots in n tries. The probability of winning Game 2 is the following:
p = S(2, 3) + S(3, 3)

The probability of winning all three shots is: p^3 

The probability of winnin at least two out of three is: 
p = (making 1 and 2, but not 3) + (making 1 and 3, but not 2) + (making 2 and 3, but not 1) 
  = (p * p * (1 - p)) + (p * (1 - p) * p) + ((1 - p) * p * p)
  = 3(1-p)(p^2)
  = 3(p^2-p^3)
  = 3p^2 - 3p^3

Thus: 
  = p^3 + 3p^2 - 3p^3
  = 3p^2-2p^3


Game 1 should be played if P(Game 1) > P (Game 2)
p > 3p^2 - 2p^3
1 > 3p - 2p^2 - Divide by p on both sides
2p^2 - 3p + 1 > 0 
(2p - 1)(p - 1) > 0 - Distributive property

As p cannot be negative, the terms must be negative. Thus: 
p - 1 < 0
p < 1

2p - 1 < 0 
2p < 1
p < 1/2 

This means Game 1 should be played if 0 < p < 0.5. If p = 0, 0.5, and 1, P(Game 1) = P(Game 2).
"""

