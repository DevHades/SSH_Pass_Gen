import random, string, os
from colorama import *

Main_Colour = Fore.LIGHTGREEN_EX
Secondary_Colour = Fore.WHITE

File_Name = "SSH_Pass.hades"

class SSH_Pass_Gen():

	def Clear():
		os.system('cls' if os.name == 'nt' else 'clear')

	def Gen(Password_Length):
		c = string.ascii_letters + string.digits + '!@#$%^&*()[].<>,'
		p = (''.join(random.SystemRandom().choice(c) for i in range(int(Password_Length))))
		return p

	def Write_To_File(p):
		print(Secondary_Colour+"["+Main_Colour +"Hades/SSH"+Secondary_Colour+"]: Writing SSH Password To File: "+ File_Name)
		f = open(File_Name, "w")
		f.write(p)
		f.close()

	def Main():
		Valid_Number = False
		Write_To_File = False
		while not Valid_Number:
			Password_Length = input(Secondary_Colour +"Enter Password Length"+Main_Colour +": ")
			if Password_Length.isdigit():
				Valid_Number = True
				while not Write_To_File:
					answer = input(Secondary_Colour +"Write To File?"+Main_Colour +"(y/n): ")
					if answer.lower() == "y":
						SSH_Pass_Gen.Write_To_File(SSH_Pass_Gen.Gen(Password_Length))
						Write_To_File = True
					elif answer.lower() == "n":
						print(Secondary_Colour+"["+Main_Colour +"Hades/SSH"+Secondary_Colour+"]: " + SSH_Pass_Gen.Gen(Password_Length))
						Write_To_File = True
					else:
						print(Secondary_Colour+"["+Main_Colour +"Hades/SSH"+Secondary_Colour+"]: Invalid Response")
			else:
				print(Secondary_Colour +"Please Enter A Integer")

SSH_Pass_Gen.Clear()
SSH_Pass_Gen.Main()

