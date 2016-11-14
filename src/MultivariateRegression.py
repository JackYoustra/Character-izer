'''
Created on Nov 4, 2016

@author: jack
'''
import math

class TrainingVector:
    def __init__(self, inputs, output):
        self.inputs = inputs #input values (list)
        self.output = output #output value

class MultivariateRegression(object):
    '''
    Creates a multivariate regression where classification queries can be performed
    '''
    LEARNING_CONSTANT = 0.000001

    def __init__(self, trainingvectors, defweight=None):
        if defweight != None:
            self.weights = defweight
            return
        '''
        Follow equation 18.4 to get regression working
        '''
        'add the first dummy x identity variable for w0'
        for vector in trainingvectors:
            vector.inputs = [1] + vector.inputs
        self.weights = [0.5]*(len(trainingvectors[0].inputs))
        before = []
        while not MultivariateRegression.__converge(before, self.weights):
            before = self.weights[:]
            for example in trainingvectors:
                for index in range(len(self.weights)):
                    weight = self.weights[index]
                    prediction = self.predict(example.inputs)
                    #logistic
                    self.weights[index] = weight + MultivariateRegression.LEARNING_CONSTANT * (example.output - prediction) * prediction * (1-prediction) * example.inputs[index]
                    #linear
                    #self.weights[index] = weight + MultivariateRegression.LEARNING_CONSTANT*(example.output - prediction)*example.inputs[index]
    def predict(self, xvals):
        'add zero offset'
        total = 0.0
        assert len(xvals) == len(self.weights)
        for index in range(len(self.weights)):
            total += self.weights[index] * xvals[index]
        return total / (len(self.weights)*255)
    
    @staticmethod
    def __converge(before, after):
        if before == []:
            return False
        difference = 0.0
        for first in before:
            for other in after:
                difference += first - other
        if difference > 0.05:
            return False
        return True
    
    def __str__(self):
        retVal = "Weights: "
        for coefficient in self.weights:
            retVal += str(coefficient) + " "
        return retVal
            