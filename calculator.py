# 2.10.2023 
# exercise 1 
# Calculator using python

print(  '''
 
1. Plus (+)
2. Minus (-)
3. Multiply (*)
4. Divide (/)

''')

choose = int(input('Enter your option:'))
print('\n')
num1 = int(input('Enter first number:')) 
num2 = int(input('Enter second number:')) 

def add(num1,num2):
    return num1 + num2

def min(num1,num2):
    return num1 - num2    

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2  




if (choose == 1):
    print(f'Result: {add(num1,num2) }') 
  
elif (choose == 2):
    print(f'Result: {min(num1,num2) }') 

elif (choose == 3):
    print(f'Result: {mul(num1,num2)}') 

elif (choose == 4):
    print(f'Result: {div(num1,num2)}')
    

    
                         

