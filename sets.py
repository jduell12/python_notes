# sets - unordered group of items
# mutable --> can only add to set can't change items in set
# does not allow for duplicate items

# create set
my_cities = {"Apex", "Grosse Ile", "Ann Arbor"}

# add
my_cities.add("Raleigh")
# print(my_cities)
my_cities.update(["Holly Springs", "Atlanta"])
# print(my_cities)

# remove
my_cities.remove('Atlanta')
print(my_cities)
my_cities.pop()  # removes last item in set (seen first in terminal)
print(my_cities)

# traverse
for i in my_cities:
    print(i)
