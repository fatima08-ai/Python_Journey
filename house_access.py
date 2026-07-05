import datetime
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
names = ("Fatima", "Jawad", "Ayesha")
list = []
password = "1234"
name = input("Enter your name: ")
pw = input("Enter the password: ")
response = input("Is there an emergency (yes/no): ")
if response == "yes":
    emergency = True
else:
    emergency = False
if (name in names and pw == password):
    print("Access Granted!")
    status = "normal"
    log = f"{name} entered in {status} status at {current_time}."
    list.append(log)
    print(list)
elif ((name not in names or pw != password) and emergency == True): 
    print("Access Granted!")
    status = "emergency"
    log = f"{name} entered in {status} status at {current_time}."
    list.append(log)
    print(list)
else:
    print("Access Denied")
