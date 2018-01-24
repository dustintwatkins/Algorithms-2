import random 

#Assuming each has n-bits
#O(xn) + O(log(N)) + O(n)
def carmichael_test(N): 
	b = 2 
	while b<N: #will happen x = N-b-1 times: O(xn)
		#check if b is relatively prime to N 
		if(gcd(b,N) == 1 and mod_exp(b, N-1, N)): #euclids algorithm is 0(log(N))
			print("returning false")
			return false;
		b = b+1 #O(n)
	
	print("returning true")
	return true;

def prime_test(N, k):

	rand_numbers = [k]#space: n*k bit values 
	for x in range(0,k):#happens k times O(kn)
		rand_numbers.append(random.randint(2, N-1))#randint() is O(n)

	for x in range(2, k+2):
		if mod_exp(x, N-1, N) != 1:
			return 'composite'
	
	print("hello")
#	for x in rand_numbers:
#		if(mod_exp(x, N-1, N) != 1):
#			return 'composite'

	if(carmichael_test(N)):
		return 'composite'
	print("after carmichael")
	return 'prime'		

#O(log(n)) 
def mod_exp(x, y, N):
	if y == 0:
		return 1
	z = mod_exp(x, y//2, N)
	
	if y % 2 == 0:			#y is even
		return (z*z) % N
	else:				#y is odd
		return x * (z*z) % N

#Dr. Farrell said not to do complexity for probability
def probability(k):
    return 1 -(1/(2**k))


#Perform Euclids algorithm to get gcd
#Complexity = O(log(a+b)) for  Euclids algorithm
def gcd(a,b):
	if(a < b):
		print("1")
		return gcd(b,a)
	if(a % b == 0):
		print("2")
		return b

	print("3")
	return gcd(b, a % b)


