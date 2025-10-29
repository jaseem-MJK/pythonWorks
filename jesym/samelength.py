list1 = list(map(int, input("Enter elements of first list seperated by space: ").split()))
list2 = list(map(int, input("Enter elements of second list seperated by space: ").split()))

if len(list1) == len(list2):
    print("both lists are of the same length.")
else:
    print("lists are of different lengths.")

if sum(list1) == len(list2):
    print("both lists are of the same sum.")
else:
    print("lists have different sums.")

common_values = set(list1) & set(list2)
if common_values:
    print("common values found:", common_values)
else:
    print("no common values found.")
    
