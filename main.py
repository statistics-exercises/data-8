import numpy as np

# This bit of code just shows you how np.floor and np.ceil work
print("The floor of 2.5 is", int( np.floor(2.5)) )
print("The ceiling of 2.5 is", int( np.ceil(2.5)) )

def percentile( data, ppp ) :
  # Your code for calculating x goes here
  

# This code allows you to test whether you function is working properly
x = np.loadtxt( "data.dat")
print( "25% of the data is less than or equal to", percentile( x, 25 ) )
print( "50% of the data is less than or equal to", percentile( x, 50 ) )
print( "75% of the data is less than or equal to", percentile( x, 75 ) )
