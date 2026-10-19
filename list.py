#List-Mutable

marks=[98, 97, 99, 95, 93]
print(marks)

#Length
print(len(marks))

#index
print(marks[0])

#slicing a list - list(st:end)

print(marks[0:3])
print(marks[-3:-1])

#loop

for score in marks:
    print(score)


marks.append(50)
print(marks)

marks.insert(0, 50)
print(marks)

print(97 in marks) # to check if it is in the list or not
