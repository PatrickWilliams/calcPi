#!python
import math


N = input("Enter the number of digits of pi you would like to compute: ")

runs = math.ceil(N/math.log(2))

a_0 = 1.0
b_0 = 1.0/(2.0**(1.0/2.0))
t_0 = 1.0/4.0
p_0 = 1.0

for x in xrange(1,N):

	a = (a_0 + b_0)/2
	b = (a_0*b_0)**(1.0/2.0)
	t = t_0 - p_0*(a_0 - a)**2
	p = 2*p_0

	pi = ((a_0 + b_0)**2)/(4*t)
	print pi
	
	a_0 = a
	b_0 = b
	t_0 = t
	p_0 = p

print 'Pi to %d number of digits is: ' % (N)
print "%0" N "d\n" % pi	 
