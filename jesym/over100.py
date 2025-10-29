ints = input("Enter the list of integers seperated by spaces")
parts = ints.split()
n = []
for p in parts:
    n.append(int(p))

print("Before modifying :")
print(n)

result = []
for num in n:
    if num > 100:
        result.append("over")
    else: 
            result.append(num)

print("\n MOdified List :")
print(result)
