# Input :
# a = [ [ 1,  2,  3, 4], 
#      [ 5,  6,  7, 8], 
#      [ 9, 10, 11, 12],
#      [13, 14, 15, 16]
#     ]

# Output : [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]


def spiral(r):
    return list(r[0]) + spiral(list(reversed(zip(*r[1:])))) if r else []
