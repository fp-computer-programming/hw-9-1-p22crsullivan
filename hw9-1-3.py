# Author: CRS 01/12/22
def find_thing(lst_or_string, to_be_found):
    for i, v in enumerate(lst_or_string):
        try:
            if to_be_found in v:
                print(i)
                break
            elif to_be_found not in lst_or_string:
                print(-1)
                break
        except:
            print("Invalid Input")

find_thing("apple", "p")
