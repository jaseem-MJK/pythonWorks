list1 = input("Enter colors for list 1 (comma-seperated): ").split(",")
list2 = input("Enter colors for list 2 (comma-seperated): ").split(",")

diff = [c for c in list1 if c not in list2]
print("colors in list1 but not in list2:", diff)
