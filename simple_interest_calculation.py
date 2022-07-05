#  Write a function to accept rate, principle and time to calculate,  simple_interest
# /The program should accepts three arguments and returns the simple interest accordingly  

# define a function to calcute
def simpleInterest(P, N, R):
    SI = (P * N * R)/100
    return SI

P = float(input("Enter the principal amount : "))
 
N = float(input("Enter the number of years : "))
 
R = float(input("Enter the rate of interest : "))
 
#calculating the simple interest 
SI = (simpleInterest(P, N, R))
 
print("The Simple interest is : {}".format(SI))