# 1)	Build a program that:
# •	Displays a list of snacks and drinks with item numbers and prices.
# •	Ask the user to choose items by number in a loop.
# •	 Keeps track of selected items and their prices.
# •	Ends when the user types "done".
# •	Finally prints a receipt showing: List of selected items with prices and total cost

# menu = {
#     1: {"name": "chocholate", "price": 2},
#     2: {"name": "chips", "price": 1},
#     3: {"name": "cookies", "price": 5},
#     4: {"name": "water", "price": 4},
# }

# for number, item in menu.items():
#     print(number, ".", item["name"], "-", "$", item["price"])

# selected_items = []

# while True:
#     choice = input ("Enter item number or 'done': ")

#     if choice == "done":
#         break

#     choice = int(choice)
#     selected_items.append(menu[choice])

# total_price = 0

# for item in selected_items:
#     print(item["name"], "-", "$", item["price"])

#     total_price += item["price"]

# print("\nTotal Price is: ", "$", total_price)



# 2)	Write a program that:
# •	Has a predefined dictionary of groceries with prices.
# •	Lets the user "add" items by typing their names.
# •	For each valid item, asks for the quantity.
# •	Keeps adding to the cart until the user types "checkout".
# •	Displays a final bill: each item, quantity, subtotal, and total.

# def grocery_shopping():
#     groceries ={"apple": 0.5, "banana": 0.3, "milk": 1.2, "bread": 1.5, "eggs": 2.0};

#     print("Welcome to the Grocery Store!")
#     print("Please add items to your cart by typing their names (type 'checkout' to finish):")
#     for item in groceries:
#         print(f"{item} - ${groceries[item]:.2f}")

#     choice = input("Enter item name: ").lower()
#     cart = {}

#     while choice != "checkout":
#         if choice in groceries:
#             quantity = int(input(f"How many {choice}s would you like to add? "))
#             if quantity > 0:
#                 cart[choice] = cart.get(choice, 0) + quantity
#                 print(f"Added {quantity} {choice}(s) to your cart.")
#             else:
#                 print("Quantity must be greater than 0.")

#         else:
#             print("Item not found. Please try again.")
#         choice = input("Enter item name (or 'checkout' to finish): ").lower()
#     if choice == "checkout":
#         print("\nFinal Bill:")
#         total = 0
#         for item, quantity in cart.items():
#             subtotal = groceries[item] * quantity
#             total += subtotal
#             print(f"{item} x {quantity} - ${subtotal:.2f}")
#         print(f"\nTotal: ${total:.2f}")
# grocery_shopping()

# 3)	Build a to-do list manager that
# •	Allows users to add tasks with priorities (e.g., "Buy milk - high").
# •	Lets them view the current list, delete tasks by number, and mark tasks as complete.
# •	Keeps looping until the user types "exit".
# •	Shows a summary at the end: number of completed tasks vs pending.

# tasks = []

# while True:
#     print("\n--- TO-DO LIST MANAGER ---")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Delete Task")
#     print("4. Complete Task")
#     print("Type 'exit' to quit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         task_name = input("Enter task name: ")
#         priority = input("Enter priority (high, medium, low): ")

#         task = {
#             "name": task_name,
#             "priority": priority,
#             "completed": False
#         }

#         tasks.append(task)
#         print("Task added successfully!")

#     elif choice == "2":
#         if len(tasks) == 0:
#             print("No tasks available.")
#         else:
#             print("\nCurrent Tasks:")
#             for i, task in enumerate(tasks, start=1):
#                 status = "Completed" if task["completed"] else "Pending"
#                 print(f"{i}. {task['name']} | Priority: {task['priority']} | Status: {status}")

#     elif choice == "3":
#         if len(tasks) == 0:
#             print("No tasks to delete.")
#         else:
#             for i, task in enumerate(tasks, start=1):
#                 print(f"{i}. {task['name']}")

#             try:
#                 task_num = int(input("Enter task number to delete: "))
#                 if 1 <= task_num <= len(tasks):
#                     removed_task = tasks.pop(task_num - 1)
#                     print(f"Deleted: {removed_task['name']}")
#                 else:
#                     print("Invalid task number.")
#             except ValueError:
#                 print("Please enter a valid number.")

#     elif choice == "4":
#         if len(tasks) == 0:
#             print("No tasks available.")
#         else:
#             for i, task in enumerate(tasks, start=1):
#                 print(f"{i}. {task['name']}")

#             try:
#                 task_num = int(input("Enter task number to mark complete: "))
#                 if 1 <= task_num <= len(tasks):
#                     tasks[task_num - 1]["completed"] = True
#                     print("Task marked as complete!")
#                 else:
#                     print("Invalid task number.")
#             except ValueError:
#                 print("Please enter a valid number.")

#     elif choice == "5" or choice.lower() == "exit":
#         break

#     else:
#         print("Invalid option. Try again.")

# completed_count = 0
# pending_count = 0

# for task in tasks:
#     if task["completed"]:
#         completed_count += 1
#     else:
#         pending_count += 1

# print("\n--- Summary ---")
# print(f"Completed Tasks: {completed_count}")
# print(f"Pending Tasks: {pending_count}")
# print(f"Total Tasks: {len(tasks)}")



