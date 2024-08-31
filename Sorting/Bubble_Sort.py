arr = [77,66,33,22,44,100,110]

for i in range(len(arr) , 0, -1):
    for j in range(i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp


print(arr)
