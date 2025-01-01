# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE(

from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    saving_balance=float(input("What is your initial saving account balance?: $"))
    interest_rate=float(input("What is the APR for the Saving Account?: "))
    saving_maturity=int(input("What is the length of months for your Saving Account?: "))
   
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned=create_savings_account(saving_balance,interest_rate,saving_maturity)


    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the savings account:')
    print(f"You earned: ${interest_earned} over {saving_maturity} months in your Saving Account.")
    print("_"*50)
    print(f"Your final saving account balance: ${updated_savings_balance}")
    

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    cd_balance=float(input("What is your initial CD account balance?: $"))
    cd_interest=float(input("What is the APR for the CD Account?: "))
    cd_maturity=int(input("What is the length of months for your CD Account?: "))
    

    # Call the create_cd_account function and pass the variables from the user.
    updated_savings_balance, interest_earned=create_cd_account(cd_balance,cd_interest,cd_maturity)

    # # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # # ADD YOUR CODE HERE
    print('Here are the details of the CD account:')
    print(f"You earned : ${interest_earned} over {cd_maturity} months in your CD Account.")
    print("_"*50)
    print(f"Your final CD account balance: ${updated_savings_balance}")
    

if __name__ == "__main__":
   main()
    # Call the main function.