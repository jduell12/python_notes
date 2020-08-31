# lists
# group of items - reference by index
# mutable aka can be changed
# allow duplicate items

my_colors = ["blue", "purple", "green"]
# # print(my_colors)

# # add to list
my_colors.append("black")  # adds to end of list
my_colors.insert(2, "orange")  # insert at index 2
# # print(my_colors)

# remove items
my_colors.remove('orange')  # removes orange
my_colors.pop()  # removes last item
del my_colors[1]  # removes item at index 1
# print(my_colors)

# traverse lists --> similar to js arrays
# for i in range(0, len(my_colors)):
#     # access an item
#     print(my_colors[i])

new_colors = ["red", "yellow", "orange"]

# list slices
# 1st item you want: 1st item you DON'T want
primary_colors = new_colors[0:2]
# print(primary_colors)
# 1st item you want --> goes to end
primary_colors = new_colors[1:]
# print(primary_colors)
# : 1st item you DON't want --> starts at beginning
primary_colors = new_colors[:2]
# print(primary_colors)

# list comprehensions
# returns new list of colors with less # than 5 chars
my_colors = ["red", "yellow", "orange", "blue", "green"]
new_colors = [c for c in my_colors if len(c) < 5]
print(new_colors)
