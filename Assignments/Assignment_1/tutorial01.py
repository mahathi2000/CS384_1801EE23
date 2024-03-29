# Function to add two numbers 
def add(num1, num2):
	if(isinstance(num1,(int, float)) and isinstance(num2,(int, float))): 
		addition = num1 + num2
		return addition
	else:
		return 0

# Function to subtract two numbers 
def subtract(num1, num2): 
	if(isinstance(num1,(int, float)) and isinstance(num2,(int, float))):
		subtraction = num1 - num2
		return subtraction
	else:
		return 0

# Function to multiply two numbers 
def multiply(num1, num2): 
	#Multiplication Logic 
	if(isinstance(num1,(int, float)) and isinstance(num2,(int, float))):
		multiplication=num1*num2
		return multiplication
	else:
		return 0

# Function to divide two numbers 
def divide(num1, num2): 
	#DivisionLogic
	if(isinstance(num1,(int, float)) and isinstance(num2,(int, float))):
		if(num2==0):
			return 0
		division=num1/num2 
		return division
	else:
		return 0


def power(num1, num2): #num1 ^ num2
	#PowerLogic
		p = 1
		if num2<0:
			num1 = 1/num1
			num2 = abs(num2)

        # Exponentiation by Squaring

		while num2:
			if num2%2:
				p*= num1
			num1*=num1
			num2//=2
		return round(p, 3)
	

def printGP(a, r, n):
	if(isinstance(a,(int, float)) and isinstance(r,(int, float)) and isinstance(n,int)):  
		gp=[]
		for i in range(0, n):
			curr_term = a * pow(r, i)
			gp.append(curr_term)
			print(curr_term, end =" ")
		return gp
	else:
		return [0]

def printAP(a, d, n):
	if(isinstance(a,(int, float)) and isinstance(d,(int, float)) and isinstance(n,int)): 
		ap=[]
		# Printing AP by simply adding d 
		# to previous term. 
		curr_term=a 
	  
		for i in range(1,n+1):
			ap.append(curr_term) 
			print(curr_term, end=' ') 
			curr_term =curr_term + d 
		return ap
	else:
		return [0]

def printHP(a, d, n):
	if(isinstance(a,(int, float)) and isinstance(d,(int, float)) and isinstance(n,int)): 
		hp=[]
		curr_term=a 
	  
		for i in range(1,n+1):
			if(curr_term==0):
				return 0
			temp=1/curr_term
			hp.append(round(temp, 3)) 
			print(round(temp, 3), end=' ') 
			curr_term =curr_term + d 
		return hp
	else:
		return [0]





