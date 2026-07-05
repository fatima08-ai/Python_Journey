import datetime
n = input("Enter habit name: ")
goal_reached = False
APP_CONFIG = ("RoutineRadar", "ver-123")
user_profile = { "habits" : [{ "id" : 1,
                              "name" : n,
                              "history" : set()
                             }]}
while True:
    opt = input("Select an option: \n\n1. View Dashboard \n\n2. Log Progress \n\n3. Exit \n\n>").strip()
    if(opt == "1"):
        for single_habit in user_profile["habits"]:
            print(f"ID: {single_habit['id']} \nHabit: {single_habit['name']} \nDays Done: {len(single_habit['history'])}")
    elif(opt == "2"):
        id=int(input("Enter habit ID:"))
        current_date=datetime.date.today()
        for single_habit in user_profile["habits"]:
            if single_habit["id"] == id:
                single_habit["history"].add(current_date)
                print("Progress logged successfully!")
    elif(opt == "3"):
        break
    else:
        print("Select a valid option!")

         

    