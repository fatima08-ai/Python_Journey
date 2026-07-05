import datetime
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
VIPs = {
    "Alice": "A123",
    "Bob": "B456" 
}
confirmed_guests = set()
name = input("Enter your name: ")
if name != confirmed_guests:
    if name in VIPs:
        password = input("Enter the password: ")
        if password in VIPs[name]:
            print("VIP Access Granted! Enjoy the lounge.")
            confirmed_guests.add(name)
        else:
            print("Wrong password!")
    else:
        confirmed_guests.add(name)
        print("Welcome to the party!")
else:
    print("You are already on the list!")

statement = f"Total number of guests are {len(confirmed_guests)} at {current_time} "
print(statement)

