# List Comprehension

item =[1,2,3,4]

# I want to create new list by using item and increase each value by 1
# ""
# new_list=[]
# for n in item:
#     new_list.append(n+1)
# print(new_list)
# ""

## LIST COMPREHENSION
# newlist =[new_item for n in item]

new_list =[n+1 for n in item]
print(new_list)

