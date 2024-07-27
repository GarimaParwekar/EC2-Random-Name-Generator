import random
import string
No_of_EC2_Instances = int(input('Please enter how many EC2 instances you want: '))
Department_Name = input('Enter your Department name: ')
print('List of EC2 instnace names are :')
for i in range(No_of_EC2_Instances):
    Random_Character = ''.join(random.choices(string.ascii_letters, k=3))
    Random_Number = ''.join(random.choices(string.digits,k=3))
    Random_EC2_Instance_Name = Department_Name + '-' + Random_Character + str(Random_Number)
    print( Random_EC2_Instance_Name)
    
