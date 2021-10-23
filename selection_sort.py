######################################################################################################
# sort an arry with minimum swaping 
# l = [9,3,5,8,1,4,7,3,6,2]
# We can do this by two way, one from min and second is max. I have prefered min way(start to end), If you want it 
# through max way then go from end to start.
######################################################################################################




def min_swap(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i, len(arr)):
            if arr[min_pos] > arr[j]:
                min_pos = j

        temp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = temp

arr = [5, 3, 8, 6, 7, 2]
min_swap(arr)

print(arr)
