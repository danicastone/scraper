import subprocess
import fileinput
import regex

first = 'Max'
last = 'Toth'
city = 'san_francisco-ca'

url = 'https://fastpeoplesearch.com/name/' + first + '-' + last + '_' + city

# try/catch loops here are probably overkill, but better safe than sorry
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
     # write the first and last name on a new line at the bottom of the spreadsheet
     # (with comma delimeters)
          output.write('\n' + first + ',' + last + ',')
     # strip the line break from the end of the street address and write after the name
          output.writelines((list[0]).strip())
     # replace the spaces in the city, state, and zip code with commas, and write to csv
          output.writelines(regex.sub('\s+', ',', list[1]))
     # close the files back up, we like to keep things tidy 
     output.close()
input.close()   