# 4)	 Movie Ticket Booking Simulation
# -	Simulate a movie theater booking system that:
# •	Shows a list of available movie titles, showtimes, and seat prices.
# •	Asks the user to choose a movie and number of tickets.
# •	 Confirms total price and asks if they want to book another movie.
# •	 Ends when they say "no" and displays total bookings and cost.

# def movie_ticket_booking():
#     movies = {
#         "inception": {
#             "showtime": "7:00 PM",
#             "price": 10.0,
#             "total_bookings": 0
#         },
#         "the matrix": {
#             "showtime": "9:00 PM",
#             "price": 12.0,
#             "total_bookings": 0
#         },
#         "interstellar": {
#             "showtime": "6:00 PM",
#             "price": 15.0,
#             "total_bookings": 0
#         }
#     }

#     total_cost = 0

#     print("Welcome to the Movie Ticket Booking System!")

#     while True:
#         print("\nAvailable movies:")
#         for movie in movies:
#             print(f"- {movie}: {movies[movie]['showtime']} - ${movies[movie]['price']:.2f}")

#         customer_choice = input(
#             "\nEnter movie name (or type 'exit' to finish): "
#         ).lower()

#         if customer_choice == "exit":
#             break

#         if customer_choice in movies:
#             num_tickets = int(
#                 input(f"How many tickets for {customer_choice}? ")
#             )

#             if num_tickets > 0:
#                 cost = num_tickets * movies[customer_choice]["price"]
#                 total_cost += cost
#                 movies[customer_choice]["total_bookings"] += num_tickets

#                 print(
#                     f"Total cost for {num_tickets} tickets to "
#                     f"{customer_choice}: ${cost:.2f}"
#                 )
#             else:
#                 print("Number of tickets must be greater than 0.")
#         else:
#             print("Movie not found. Please try again.")

#     print("\nBooking Summary:")
#     total_bookings = 0

#     for movie in movies:
#         if movies[movie]["total_bookings"] > 0:
#             print(
#                 f"{movie}: "
#                 f"{movies[movie]['total_bookings']} tickets booked."
#             )
#             total_bookings += movies[movie]["total_bookings"]

#     print(f"\nTotal tickets booked: {total_bookings}")
#     print(f"Total Cost: ${total_cost:.2f}")


# movie_ticket_booking()


# 5)	Create a basic quiz game that:
# •	Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# •	Ask the user each question and records their answers.
# •	At the end, displays:
# o	 The user's score (e.g., 7/10)
# o	Correct answers for any questions they got wrong

# questions = [
#     {"question": "What is 2 + 2?", "answer": "4"},
#     {"question": "What is the capital of Italy?", "answer": "Rome"},
#     {"question": "What color is the sky?", "answer": "Blue"},
#     {"question": "What is 5 + 3?", "answer": "8"},
#     {"question": "What language are we learning?", "answer": "Python"}
# ]

# score = 0
# wrong_answers = []

# for question in questions:
#     user_answer = input(question["question"] + " ")

#     if user_answer.lower() == question["answer"].lower():
#         print("Correct")
#         score += 1
#     else:
#         print("Wrong. The correct answer is", question["answer"])
#         wrong_answers.append(question)

# print("\nFinal Score:", score, "/", len(questions))

# print("\nCorrect answers for questions you got wrong:")
# for question in wrong_answers:
#     print(question["question"])
#     print("Correct answer:", question["answer"])



# 6)	You receive log records:
# logs = [
#    {"user": "alice", "action": "login"},
#    {"user": "bob", "action": "login"},
#    {"user": "alice", "action": "purchase"},
#    {"user": "", "action": "login"},
#    {"user": "charlie", "action": None},
#    {"user": "bob", "action": "logout"}
# ]

# Build a program that:
# •	Remove invalid records where:
# o	user is empty OR
# o	action is missing (None)
# o	Count actions per user (dictionary)
# o	Count frequency of each action (dictionary)
# o	Cleaned record count
# o	User activity summary
# o	Most common action


# Expected Output
# Cleaned Records: 4

# User Activity:
# {
#     "alice": 2,
#     "bob": 2,
#     "charlie": 0
# }

# Action Counts:
# {
#     "login": 2,
#     "purchase": 1,
#     "logout": 1
# }

# Most Common Action: login

# logs = [
#     {"user": "alice", "action": "login"},
#     {"user": "bob", "action": "login"},
#     {"user": "alice", "action": "purchase"},
#     {"user": "", "action": "login"},
#     {"user": "charlie", "action": None},
#     {"user": "bob", "action": "logout"}
# ]

# cleaned_logs = []
# user_activity = {}
# action_counts = {}

# for log in logs:
#     if log["user"] != "" and log["action"] != None:
#         cleaned_logs.append(log)

# for log in cleaned_logs:
#     user = log["user"]

#     if user not in user_activity:
#         user_activity[user] = 1
#     else:
#         user_activity[user] += 1

# for log in cleaned_logs:
#     action = log["action"]

#     if action not in action_counts:
#         action_counts[action] = 1
#     else:
#         action_counts[action] += 1

# most_common_action = ""
# highest_count = 0

# for action, count in action_counts.items():
#     if count > highest_count:
#         highest_count = count
#         most_common_action = action

# print("\nCleaned records: ", len(cleaned_logs))
# print("\nUser Activity:")
# print(user_activity)

# print("\nAction Counts:")
# print(action_counts)

# print("\nMost Common Action:", most_common_action)
