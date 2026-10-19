name="Tony Stark"

grade='B'

#string operations
print(name.upper())
print(name.lower())
print(name)


#find
print(name.find("ark")) # 0 based index
print(name.find("T"))
print(name.find("X"))

# replace
print(name.replace("Tony Stark", "Ironman"))
print(name.replace("Tony", "Ironman"))
print(name.replace("T", "Ph"))


#check for presence
print('S' in name) #True
print('X' in name) #False

#reserved keywords
# True, False, while, for, break, continue
