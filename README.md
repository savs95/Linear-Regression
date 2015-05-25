## Linear Regression as an aid in learning
### Uses a direct formula to find pseudo-inverse, and hence compute weight.
	- Creates a matrix of training data set dim(X) = (N,d+1), where d is the dimension   
	- Creates a matrix of output of target funtion on training data. dim(Y) = (N,1)   
	- computes X transpose, multiply X transpose with X, take inverse of the product and multiply it with X tranpose. Then multiply the product with Y.   
	- This gives a nice estimate for the weight as shown. Yellow line is the target function and blue line is the regression line. Generally used as a starting weight in perceptron learning algoritm.   
![My image] (100pts.png)   
	-Run as    
	```
	-$ python lin_regression.py
	```
### Uses Python 2.7 with numpy and matplotlib	

