''' Write  a program to calculate the electricity
(accept number of unit from user) according to the
following criteria
    Unit
   Price
   Fist 100 units
   charge            no
   Next 100 units   RS 5
   per units
   After 200 units
   Per units        Rs 10
   (for example if input unit is 350 than
    total bill amount is RS 2000)'''
amt=0
nu=int(input("Enter number of electric unit="))
if nu<=100:
   print("amt=0")
if nu>100 and nu<=200:
    print("amt=(nu-100)*5")
if nu>200:
    amt=500+(nu-200)*10
    print("Amount to pay:",amt)
    
   
