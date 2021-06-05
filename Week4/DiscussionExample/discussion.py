# We covered pickling and unpickling in these week's lectures. Now that we know how to use the pickle library do some research and compare pickle with cpickle. Also do some research on the dill library. Compare and explain the benefits and write an example for each.

import re

s = 'welcome home'
m = re.match(r'(.*)(.*?)', s)
print(m.group())