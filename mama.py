import random
def phonenumber(operator):
 endNum = random.randint (10000000,99999999)
 number = f"01{operator} {endNum}"
 print(number)
print('''CHOIS YOUR OPERATOR 
        [1] GRAMENPHONE
        [2] ROBI
        [3]BAGALALINK''')
chois = input ('ENTER YOUR CHOIS:')
amount =int(input('HOW MANY NUMBER YOUR WHIT:')
)
if chois == '1':
 for i in range (amount +1):
   phonenumber(7)
   
elif chois == '2':
 for i in range (amount +1):
   phonenumber(8)

if chois == '3':
 for i in range (amount +1):
   phonenumber(9)
else:
  print('wrong input')
   
