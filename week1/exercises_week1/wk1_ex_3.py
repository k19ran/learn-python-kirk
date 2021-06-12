'''
Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator.
 The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers,
 letters, and underscore, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''
from __future__ import print_function,unicode_literals

first_var = u'2a01:89c0:0:a012::1'
SECOND_VAR = u'2a01:89c0:0:a012::2'
TH3_ird_VAR = u'2a01:89c0:0:a012::2'
#print(type(first_var))
print("is var1 is equal to var2: {}".format(first_var == SECOND_VAR))
print("is var1 not equalt to var1: {}".format(first_var != TH3_ird_VAR))

#print(first_var,SECOND_VAR,TH3_ird_VAR)
