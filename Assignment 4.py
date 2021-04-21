#Enter the price of the House you wish to Buy
price = float(input("Enter the new house price"))
creditscore = int(input("Enter credit score: "))
#Enter the first name
first_name = input("first_name")
#Enter the last name
last_name = input("last_name")
fullnames = input('first_name +"" + last_name')
#Enter the email
email = input("email")
#Enter the phone number
phone = input('phone')
#Enter the mailing address
physical_address = input("Enter the mailing address")
#Enter the city
city = input("city")
#Enter state
state = input("state")
#Enter the mailing
zipcode = input("zipcode")


if creditscore >= 780 and creditscore <=850:
    downpayment = 0
    credit_status = "Excellent Credit"
    print("Excellent Credit")
    print("Downpayment = " + str(downpayment))
    price = downpayment + price
    print(price)

elif creditscore <= 779 and creditscore >=740:
    downpayment = 0.2 * price
    credit_status = "Very Good Credit"
    print(credit_status)
    print("Downpayment = " + str(downpayment))
    price = downpayment + price
    print(price)

elif creditscore <= 739 and creditscore >=720:
    downpayment = 0.3 * price
    credit_status = "Above average Credit"
    print('Above average Credit')
    print("Downpayment = " + str(downpayment))

elif creditscore <= 779 and creditscore >=740:
    downpayment = 0.2 * price
    credit_status = "Very Good Credit"
    print('Very good Credit')
    print("Downpayment = " + downpayment)

print('='*60)
print            ("OUTPUT OF THE PROGRAM")
print('='*60)


print('Full Names:', fullnames)
print('Physical Address:', physical_address)
print('City:', city,  'State:', state,  'Zipcode:', zipcode)
print() 

print('New House Price: ', price)
print('Down Payment: ', downpayment)
print('Credit Score: ', creditscore)
print('Credit Status: ', credit_status)
print()

print("CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME - ", fullnames)
print('='*60)
