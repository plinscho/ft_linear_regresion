This is an exercise to understand the foundations of machine learning,
it grabs the data from "data.csv", normalizes it and calculates a linear regresion
to guess a price given a mileage.

How to use it:




This project aims to teach the fundamentals of machine learning.
Introducing concepts like linear regresion and gradient descent,
we can calculate optimal price and train a model with the data.

We need to find "funci", this will be our function:

    y = t0 + t1 * x 

This represents a straight line in a 2d plane, and adjusting 
t0 is intersection when km = 0, and t1 controls the slope.

"x" are the kilometers of the car and "y" the price for it.
There are optimal values for "t1" and "t2", and to get those values
we can't simply try. We'll start trying always get something, but the point is how i
GOOD (the error) this something is compared to reality

    cost function / error = estimated price - predicted price

We can try and give funci some values:

    km = 100000
    real price € = 5000
    t0 = 0
    t1 = 0

    y = 0 + 0 * 100000 = 0
    error = 0 - 5000 = -5000

we can try m times, let's square the error and divide by m to get average error.
This is called MSE (Mean Squared Error) and we want it as close to 0 as possible.

    MSE = sum((expected - real)^2) / m

We will use the error to adjust "funci", the slope o
And because we can't just try for infinite values, we will use the gradient
descent. This way we will get t0 and t1 faster than random.
And because we want it to be the minium possible, 
we will get the derivative of the MSE using gradient descend.

If we derive the MSE function, we obtain:

    t0' = t0 - a * (sum(expected - real), m times) / m
    t1' = t1 - a * (sum(expected - real), m times) / m * x

where "a" is the learning rate and "x" are the km.
But remeber we can also write "expected" like:
    
    expected price = t0 + t1 * x







    




