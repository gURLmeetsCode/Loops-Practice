def is_prime(n): 
	for num in range(2,n):
		print num
		if n % num == 0:
			return False
	
	return True 

print is_prime (5) 		
print is_prime (6)

#Your task is to write a function that checks if a number is a prime number. Then test your function to make sure it works.

#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
