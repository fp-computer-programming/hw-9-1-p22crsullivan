# Author: CRS 01/12/22
def even_indexes(lst):
    for i, v in enumerate(lst):
        if i % 2 != 0:
            print(v)


even_indexes([1, 2, 3, 4])