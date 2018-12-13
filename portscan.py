import sys
import subprocess as sp
from colorama import Fore, init
init()

def main():
	clear()
	print(Fore.BLUE+'*'*25)
	print('+ '+Fore.CYAN+'Dank Port Scanner Hax'+Fore.BLUE+' +')
	print('+     '+Fore.CYAN+'Created By Inc'+Fore.BLUE+'    +')
	print('*'*25+Fore.WHITE)
	
	ipVal = raw_input(Fore.GREEN+'Please Enter IP: '+Fore.RED)
	sp.call('nmap -v -A '+ipVal, shell=True)
	
	attemptVal = True
	while attemptVal:
		attempts = raw_input(Fore.GREEN+'Would you like to scan another IP(Y/n)?: '+Fore.RED)

		if attempts.upper() == 'Y':
			main()
			attemptVal = False
		elif attempts.upper() == 'N':
			sys.exit(Fore.WHITE+'Thanks For Using My Script!\n~Inc')

def clear():
	sp.call('clear', shell=True)

if __name__ == '__main__':
	main()
