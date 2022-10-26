# import required package
import re

# take inputs
string = input('Enter any string: ')
 
# special characters
special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

# check string contains special characters or not
if(special_char.search(string) == None):
    print('String does not contain any special characters.')
else:
    print('The string contains special characters.')
