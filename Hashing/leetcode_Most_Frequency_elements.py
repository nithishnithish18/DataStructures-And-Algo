arr = [1,1,1,1,5,6,7,7]
k = 9
maxi = max(arr)

hash_map = dict()
for i in range(len(arr)):
    if arr[i] <= maxi:
        diff = maxi-arr[i]
        if diff <= k:  
            arr[i] = arr[i]+diff
            k = k - diff

    