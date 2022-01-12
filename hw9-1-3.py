# Author: CRS 01/12/22
def find_thing(lst_or_string, to_be_found):
    for to_be_found, to_be_found in enumerate(lst_or_string):
        if to_be_found in lst_or_string:
            print(lst_or_string)
        elif to_be_found not in lst_or_string:
            print(-1)


find_thing("apple", "p")