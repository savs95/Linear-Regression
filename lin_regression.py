'''
Created on May 25, 2015

@author: savs95
'''
import numpy as np
import target

def compute_y (lst):
    y_soln = []
    for i in lst :
        y_soln.append(np.sign(target.TF.dot(i)))
    return y_soln    

x = np.matrix(target.lst)
x_trans = x.T
yT=[]
yT = compute_y(target.lst)
numpyT=np.matrix(yT)
y=numpyT.T
pseudo_inv = ((x_trans*x).I)*x_trans
lin_reg_weight = pseudo_inv*y
weight = np.array(lin_reg_weight.T)

k = np.linspace(-1,1)
target.plt.plot(k, (-weight[0][1]/weight[0][2])*k+(-weight[0][0]/weight[0][2]), 'b-')
target.plt.show() 
