size = int(input('Enter Array Size: '))
arr = [0] * size
for i in range(size):
    arr[i] = int(input('enter array element:'))

#pre-compute stage
hash_arr = [0]*100
for i in range(size):
    hash_arr[arr[i]] += 1 

q = int(input("enter numbe of question: "))
while q != 0:
    if q < 1:
        break
    num = int(input("Enter number to fecth:"))
    q -= 1
    print(hash_arr[num])

