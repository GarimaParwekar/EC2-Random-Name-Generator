import random
import string

No_of_EC2_Instances = int(input('Please enter how many EC2 instances you want name for ? '))
Department_Name = input('Enter your Department name ')
while True:
    for i in range(No_of_EC2_Instances):
        Random_Character = random.choices(string.ascii_letters)
        Random_Number = random.randint(0,9)
        Random_EC2_Instance_Name = Department_Name + Random_Character+str(Random_Number)
        print('Name of the EC2 instance is' , Random_EC2_Instance_Name)
    break 


        

