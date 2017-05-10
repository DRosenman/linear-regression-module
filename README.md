
# Linear Regression Module 

For a user-guide of the module, click [here](http://http://daverosenman.com/linear-regression-user-guide.html)


**lr.summary_stats(x, y, through_origin=False)** 

>**parameters**: x,y, (optional) through_origin <br>
x and y must be two sets of measurements of equal length. To force the regression line to through through the origin, include the third parameter as through_origin = True.

>**returns:**  
    
    >>**slope** of regression line 
    
    >>**intercept** of regression line
    
    >>**standard error of slope** of regression line
    
    >>**standard error of intercept** of regression line
    
    >>**correlation coefficient (a.k.a. r)** 


**lr.print_summary_stats(x, y, through_origin=False)**

>**parameters**: x,y, (optional) through_origin <br>
x and y must be two sets of measurements of equal length. To force the regression line to through through the origin, include the third parameter as through_origin = True.

>**prints:** 
  >>**slope** of regression line 
    
    >>**intercept** of regression line
    
    >>**standard error of slope** of regression line
    
    >>**standard error of intercept** of regression line
    
    >>**correlation coefficient (a.k.a. r)** 


### Individual Linear Regression Coefficients
**lr.slope(x, y, through_origin=False)**

>**parameters**: x,y, (optional) through_origin <br>
x and y must be two sets of measurements of equal length. For the slope of the best fit line through the origin, include the third parameter as through_origin = True.

>**returns:** the best fit slope

**lr.slope_error(x, y, through_origin=False)**

>**parameters**: x,y, (optional) through_origin <br>
x and y must be two sets of measurements of equal length. For the standard error of the slope of the best fit line through the origin, include the third parameter as through_origin = True.

>**returns:** The standard error of the slope.

**lr.intercept(x,y)**
>**parameters**: x,y <br>
x and y must be two sets of measurements of equal length.

>**returns:** The intercept of the best fit line

**lr.intercept_error(x,y)**
>**parameters**: x,y, (optional) through_origin <br>
x and y must be two sets of measurements of equal length.

>**returns:** The standard error of the intercept

**lr.r(x,y)**
>**parameters**: x,y <br>
x and y must be two sets of measurements of equal length.

>**returns:** The correlation coefficient, a.k.a. r

**lr.r_squared(x,y):**
>**parameters**: x,y <br>
x and y must be two sets of measurements of equal length.

>**returns:** The coefficient of determination, a.k.a. $r^2$

**lr.p_value(x,y,through_origin=False)**

>**parameters**: x,y, (optional) through_origin<br>
x and y must be two sets of measurements of equal length. For the p-value when the best fit line in forced to inercept the origin, include the third parameter as through_origin = True.

>**returns:** Two sided p-value for the t-test with the null hypothesis that the slope is zero.
