safe_destinations =("Iceland", "Japan", "Switzerland", "South Korea", "Pakistan")
trip_logs = []
name = input("Enter your name: ")
country = input("Enter the name of the country you want to visit: ").title()
daily_budget = float(input("Enter your daily budget: "))
stay_days = int(input("Enter the number of days you are planning to stay: "))
if (country not in safe_destinations):
    print("Sorry! We don't currently offer trips to", country)
else:
    total_cost = daily_budget*stay_days
    if(total_cost > 3000):
        print("This is a luxury trip.")
    else:
        print("This is a budget-friendly trip.")
    summary = f"{name} is travelling to {country} for {stay_days} days. Total cost: ${total_cost}"
    trip_logs.append(summary)
    print (trip_logs)
