# The FDA recommends that for a healthy, balanced diet, a person on average needs around 2,000 Kcal a day to maintain their weight. As a result, Instacart is set to release a new feature that will
# help customers control their daily intake of calories. Given a list of items in a customer's cart, it will show the items that can be consumed in one day such that their total caloric value is as
# close to 2000 as possible.
#
# Knowing the caloricValue of each bought item, return the 0-based indices of the items to be consumed in one day. If there is more than one option, return the lexicographically smallest one.
#
# Example
#
# For caloricValue = [400, 800, 400, 500, 350, 350], the output should be
# solution(caloricValue) = [0, 2, 3, 4, 5].
#
# Caloric value of items [1, 3, 4, 5] and [0, 2, 3, 4, 5] both sum up to 2000 but since [0, 2, 3, 4, 5] is lexicographically smaller than [1, 3, 4, 5], the answer is [0, 2, 3, 4, 5].
#
# For caloricValue = [150, 900, 1000], the output should be
# solution(caloricValue) = [0, 1, 2].
#
# The total sum of all items (i.e. 2050) is 50 Kcal larger than 2000, so the answer is [0, 1, 2].
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.integer caloricValue
#
# Caloric value of each item in the cart. The total sum of all items is not greater than 104.
#
# Guaranteed constraints:
# 1 ≤ caloricValue.length ≤ 30,
# 2 ≤ caloricValue[i] ≤ 104.
#
# [output] array.integer
#
# The items to consume in a day.

# N -> This is a modified NP-complete known problem as here: https://en.wikipedia.org/wiki/Subset_sum_problem
# This solution is here: https://stackoverflow.com/questions/70324986/python-closest-subset-sum-function
# It does not do the lexicographic sorting, which I imagined they added simply so people like me with basic Googling skills wouldn't just copy paste an answer.


from itertools import combinations


def solution(caloricValue):
    print(closest_subset(2000, caloricValue))


def closest_subset(s, nums):
    return min((
        c
        for i in range(1, len(nums) + 1)
        for c in combinations(nums, i)
    ), key=lambda x: abs(s - sum(x)))
