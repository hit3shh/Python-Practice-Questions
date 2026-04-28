'''
Q- Train Ticket Booking

Story:
Seats available → confirm 
Else → waitlist

If VIP → override

Tag: IRCTC (Practice Scenario) 2023

Input: Seats = 0 VIP = Yes

Output: Ticket Confirmed

'''

avail=0
seats = int(input("Seats Required: "))
vip = input("Enter vip status (yes/no): ")

if vip=="yes"  or seats<=avail :
    print("ticket confirmed")

else:
    print("waiting..")

