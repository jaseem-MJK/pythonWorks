colors = input("Enter comma-seperated color names: ")
color_list = colors.split(",")
color_list = [c.strip() for c in color_list]
print("First color:", color_list[0])
print("Last color:", color_list[-1])
