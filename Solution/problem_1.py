"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,   
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
# Limit//n -> tells how many multiples there are in limit of 'n'
# substrating summation of the multiples of 15 beacause this part is 
# added both by summation of 3 and 5
  LIMITATION = 1000
  LIMIT = LIMITATION-1    # Under Limitation thus -1
  sum_of_3 = summation((LIMIT//3))*3
  sum_of_5 = summation((LIMIT//5))*5
  sum_of_15 = summation((LIMIT//15))*15
  result = sum_of_3+sum_of_5-sum_of_15
  print('Under '+str(LIMITATION)+' the sum of multiple :\n'+str(result))

def summation(x):
  return (x*(x+1))//2


if __name__=='__main__':
  main()
