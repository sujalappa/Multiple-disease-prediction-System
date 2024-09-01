import numpy as np


class SVM_classifier():
 #initiating the hyperparameter
  def __init__(self,learning_rate,no_of_iterations,lambda_param):
    self.learning_rate = learning_rate
    self.no_of_iterations = no_of_iterations
    self.lambda_param = lambda_param

  #fitting the data to SVM classifier
  def fit(self,X,Y):
    self.m,self.n = X.shape # m and n are rows and cols respectively
    self.w = np.zeros(self.n)
    self.b = 0
    self.X = X
    self.Y = Y

    for i in range(self.no_of_iterations):
      self.update_weights()

 # updating the weights and bias
  def update_weights(self):
    #label encoding
    y_label = np.where(self.Y <=0,-1,1)
      
      for index,x_i in enumerate(self.X):
        condition = y_label[index] * (np.dot(x_i,self.w) - self.b) >= 1

        if(condition == True):
          dw = 2*self.lambda_param*self.w
          db = 0
        else:
          dw = 2*self.lambda_param*self.w - np.dot(x_i,y_label[index])
          db = y_label[index]
        
        self.w = self.w - self.learning_rate*dw
        self.b = self.b - self.learning_rate*db
        



  # predicting the label for given input
  def predict(self,X):

    output = np.dot(X,self.w) - self.b
    predicted_label = np.sign(output)
    y_pred = np.where(predicted_label <= -1,0,predicted_label)
    return y_pred