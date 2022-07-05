#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. 
# /Ask the user for their salary and year of service and print the net bonus amount. /
# Write a python code to implement this scenario. 

year_of_service = int(input("type in your years of service"))
basic_salary = int(input("type in your basic salary")) 
net_bonus =((basic_salary*5)/100)

def bonus(year_of_service,basic_salary,net_bonus):
    if year_of_service>= 5 and basic_salary:
        return net_bonus

print (f"your net bonus is: {net_bonus}")






