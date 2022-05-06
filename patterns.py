#1.pattern
# # # #
# # # #
# # # #
# # # #
for i in range(4): # i - rows
    for j in range(4): # j- columns
        print("# ",end="")
    print()
# 2.pattern
#
# #
# # #
# # # #
print("2nd pattern")
for i in range(4): # i =0,1,2,3
    for j in range(i+1):
        print("# ",end="")
    print()
#3.pattern
# # # #
# # #
# #
#
print("3rd pattern")
for i in range(4,0,-1):
    for j in range(i):
        print("# ",end="")
    print()
