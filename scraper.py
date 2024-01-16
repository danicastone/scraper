import subprocess
import fileinput
import regex

first = 'Max'
last = 'Toth'
city = 'san_francisco-ca'

url = 'https://fastpeoplesearch.com/name/' + first + '-' + last + '_' + city

try:
     subprocess.run('lynx -dump ' + url + ' > copy.txt', 
     shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f'Command {e.cmd} failed with error {e.returncode}')


try:
    subprocess.run('< copy.txt grep -zoP \'(?<=\\[10\\])(?s).*(?=Past)\' > addresses.txt', shell=True, check=True)
except subprocess.CalledProcessError as e:
     print(f'Command {e.cmd} failed with error {e.returncode}')


with open('addresses.txt', 'r') as file:
     input = file.read()
     input = regex.sub('*\s', ',', input)
with open('database.csv', 'a') as output:
     output.write(input)
   

#with open('addresses.txt', 'r+b') as file:
     # memory-map the file, size 0 means whole file
#     mm = mmap.mmap(file.fileno(),0)
     #read content by line via standard file methods
#     with open('db.csv', 'r+b') as database:
#          database.write(mm.readline())

#     input = file.read()
#     for i, line in enumerate(input):
#          if i == 1:
#               input.replace(line1_search, replace_text)
#               print(input)
#         elif i == 2:
#               data = file.read()
#               data = data.replace(line2_search, replace_text)

#with open(r'addresses.txt', 'w') as file:
#     file.write(input)     #writing replacement data into text file

#print('Text replaced!')
