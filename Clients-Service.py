from cryptohash import sha256
DataFile=open('CustomersData.txt','a')
AdminDataDictionary={"Name":"SUHAYB" , "Email":'Admin97334@lucidya.com',"Password":'040670c71a2ddf1f23d5559c15faeb190b12f836a0d2f1dbd0e362797df07acd'}
CustomersDataDictionary={}
print("Enter 1 for SignUp as Customer\nEnter 2 for LogIn as Customer\nEnter 3 for LogIn as Admin")
def SignUpAsCustomer(Name,Email,Password):
  Password=sha256(Password)
  DataFile.write(f"[\nName: {Name}\nEmail: {Email}\nPassword: {Password}\n\n\n]")
  CustomersDataDictionary[Email]=[Name,Password]
def LogInAsCustomer(Email,Password):
  print(f"Hello {CustomersDataDictionary[Email][0]}" if sha256(Password)==CustomersDataDictionary[Email][1] else "Email or Password is wrong!!") if Email in CustomersDataDictionary.keys() else print("Email or Password is wrong!!")
def LogInAsAdmin(Email,Password):
  print(f'Hello My Admin ({AdminDataDictionary["Name"]}) 🙏' if Email==AdminDataDictionary["Email"] and sha256(Password)==AdminDataDictionary["Password"] else "You are not Admin 😡")
def GiveMeYourData():
  Order = input('Enter Service Number: ')
  Name=input('Enter Your Name: ')
  Email=input('Enter Your Email: ')
  Password=input('Enter Your Password: ')
  SignUpAsCustomer(Name,Email,Password) if Order=='1' else LogInAsCustomer(Email,Password) if Order=='2' else LogInAsAdmin(Email,Password)
  
GiveMeYourData()
