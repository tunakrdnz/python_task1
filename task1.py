#REVERSE A NESTED LIST IN PYTHON

my_list = [[11,12],[131,4],[15,16,17]]
for sub_list in my_list:
  sub_list.reverse()
print(my_list)


#FLATTEN A LIST IN PYTHON

def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


print(flatten([[1, 2, 3, 4], [5, 6, 7], [8, 9], 10]))

