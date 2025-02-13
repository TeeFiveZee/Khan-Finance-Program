import statistics
#Declare income, exepenses, and savings
class Khan:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.savings = 0
    
    #Prompting the user to enter their yearly income
    def user_income(self):
        while True:
            try:
                amount = float(input("Please enter your Yearly Income $$: "))
                if amount < 0:
                    print("\n It cannot be a negative number....")
                    continue
                self.income = amount
                break
            except ValueError:
                print("\n That is not a valid number..")
#Prompting the user to enter their savings amoung which is validated.
    def user_saving(self):
        while True:
            try:
                amount = float(input("\n Please enter amount you want to save: $$"))
                if amount < 0:
                    print("It cannot be a negative number...")
                    continue
                self.savings = amount
                break
            except ValueError:
                print("\nThat is not a valid number...")
       #allows the user to add as many expenses as needed with its own catagory.
    def user_expense(self):
        while True:
            prompt = input("Would you like to add an expense? (y/n): ").lower()
            if prompt == "n":
                break
            category = input("Enter category for the expense:")
            while True:
                try:
                    amount = float(input("Enter the amount of the expense: "))
                    if amount < 0:
                        print("\n It cannot be a negative number")
                        continue
                    if category in self.expenses:
                        self.expenses[category] += amount
                    else:
                        self.expenses[category] = amount
                    break
                except ValueError:
                    print("\nThat is not a vlid number...")
    #This gives the user a summary of all their finances
    def user_summary(self):
        total_expenses = sum(self.expenses.values())
        balance = self.income - total_expenses - self.savings
        summary = {
            "Income": self.income,
            "Savings": self.savings,
            "Total Expense": total_expenses,
            "Balance": balance,
            "Expenses": self.expenses
            }
        
        return summary # Returns the financial summary as a dictionary.
    #Saving the information to a text file.
    def savefile(self, filename="finances.txt"):
        with open(filename, "w") as file:
            for key, value in self.user_summary().items():
                file.write(f"{key}: {value}\n")
            print("Your file has been saved to Finances.txt")
     #Adds budget tracking and allows the user to choose if they would like to do so.   
class BudgetPlanner(Khan):
    def __init__(self):
        super().__init__()
        self.budget = {}
    
    def user_budget(self):
       print("Now you will set your budget for different categories.")
       while True:
           prompt = input("Do you want to set a budget? (y/n): ").lower()
           if prompt == "n":
               break
           category = input("Enter the budget category: ")
           while True:
                try:
                    amount = float(input("Enter Budget Amount:"))
                    if amount < 0:
                        print("You cannot have a negative budget\n")
                        continue
                    self.budget[category] = amount
                    break
                except ValueError:
                    print("That is not a valid number...\n")
         #compares the users budget with the amount spent and show how much they went over or under budget
    def compare_user_budget(self):
        comparison = {}
        for category, budgeted in self.budget.items():
            spent = self.expenses.get(category, 0)
            saved = budgeted - spent
            comparison[category] = {"Budget": budgeted,
                                    "Amount Spent": spent,
                                    "Saved": saved}
        return comparison            

   #Main function which execture the program. 
def main():
    program = BudgetPlanner()
    
    print("Welcome to Khan Finance Services")
    #Create an instance of all tools
    program.user_income()
    program.user_expense()
    program.savefile()
    program.user_budget()
    
    print("\nYour Financial Summary:")
    summary = program.user_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    program.savefile() #sames the summary to the file
    
    print("\nBudgeting:")
    budget_comparison = program.compare_user_budget()
    for category, details in budget_comparison.items():
       print(f"{category}: {details}")
#Making sure the function will only run when the script is executed.    
if __name__ == "__main__":
    main()

        
                