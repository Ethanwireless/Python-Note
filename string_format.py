# string format
# {[argument_index_or_keyword]:[width][.precision][type]}
str = "Floating point {0:20.2f}".format(345.7916732)

array = [34, 66, 12]
str = "A = {0}, B = {1}, C = {2}".format(*array)

str = 'Sam has {red} red balls, {green} yellow balls \
and {0} bats'.format(3, red = 12, green = 31)

print str