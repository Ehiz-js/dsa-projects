# import sys

# input = sys.stdin.read()
# tokens = input.split()
# a = int(tokens[0])
# b = int(tokens[1])
# print(a+b)

def sum():
  input1 = int(input("Enter a number between 0 and 9: "))
  input2 = int(input("Enter another number between 0 and 9: "))
  if input1>9 or input2>9 or input1<0 or input2<0 :
    print("please enter a number between 0 and 9")
  else:
    sum = input1 + input2
    print(sum) 
  
sum()

