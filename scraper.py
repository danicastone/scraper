import subprocess
import fileinput
import re

first = 'Max'
last = 'Toth'
city = 'san_francisco-ca'

url = 'https://fastpeoplesearch.com/name/' + first + '-' + last + '_' + city

phone_regex = r'(\(\b[2-9][0-9]{2}\)[-.\s][2-9][0-9]{2}[-. ][0-9]{4}\b)'

# try/catch loops here are probably overkill, but better safe than sorry
try:
     # open the url in lynx and copy all text on the page into copy.txt
     subprocess.run('lynx -dump ' + url + ' > copy.txt', 
     shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f'Command {e.cmd} failed with error {e.returncode}')

try:
     # search for the point where the street address starts, and copy it into address.txt
     subprocess.run('< copy.txt grep -zoP \'(?<=\\[10\\])(?s).*(?=Past)\' > address.txt', 
     shell=True, check=True)
except subprocess.CalledProcessError as e:
     print(f'Command {e.cmd} failed with error {e.returncode}')

phone_input = open('copy.txt', 'r')
# read everything we got from the listing into a string
phone_string = phone_input.read()
phone_input.close()

phone_number = re.search(phone_regex, phone_string)
print(phone_number)

with open('address.txt', 'r') as input:

     #read all the lines of the file into a list
     list = input.readlines()
#     print(regex.match(r'(\b[2-9][0-9]{2}\)[-. ][2-9][0-9]{2}[-. ][0-9]{4}\b)',phone_string))
     with open('database.csv', 'a') as output:
     # write the first and last name on a new line at the bottom of the spreadsheet
     # (with comma delimeters)
          output.write('\n' + first + ',' + last + ',')
     # strip the line break from the end of the street address and write after the name
          output.writelines((list[0]).strip())
     # replace the spaces in the city, state, and zip code with commas, and write to csv
          output.writelines(re.sub('\s+', ',', list[1]) + phone_number.group())
     # then use regular expressions to find the first phone number, and write it to the csv
          print(phone_number)
#          output.writelines(phone_number.group())
     # close the files back up, we like to keep things tidy 
     output.close()
input.close()   
