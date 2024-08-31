#search string
s = str(input('Enter the string:'))

#pre-compute stage
hash_arr = [0]*26
for i in range(len(s)):
    hash_arr[ord(s[i])-ord('a')] += 1 

#fetch input char
q = int(input("enter number of question: "))
while q != 0:
    if q < 1:
        break
    c = ord(str(input("Enter char to fecth:"))) - ord('a')
    q -= 1
    print(hash_arr[c])

print(hash_arr)