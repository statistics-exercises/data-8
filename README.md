# Inverting the cumulative distribution

Congratulations on completing the last exercise!  To summarise the last exercise showed that if we have the following ordered data set:

````
data = [ 0.1, 0.3, 0.4, 0.5, 0.6, 0.9 ]
````

Then we have the following information on the cumulative probability distribution function:

![](https://render.githubusercontent.com/render/math?math=P(X<0.1)=0\quad\P(X\le\0.3)=\frac{1}{5}\quad\P(X\le\0.4)=\frac{2}{5}\quad\P(X\le\0.5)=\frac{2}{5}\quad\P(X\le\0.6)=\frac{4}{5}\quad\P(X\le\0.9)=1)

In other words, if we return to the statement that we want to write:

````
z % of the data points are less than or equal to x.
````

sorting the data thus allows us to determine the x values that correspond to particular values of z.  We cannot, however, determine the x value that corresponds to any value of z.  We can only determine the x values for the six values of z given above.  

Probability theory provides us with many tools for resolving this problem, which we will learn about during this course.  To use __ALL__ of these tools, however, we need to make assumptions about the process that generates the data.  From this point onwards we thus need to remember that we are never simply viewing the data we collect from experiments.  We are instead using a model to understand the data.

With that in mind, let's introduce a model for the cumulative probability distribution for data.  We are going to suppose that the cumulative distribution function is linear in between each pair of the values of at which we know it based on the sorted data.  Let's now suppose that are asked to calculate the value of x that z % of the data are less or equal to.  If we have N data points we do the following operation:

![](https://render.githubusercontent.com/render/math?math=j=\frac{(N-1)z}{100})

to get a number between 0 and N-1.  This number is likely to be a decimal.  We can convert it to an integer in python, however, in two different ways:

````
f = int( np.floor( (N-1)*z / 100 ) )
c = int( np.ceil( (N-1)*z / 100 ) )
````

The example code on the panel left demonstrates what these two commands do.  As you can see, the first command rounds the real number down to the nearest integer, while the second command rounds the real number up to the nearest integer.  As such if we do:

```
a1 = int( np.floor(3) ) 
a2 = int( np.ceil(3) )
```

Then the variables `a1` and `a2` are both set equal to 3.

We can use the `np.floor` and `np.ceil` commands to get closer to the solution of this problem of computing the value of x that z% of the data are less or equal to.  Considering the values in example array called data that was given above helps us to see how.  Let's suppose that we want to calculate the value of x that 25% of the data is less than.  There are 6 values in data so:

````
j = 5 * 25 / 100 = 5/4
````

The floor and ceiling of `j` are thus f = 1 and c = 2.  As long as `data` has been sorted we can thus write that x takes some value between ![](https://render.githubusercontent.com/render/math?math=d_l)=`data[1]` and ![](https://render.githubusercontent.com/render/math?math=d_c)=`data[2]`.  We can then  get the final value of `x` here by assuming these two points where we know the function are connected by a straight line and thus writing:

![](https://render.githubusercontent.com/render/math?math=x=d_l%2B(d_c-d_l)\left(\frac{(N-1)z}{100}-l\right))

which is just the equation for a straight line passing through ![](https://render.githubusercontent.com/render/math?math=(l,d_l)) and ![](https://render.githubusercontent.com/render/math?math=(c,d_c)).    

__To complete this exercise you will need to use these ideas to complete the function called `percentile`__.  This function takes two arguments:

1. `data` - a data set that is not ordered.
2. `ppp` - the percentile that needs to be calculated.

The function should return the value of x that `ppp`% of the data is less than.  x should be calculated using the formula given above.
