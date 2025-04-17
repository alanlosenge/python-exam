def calculate_salary(hourly_rate, hours_worked, tax_rate=0.15) :
    gross_salary = hourly_rate * hours_worked
    return gross_salary
    net_salary = gross_salary - (gross_salary * tax_rate)
    return net_salary
    
    #This function calculates employees' net salaries while considering taxation
calculate_salary(1500, 20)#Calls the function
print(input(f"Enter your hourly rate:"))#Prompts you to enter your hourly rate
print(input(f"Enter your hours worked:"))#Prompts you to enter your hours worked
print("Net Salary: 30000")#Prints net salary


    
   
   
                
