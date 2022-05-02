#Author:Morece Williams
#Date Created: April 25, 2022
#Course: ITT103
#Purpose: This the the code developed for the JamEx limited commission calculator.
#It was developed based off the pseudocode but many changes has been made for improvements.

class_num = input('Enter class number from either 1, 2 or 3: ')

def values():
  global sales_amount
  global sales_person_num
  sales_person_num = str(input("Enter sales person number: "))
  while True:
    try:
      sales_amount = int(input("Enter sales amount: "))
    except ValueError:
      print("Please enter appropriate sales amount")
      continue
    else:
       return sales_amount
       break


while class_num == '1' or class_num == '2' or class_num == '3' :

  if class_num == '1':
    values()
    
    if sales_amount <=1000:
      rate = 0.06
      comm = sales_amount * rate
      print(sales_person_num,' commission is: ',comm)
      class_num = input('Enter class number 1, 2, 3 or enter "End" to end process: ')
    
    elif sales_amount >1000 and sales_amount <2000:
      rate = 0.07
      comm = sales_amount * rate
      print(sales_person_num,' commission is: ',comm)
      class_num = input('Enter class number 1, 2, 3 or enter "End" to end process: ')
       
    elif sales_amount >=2000:
      rate = 0.1
      comm = sales_amount * rate 
      print(sales_person_num,' commission is: ',comm)
      class_num = input('Enter class number 1, 2, 3 or enter "End" to end process: ')
       
  if class_num == '2':
    values()
    
    if sales_amount <1000:
      rate = 0.04
      comm = sales_amount * rate
      print(sales_person_num,' commission is: ',comm)
      class_num = input('Enter class number 1, 2, 3 or enter "End" to end process: ')
      
    if sales_amount >= 1000:
      rate = 0.1
      comm = sales_amount * rate
      print(sales_person_num,' commission is: ',comm)
      class_num = input('Enter class number 1, 2, 3 or enter "End" to end process: ')
      
  if class_num == '3':
    values()
    rate = 0.45
    comm = sales_amount * rate
    print(sales_person_num,' commission is: ',comm)
    class_num = input('Enter class number 1, 2, 3 or enter "End" to end process: ')
    
if class_num == 'End':
  print('Thank you and Goodbye')

else:
  print('Incorrect class input. Please restart and try again.')
