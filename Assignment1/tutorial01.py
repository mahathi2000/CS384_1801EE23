# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	#Multiplication Logic 
	multiplication=num1*num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	#DivisionLogic
	division=num1/num2 
	return division
	
def power(num1, num2): #num1 ^ num2
	#PowerLogic 
    if(num2 == 0): return 1
    temp = power(num1, int(num2 / 2))  
      
    if (num2 % 2 == 0): 
        return temp * temp 
    else: 
        if(num2 > 0): return num1 * temp * temp 
        else: return (temp * temp) / num1 
	

def printGP(a, r, n):  
	gp=[]
	for i in range(0, n):
		curr_term = a * pow(r, i)
		gp.append(curr_term)
		print(curr_term, end =" ")
	return gp

def printAP(a, d, n): 
	ap=[]
	# Printing AP by simply adding d 
	# to previous term. 
	curr_term=a 
  
	for i in range(1,n+1):
		ap.append(curr_term) 
		print(curr_term, end=' ') 
		curr_term =curr_term + d 
	return ap

def printHP(a, d, n): 
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





