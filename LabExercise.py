#ELIZA KANTAN ANAK BUNIE
#20DDT19F1071

#QUESTION 1(a)
range(11)
for i in range(11):
      print("The square of",i,"is:",i*i) 

#QUESTION 1(b)
limit=11
i=0
sum=0
while i<limit:
    if i%2==0:
        sum=sum+i
    i=i+1
print("The total of even numbers from 0 to 10 is:", sum)

#QUESTION 2
username = input("Please enter your username: ")
password = input("Please enter the password: ")
print(len(password)) 
if not username.isalpha():
    print ("Your password need in numeric")
if len(password)< 5:
    print("Your password need to contain atleast 5 characters")
if not password.isdigit():
    print("Your password must in numeric")
else:
    print("")

#QUESTION 3
car_price = 103300
downpayment=int(input("Please enter your downpayment: "))
year=int(input("Please enter your loan period in years: "))

laon_amount=car_price - downpayment
total_interest=(2.7/100)*laon_amount*year
monthly_installment=(laon_amount+total_interest)/(year*12)
monthly = str(round(monthly_installment, 2))

print("You need to pay RM",monthly,"as your monthly installment")

