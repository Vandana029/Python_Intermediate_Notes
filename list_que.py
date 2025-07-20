# Flatten a list of lists into a single list
'''
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # Recursively flatten the sublist
        else:
            result.append(item)  # Append the item if it's not a list
    return result

# Find the longest sublist in a list of lists
def find_longest_sublist(lst):
    return max(lst, key=len)        
    # longest = []
    # for item in lst:
    #     if isinstance(item, list):
    #         if len(item) > len(longest):
    #             longest = item
    # return longest  

#print(find_longest_sublist([[1, 2, 3], [4, 5, 6, 7], [8]]))  # Output: [4, 5, 6, 7]
my_list = ['A']
my_list.insert(3, 'B')
print(len(my_list))  # Output: 2
# print all elements in my_list
for i in my_list:
    print(i)  # Output: A, B
'''

