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
     subprocess.run('< copy.txt grep -zoP \'(?<=\\[10\\])(?s).*(?=Past)\' > addresses.txt', 
     shell=True, check=True)
except subprocess.CalledProcessError as e:
     print(f'Command {e.cmd} failed with error {e.returncode}')


with open('addresses.txt', 'r') as input:
     #read all the lines of the file into a list
     list = input.readlines()
     with open('database.csv', 'a') as output:
          output.write('\n' + first + ',' + last + ',')
          output.writelines((list[0]).strip())
          output.writelines(regex.sub('\s+', ',', list[1]))
#     temp_line = list[1]
 #    print(list)
 #    print(list[1])
 #    print(temp_line)
#     with open ('temp.txt', 'w') as temp:
#          temp.writelines(temp_line)
#          regex.sub('\s+', ',', temp.txt)
#          print(temp_line) 
#          list[1] = temp.readlines()
#          print(list[1])
#          with open ('database.csv', 'a') as output:
#               output.writelines(list[0])
#               output.writelines(list[1])
#               i.replace('/n/[ ]*|[ ]+/g', ',')
#               output.writelines(i)

input.close()
output.close()   
