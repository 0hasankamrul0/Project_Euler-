"""
Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.
"""

def main():
# After 2 number Even number repeats. So the trick is to add every even number 
# with each iteration of while loop

  LIMIT = 4000000
  n1 = 1
  n2 = 2
  n3 = 0
  result = 0
  while n2<LIMIT:
    result += n2
    n3 = n1+n2
    n1 = n3+n2
    n2 = n1+n3
  print('Sum: '+ str(result))


if __name__ == '__main__':
  main()
