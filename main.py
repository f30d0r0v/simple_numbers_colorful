print('''\033[34m 
	Hello, World from my simple project!
	Author: R. Fedorov. 
	This code search simple numbers and write them\033[32m green. \033[34m
	Not simple numbers this code print\033[31m red. 
\033[0m''') 

n = int(input("From 1 to n = ")) 

def red_output(text):
	print("\033[31m "+str(text)+"\033[0m")

def green_output(txt):
	print(f"\033[32m {txt} \033[0m")

def check(n):
	if n<2:
		print("This number is less than 2. Enter another number, please, or word \"stop\"")
		n = input(">>> ")
		if "stop" in n.lower():
			print()
			green_output("Process fineshed.")
			return 0
		else:
			check(int(n))
		return 0
	for i in range(2, n+1):
		j = 2
		f = 1
		while j*j<=i:
			if i%j==0:
				f = 0 
				break
			j+=1 
		if f:
			green_output("Simple number: "+str(i))
		else:
			red_output(f"Not simple number: {i} ({i}%{j}=0)")
check(n)

