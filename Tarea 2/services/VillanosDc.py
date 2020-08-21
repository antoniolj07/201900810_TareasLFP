import csv
print('villanos dc')

with open('data\dc-villanos.csv') as data:
    villanos = csv.reader(data, delimiter='|')
    for villano in villanos:
        print('--------------------------')
        print('Nombre: {0} \nPoder: {1}\nApodo: {2} \nArchinemesis: {3}'.format(villano[0], villano[1], villano[2], villano[3]))
        print('--------------------------')
import main
main.Main()