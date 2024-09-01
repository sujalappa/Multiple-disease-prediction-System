import numpy as np
class Lasso_Regression():

  def __init__(self,learning_rate,no_of_iterations,lambda_param):
    self.learning_rate = learning_rate
    self.no_of_iterations = no_of_iterations
    self.lambda_param = lambda_param

  def fit(self,X,Y):
    self.m , self.n = X.shape

    self.w = np.zeros(self.n)
    self.b = 0;
    self.X = X
    self.Y = Y
    for i in range(self.no_of_iterations):
      self.update_weights()

  def update_weights(self):
    y_prediction = self.predict(self.X)

    dw = np.zeros(self.n)

    for i in range(self.n):

      if self.w[i] > 0:
        dw[i] = (-2/self.m)*(self.X[:,i].dot(self.Y - y_prediction) + self.lambda_param)
      
      else:
        dw[i] = (-2/self.m)*(self.X[:,i].dot(self.Y - y_prediction) - self.lambda_param)

    db = -2/self.m * np.sum(self.Y - y_prediction)
    self.w = self.w - self.learning_rate *dw
    self.b = self.b - self.learning_rate *db


  def predict(self,X):

    return np.dot(X,self.w) + self.b # return X.dot(self.w) + self.b

