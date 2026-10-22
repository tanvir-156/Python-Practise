#Array

li=[1, 2, 4, 6]
li.append(1)
print(li)

li.insert(4,8)#index first value later
print(li)

li.pop() #pop last
print(li)

li.pop(1)
print(li)

li.append(4)
li.append(6)
print(li)


li.remove(6)
print(li)

li.append(9)
del li[1:2]
print(li)

print(li[1:2]) # slice
li = li[1:2] # assign new sliced array


li.append(1)
li.append(2)
li.append(4)

li[1] = 2
print(li)


arr = [0 for i in range(5)] # fill 0, 5 times
# neede predefined array size in 2D array for adjacency matrix

arr.append(5)
print(arr)

ar = [
    [1, 4, 6],
    [2, 6, 8],
    [3, 8, 10]
]


print(ar)


ar[2][2] = 15
ar[0][0] = 10
print(ar)