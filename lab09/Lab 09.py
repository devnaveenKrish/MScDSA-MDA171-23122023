import csv

class ExpenseTracker:
    def __init__(self):
        self.transactions = {
            "Expenses": [],
            "Income": []
        }
        self.load_transactions()

    def store_transaction(self, type, category, cost, desc, date):
        transaction = {
            "Category": category,   
            "Cost": cost,
            "Description": desc,
            "Date": date
        }
        if type == "Expenses":
            self.transactions["Expenses"].append(transaction)
        else:
            self.transactions["Income"].append(transaction)

    def view_transactions(self):
        print("\nIncome Transactions:")
        for income in self.transactions['Income']:
            print(income)

        print("\nExpense Transactions:")
        for expense in self.transactions['Expenses']:
            print(expense)

    def total_income_expense(self):
        total_income = 0
        for income in self.transactions['Income']:
            total_income+=income["Cost"]
        print("The total Income will be: ",total_income)

        total_expense = 0
        for expenses in self.transactions['Expenses']:
            total_expense+=expenses["Cost"]
        print("The total Expense will be: ",total_expense)
        return total_income, total_expense
    

    def load_transactions(self):
        with open('Lab 09/expenseTracker.csv', 'r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                transaction_type = row["Type"]
                self.transactions[transaction_type].append({
                    "Category": row["Category"],
                    "Cost": float(row["Cost"]),
                    "Description": row["Description"],
                    "Date": row["Date"]
                })




expenseTracker = ExpenseTracker()

while True:
    print("\nMenu Options:")
    print("1. Add New Transaction")
    print("2. View Transactions")
    print("3. Calculate Total Income and Expense")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        ExpenseType = input("Please Enter the Type of Entry you would like to choose (Expense/Income): ")
        Category = input("Please Enter the type of Expenditure: ")
        Cost = float(input("Enter the amount of Expenditure: "))
        Description = input("Enter the Descriptions: ")
        Date = input("Enter the Date: ")
        expenseTracker.store_transaction(ExpenseType.title(), Category, Cost, Description, Date)

    elif choice == "2":
        expenseTracker.view_transactions()

    elif choice == "3":
        expenseTracker.total_income_expense()
        

        

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
