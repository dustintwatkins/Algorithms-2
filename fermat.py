import random 

#Assuming each has n-bits

#complexity: O(tn) + O(nlog(N)) + O(n)
#space: O(n^2)
def carmichael_test(N): 
	b = 2 #space: O(n) bits 
	while b < N: # will happen t = N-b-1 times: O(tn)
		#check if b is relatively prime to N and passes mod_exp function, if so it is prime 
		
		#gcd(euclids) complexity: O(log(n*b + n* N))
		#	      space: O(2n) = O(n)	
		#mod_exp: complexity: O(N*n*log(N*n))
		#	  space: O(3n) = O(n) but the recursive call itself is O(n^2)
		if(gcd(b,N) == 1 and mod_exp(b, N-1, N)): 
			return 0;
		b = b+1 			#space: O(n) 
	
	return 1;

#complexity: O(xn) * O(nlog(N*n)) 
#space: O(2n) = O(n)
def prime_test(N, k):
	
	#space: O(n*k)
	rand_numbers = random.sample(range(2, N-2), k) 

#	for x in rand_numbers:This was used to verify the numbers were not repeated
#		print(x)	

	for x in rand_numbers:			#complexity: O(x * n)
		if(mod_exp(x, N-1, N) != 1):	#complexity: O(nlog(N*n))
			return 'composite'	#space: O(n) but recursive call is O(n^2)

	if(carmichael_test(N)): 		#complexity: O(tn) + O(nlog(N)) + O(n)
		return 'composite'
	return 'prime'		

#complexity: O(log(n * N))
#space: O(3n) = O(n)  
def mod_exp(x, y, N):
	if y == 0:
		return 1
	z = mod_exp(x, y//2, N)
	
	if y % 2 == 0:				#y is even
		return (z*z) % N		#complexity for multiplication: O(z*n)^2 = O(n^2)
	else:					#y is odd
		return x * (z*z) % N		#complexity: O(x*n +z*n)^2 = O(n)

#Dr. Farrell said not to do complexity for probability
def probability(k):
    return 1 -(1/(2**k))


#Perform Euclids algorithm to get gcd
#Complexity: O(log(a+b)) for  Euclids algorithm
#space: O(a*n + b*n) = O(n)
def gcd(a,b):
	if(a < b): 
		return gcd(b,a)			#same complexity & space 
	if(a % b == 0):
		return b

	return gcd(b, a % b) 


