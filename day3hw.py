# Exercise 1

nums = [100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]

def make_negative(nums_list):
    neg_list = []
    for n in nums_list:
        if n > 0: 
            neg_list.append(n * -1)
    return neg_list


make_negative(nums)

# Exercise 2

address = "123 Real Street, Apt. 2, Springfield, OR 43498"

def filtered_address (address):
    list_of_numbers = []
    for n in address:
        if n.isdigit():
            list_of_numbers.append(str(n))
    return list_of_numbers

filtered_address(address)


# Exercise 3

digits = '123'

def added_strings(digits):
    value = int(digits) + 1 
    return str(value) 

x = added_strings(digits)
print(x)

print(type(x))