import numpy as np
class Linear_Regression():

  def __init__(self,learning_rate,no_of_iterations):
    self.learning_rate=learning_rate
    self.no_of_iterations=no_of_iterations


  def fit(self,X,Y):
    # number of training examples & number of features
    self.m,self.n=X.shape #number of rows and columns
    # initialize weights
    self.w=np.zeros(self.n) #array of zeroes of size n i.e features
    self.b = 0
    self.X = X
    self.Y = Y

    #implementing gradient descent

    for i in range(self.no_of_iterations):
      self.update_weights()

  def update_weights(self,):
    #update weights
    Y_prediction = self.predict(self.X)


    #calculate gradients

    dw = - (2*np.sum((self.X.T).dot(self.Y - Y_prediction)))/self.m
    db = - 2*np.sum(self.Y - Y_prediction)/self.m


    #update weights
    self.w = self.w - self.learning_rate*dw
    self.b = self.b - self.learning_rate*db


  def predict(self,X):
    return X.dot(self.w) + self.b