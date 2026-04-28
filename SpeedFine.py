'''
Q- Traffic Fine System Story: A smart traffic system tracks overspeeding vehicles.

If speed > 80 → fine ₹500.

If >100 → ₹1000.

If repeated violation → double fine.

Tag: TCS NQT 2023

Input: Speed = 105 Repeated = Yes

Output: Fine = 2000

'''

speed= int(input("speed: "))
repeated= input("Repeated(yes/no) :  ")
fine=0

if speed>100 :
    if repeated == "yes":
        fine = 2*1000
    else:
        fine = 1000

elif speed >80:
    if repeated == "yes":
        fine = 2*500
    else:
        fine = 500

print("fine: ",fine)