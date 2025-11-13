text=input("enter a string:")
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print("character frequencies:")
for key,value in freq.items():
    print(f"'{key}':{value}")
