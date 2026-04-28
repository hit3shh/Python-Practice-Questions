'''
Q-  Cab Fare System

Story:    
Fare:
• First 5 km → ₹50/km     
• Next 5 → ₹40/km       
• Beyond → ₹30/km    
Night → +20% 

Tag: Uber 2023

Input:
Distance = 12
Night = Yes


Output:
Fare = 624

'''

ride= float(input("enter toal distance covered in KMs : "))
night= input("Night(yes/no): ")
fare=0

if ride<5 :
    fare = ride*50
elif ride<10 :
    fare = 5*50 + (ride-5)*40
else:
    fare = 5*50 + 5*40 + (ride-10)*30

if night=="yes" :
    fare = fare*1.2

print("total fare: ",fare) 

