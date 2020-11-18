total_cost = 1000000
semi_annual_raise = 0.07
annual_return = 0.04
starting_salary = float(input("Enter your starting salary:   "))
portion_down_payment = total_cost * 0.25
current_savings = 0
epsilon = 100
number_of_months = 0


def three_year_savings(current_savings, guess, semi_annual_raise,
                       annual_return, starting_salary):
    for month in range(0,36):
        if (month + 1) % 6 == 0 and month != 0:
            starting_salary += semi_annual_raise * starting_salary
            current_savings += guess * starting_salary / 12 + current_savings * annual_return / 12
        else:
            current_savings += guess * starting_salary / 12 + current_savings * annual_return / 12
    return current_savings


highest_three_year = three_year_savings(0, 1, 0.07, 0.04, starting_salary)
if abs(highest_three_year - portion_down_payment) >= epsilon and highest_three_year < portion_down_payment:
    print("It is not possible to pay the down payment in three years. Your maximum savings:", highest_three_year)
else:
    low = 0
    high = 10000
    guess = int((low + high) / 2)
    guessed_savings_rate = guess / 10000
    step = 0
    savings = three_year_savings(0, guessed_savings_rate, 0.07, 0.04, starting_salary)
    while abs(savings - portion_down_payment) >= epsilon and savings < portion_down_payment:
        if savings > portion_down_payment:
            low = guess
        else:
            high = guess
        step += 1
        guess = int((high + low) / 2)
        print(guess)
        guessed_savings_rate = guess/10000
        savings = three_year_savings(0, guessed_savings_rate, 0.07, 0.04, starting_salary)
    print("Best savings rate:", guessed_rate)
    print("Steps in bisection search:", step)
