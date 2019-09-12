

# print
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

map(power_of_2, filter(is_even, range(10)))[:4]
# You should change that manually to:
# [x * x for x in range(10) if x % 2 == 0][:4]

# reduce
#########

def multiply(a, b):
    return a * b
reduce(multiply, range(1, 11))


# long
########


a = long(1)

# apply

def marvelous_function(param1, param2, like_param2_but_better):
   print(param1)
   print(param2)
   print(like_param2_but_better)

positional_params = ['First', 'Second']
keyword_argument_params = {"like_param2_but_better": "Best"}
apply(marvelous_function, positional_params, keyword_argument_params)

# execfile

execfile("some_module.py")
