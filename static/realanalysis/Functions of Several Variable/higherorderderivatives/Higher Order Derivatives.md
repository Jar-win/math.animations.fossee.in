## Higher Order Derivatives
### Definition
Any derivative beyond the first derivative of a function are referred to as higher order derivatives.

A partial derivative of a function of several variables is its derivative with respect to one of those variables, with the others held constant. For example $ \frac{\partial z}{\partial x}$ is the first partial derivative of the function $z=f(x,y)$ with respect to $x$

### Motivation

Moving from first order derivatives like ($\frac {dy}{dx}$ ) to higher order derivatives like $\frac {d^2y}{dx^2}$ and $\frac {d^3y}{dx^3}$ is something that most students entering the university for the first time have trouble grasping, but higher order derivatives form the foundation for concepts like acceleration, rate of inflation etc so it is essential to understand what they mean and what they represent.
The whole situation changes when we consider function of several variables as they cannot be differentiated as the functions of one variable. This gives rise to the partial derivatives, which give rise to many important results like the heat equation, societal consumption function etc.

### Bird's Eye View
Higher order derivatives are the derivatives of derivatives. What they represent is the sensitivity of the derivative function to change in input variable.
For example :
The second order derivative $\frac {d^2y}{dx^2}$ represents the sensitivity of the first derivative $\frac {dy}{dx}$ to changes in the input variable $x$. Similarly the third order derivative $\frac {d^3y}{dx^3}$ represents the sensitivity of the second order derivative $\frac {d^2y}{dx^2}$ to changes in the input variable $x$. 
Partial derivatives can be understood as the derivatives of a multivariate function that has been converted to a function with one variable by considering other variables as constants.
### But what does it mean?
The intuition behind higher order derivatives can be understood in through this example. We know that for a function $y=f(x)$ it's first order derivative $\frac {dy}{dx}$ shows how much the function changes when there is a tiny change in $x$. In  a similar fashion as $\frac {dy}{dx}$ is also a function the derivative of that i.e. the second order derivative $\frac {d^2y}{dx^2}$ shows how much the first derivative function $\frac {dy}{dx}$ changes when there is small change in the input variable $x$. This same logic can be extrapolated to other higher order derivatives.

The logic behind partial derivatives and partial derivatives of higher order is quite similar to the higher order derivative when we understand them as the derivatives of multivariate functions that have been converted to functions with one variable by considering other variables as constants. Partial derivatives of the first order shows how much the multivariate function changes when there is a tiny change in one variable when the other variables are held constant and as the first order partial derivative can also be considered as a multivariate function we can differential it partially again giving rise to partial derivatives of higher order. Partial derivatives of $(n+1)^{th}$ order show the sensitivity of the $n^{th}$ order partial derivative to the changes in different variables.

For example:
Partial derivatives of second order like $\frac {\partial^2 z}{{\partial x}{\partial y}}$ and $\frac {\partial^2 z}{\partial x^2}$ show the sensitivity of the first order partial derivative $\frac {\partial z}{\partial x}$ to changes in the variables $y$ and $x$ respectively. In this way the partial derivatives of  $n^{th}$ order show the sensitivity of partial derivatives of $(n-1)^{th}$ order.

### Graphical Representation
We know that a derivative of a function is the tangent drawn to the function at that point. In the similar way a second order derivative is a tangent drawn to to first order derivative at that point. 
As higher order derivatives are also functions they can also be plotted on the cartesian plane. Here is an example of the function $f(x) = x^3$ , it's first order derivative and  it's second order derivative. 

{Animation 1}

As we get partial derivatives from multivariate function they are usually plotted in the 3d space .As partial derivatives will also be function of several variables they can be plotted in the 3d space. Partial derivatives in the 3d space look like planes as they are calculated assuming one variable to be constant. This can be understood with an example.
This is the plot of a multivariate function $z =x^2y^2$ and it's first order partial derivatives $\frac {\partial z}{\partial x}$ at $y=1$ and  $\frac {\partial z}{\partial y}$ at $x=1$.

{Animation 2}

### Points to Ponder
* What will be the nth derivative of a nth degree polynomial?
* If first derivative is the tangent to the function at that point then what will the second derivative to the function be at that point?
* Is partially differentiating $\frac {\partial z}{\partial x}$ with respect to $y$ and partially differentiating $\frac {\partial z}{\partial y}$ with respect to $x$ the same?

### Applications
Let us look at some of the applications of the Higher order derivatives
* Higher order derivatives are extensively used in physics especially in the field of kinematics while dealing with the motion of objects.
* Higher order derivatives are also used in operations research in the maximization and minimization problems.
* Partial derivatives are used in physics in important equations like the heat equation.
* Partial derivatives are also used in quantum mechanics, economics,optimization problems etc.
### Historical Note
Isaac Newton and Gottfried Leibniz independently discovered calculus in the mid-17th century. However, each inventor claimed the other stole his work in a bitter dispute that continued until the end of their lives.
### References
* https://en.wikipedia.org/wiki/Derivative
* https://en.wikibooks.org/wiki/Calculus/Higher_Order_Derivatives
* http://tutorial.math.lamar.edu/Classes/CalcI/HigherOrderDerivatives.aspx
* https://en.wikipedia.org/wiki/Partial_derivative#Higher_order_partial_derivatives
### Further reading
* https://math.stackexchange.com/questions/2987574/how-to-see-discontinuity-of-second-derivative-from-graph-of-function
* https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivatives/
