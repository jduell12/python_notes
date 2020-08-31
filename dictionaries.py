# dictionaries
# group of values we reference through their keys
# mutable
# allow duplicate items

# create
my_grades = {
    "Math": "88",
    "Science": "93",
    "English": "91",
    "History": "70"
}

# access
print(my_grades.get("History"))

# add
my_grades["Art"] = 81
print(my_grades)

# change
my_grades["History"] = 80
print(my_grades)

# remove
my_grades.pop('History')  # remove specific item
print(my_grades)
my_grades.popitem()  # remove last item (seen first in terminal)
print(my_grades)

# length
print(len(my_grades))

# traverse
for classGrade in my_grades:
    print(my_grades[classGrade])
