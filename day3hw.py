#Given an array of positive integers nums, return a list of all of the negative integers.
#Ex. 1
#nums = [1, 3, 5, 7, 8]
#Expected Output: [-1, -3, -5, -7, -8]

#Ex. 2
#nums = [100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]
#Expected Output: [-100, -534, -32, -15, -77, -222, -788, -345, -75645, -22]

nums = [100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]

def make_negative(nums_list):
    neg_list = []
    for n in nums_list:
        if n > 0: 
            neg_list.append(n * -1)
    return neg_list


make_negative(nums)


#Given a string, return a list of all of the digits in the string.
#Ex. 2
address = "123 Real Street, Apt. 2, Springfield, OR 43498"
#Expected Output: ['1', '2', '3', '2', '4', '3', '4', '9', '8']

#Ex. 2
#sentence = "My phone number is (555) 555-4321"
#Expected Output: ['5', '5', '5', '5', '5', '5', '4', '3', '2', '1']

address = "123 Real Street, Apt. 2, Springfield, OR 43498"

