

# print()
########

print "Howdy, Earth!"

with open('out.log', 'w') as f:
    print >>f, "This redirects to a log file"
print "Ending with a coma skips the line break",

# range() and xrange()
#######################

for x in (range(2) + [3]):
    print(x)

for x in xrange(3):
    print(x)

# map() and filter()
#####################

def is_even(num):
    return num % 2 == 0

def power_of_2(num):
    return num * num

# This is going to be badly converted
map(power_of_2, filter(is_even, range(10)))[:4]
# You should change that manually to:
# [x * x for x in range(10) if x % 2 == 0][:4]

# reduce()
#########

def multiply(a, b):
    return a * b
reduce(multiply, range(1, 11))


# zip() and enumerate()
####################

fruits = ["Memberberries", "Gomu Gomu no Mi", "Senzus Beans"]
is_fruit = [True, True, False]
for f, status in zip(fruits, is_fruit)[:2]:
    print(f, status)
for num, f in enumerate(fruits)[:2]:
    print(num, f)

# input() and raw_input()
##########################

res = input("test")
res = raw_input('test')

# cmp()
########

# This is NOT going to be fixed:
famous_last_words = [
    "Yippee ki-yay",
    "Kawabunga",
    "Kamehameha",
]
def compare(first, second):
     if len(first) > len(second):
         return 1
     elif len(first) < len(second):
         return -1
     else:
         return 0

sorted(famous_last_words, cmp=compare)


# long()
########


a = long(1)

# apply()
########

def marvelous_function(param1, param2, like_param2_but_better):
   print(param1)
   print(param2)
   print(like_param2_but_better)

positional_params = ['First', 'Second']
keyword_argument_params = {"like_param2_but_better": "Best"}
apply(marvelous_function, positional_params, keyword_argument_params)

# execfile()
###########

execfile("some_module.py")


# reload()
###########

# This is not going to be converted
reload('os')

# buffer()
############

# This is not going to be converted
buffer("azertyuiop", 3, 7)

# coerce()
###########

# This is not going to be fixed.
coerce(1, 1.3)

# file()
########

# This is not going to be fixed
file('test')

# intern()
###########

intern("test")


# callable()
#############

callable(str)

# dict
########

d = {}
d.viewsitems()[0]
d.has_key('test')

# division
###########

# This won't be converted
1 / 2
