"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
  LIMITATION = 1000
  LIMIT = LIMITATION-1
  sum_of_3 = summation((LIMIT//3))*3
  sum_of_5 = summation((LIMIT//5))*5
  sum_of_15 = summation((LIMIT//15))*15
  result = sum_of_3+sum_of_5-sum_of_15
  print('Under '+str(LIMITATION)+' the sum of multiple :\n'+str(result))

def summation(x):
  return (x*(x+1))//2


if __name__=='__main__':
  main()
