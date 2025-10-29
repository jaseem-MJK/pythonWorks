line = input("Enter a line of text: ")

line = line.lower()

words = line.split()

wc = {}

for word in words:
    wc[word] = wc.get(word, 0) + 1

print("\nWord occurrences:")
for word, count in wc.items():
    print(f"{word}: {count}")
    
