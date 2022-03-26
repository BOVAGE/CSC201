"""
    output this pattern
            1         
          1 2 1       
        1 2 4 2 1     
      1 2 4 8 4 2 1   
    1 2 4 8 16 8 4 2 1
    
=============================

    - 2^0
    - 2^0 2^1 
    - 2^0 2^1 2^2
    - 2^0 2^1 2^2 2^3
    - 2^0 2^1 2^2 2^3 2^4

    In mathematical terms, we can have the pattern
    interpreted as:
        nth term = {2^0 2^1 2^2 ... 2^n}
        write the first four term of this sequence:
        nth term  'concatenated with' reverse of (n-1)th term
        which forms each line of the pattern.
    
    I know the domain of a sequence is always a set of positive
    integers. But programmers start couting from zero so let me assume that
    so domain = [0,1,2,3...]
"""

for i in range(0,5):
	if i == 0:
		l = [str(2**j) for j in range(i+1)]
	else:
		n = [str(2**j) for j in range(i+1)]
		n.pop()
		l = [str(2**j) for j in range(i+1)] + n[::-1]
	print(" ".join(l).center(18))
