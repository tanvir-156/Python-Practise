#multiples of 3(1 to 50) =>21

for i in range(1, 51):
    if(i==21):
        break
    if(i % 3== 0):
        print(i)

print("out of loop")