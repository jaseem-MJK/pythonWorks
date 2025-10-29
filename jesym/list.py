numbers  = list(map(int, input("Enter integers seperated by space: ").split()))
positive_numbers = [num for num in numbers if num > 0]
print("positive numbers:", positive_numbers)

N = int(input("Enter the value of N: "))
squares = [x**2 for x in range(1, N+1) ]
print("squares:", squares)

word = input("Enter a word: ")
vowels = [char for char in word if char in 'aeiou']
print("vowels in word:",vowels)

word2 = input("Enter ordinal word: ")
ordinals = [ord(char) for char in word2]
print("ordinal values of word:", ordinals)
