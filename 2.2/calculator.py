"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
# Coffee Budget and Savings Calculator

# Step 1: Get user input
cups_per_day = int(input("How many cups of coffee do you drink per day? "))
cost_per_cup = float(input("How much does one cup of coffee cost at a cafe (in dollars)? "))

# Step 2: Set homemade coffee cost
homemade_cost_per_cup = 0.50  # average cost of homemade coffee

# Step 3: Calculate cafe coffee costs
daily_cafe = cups_per_day * cost_per_cup
monthly_cafe = daily_cafe * 30
yearly_cafe = daily_cafe * 365

# Step 4: Calculate homemade coffee costs
daily_home = cups_per_day * homemade_cost_per_cup
monthly_home = daily_home * 30
yearly_home = daily_home * 365

# Step 5: Calculate savings
monthly_savings = monthly_cafe - monthly_home
yearly_savings = yearly_cafe - yearly_home

# Step 6: Show the results
print("\n--- Coffee Budget and Savings Summary ---")
print("Cafe Coffee Daily: ${:.2f}".format(daily_cafe))
print("Cafe Coffee Monthly: ${:.2f}".format(monthly_cafe))
print("Cafe Coffee Yearly: ${:.2f}".format(yearly_cafe))

print("\nHomemade Coffee Daily: ${:.2f}".format(daily_home))
print("Homemade Coffee Monthly: ${:.2f}".format(monthly_home))
print("Homemade Coffee Yearly: ${:.2f}".format(yearly_home))

print("\nPotential Monthly Savings: ${:.2f}".format(monthly_savings))
print("Potential Yearly Savings: ${:.2f}".format(yearly_savings))

print("\nConsider whether switching to homemade coffee could help your budget.")