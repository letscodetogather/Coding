#####################################################################
# Find the triplet from a given list whose some will be equal to s
#
#
#####################################################################
def triplet_sum(l, s):
    l.sort()
    for i in range(len(l)-2):
        a = l[i]
        start = i+1
        end = len(l)-1
        while start < end:
            b = l[start]
            c = l[end]
            if (a+b+c) == s and len(list(set((a, b, c)))) == 3:
                print(a, b, c)
                start = start + 1
                end = end - 1
            elif a+b+c > s:
                end = end - 1
            else:
                start = start + 1

triplet_sum([9,3,5,8,1,4,7,3,6,2], 14)
