words=input("Enter words seperated by spaces:").split()
longest_word=max(words,key=len)
print("the longest word is:",longest_word)
print("Length of the longest word:",len(longest_word))
