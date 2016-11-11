'''
Created on Nov 7, 2016

@author: jack
'''

from string import ascii_lowercase
from Loader import load, imageToWeights
import MultivariateRegression
import copy
from PIL import Image
from Loader import imageToWeights
from sklearn import linear_model

# return map of training vectors -> letter
def createTrainingVectors(letters):
    trainingVectors = {} # one list of vectors per letter
    for letter, images in letters.items(): #initialize list
        trainingVectors[letter] = []
        
    for letter, images in letters.items():
        for image in images:
            for currentLetter in ascii_lowercase:
                weights = imageToWeights(image)
                output = 0.0
                if letter == currentLetter:
                    output = 1.0
                currentvector = MultivariateRegression.TrainingVector(weights, output)           
                trainingVectors[currentLetter].append(copy.deepcopy(currentvector))
    return trainingVectors

if __name__ == '__main__':
    
    letters = load()
  
    trainers = createTrainingVectors(letters)
    #let's try 'A'
    a = trainers['a']
    weights = []
    values = []
    for listItem in a:
        weights.append(listItem.inputs)
        values.append(listItem.output)
    
    #cool = linear_model.LogisticRegression()
    #cool.fit(weights, values)
    
    
    #regression = MultivariateRegression.MultivariateRegression(None, defweight=[0.4980739007472371,0.034294627828366626,0.08527965194087288,0.1611870785960047,0.20510706494725237,0.1647477728264825,0.0992302295864054,0.04132866244579191,0.03296886126530924,0.07010771926676687,0.10676335664100603,0.11058294826171326,0.09605828600570894,0.07552970677772958,0.03219182081913526,0.02124397446868094,0.03749483934979752,0.055892351803555826,0.058883158424758206,0.04569714919406262,0.029699170400632097,0.020281550749062675,0.012887985299360796,0.017883024180103586,0.023729694350087253,0.024766788815806413,0.02029564278452003,0.014526331358683814,0.0109255050331542,0.009790039260313185,0.011786566800573337,0.014167221227157203,0.013808719001855726,0.011920327630028092,0.011314754849456685,0.009319095256870028])
    regression = MultivariateRegression.MultivariateRegression(a)
    #print(str(cool.coef_))
    print(regression)
    im = Image.open("sample.jpg")
    weights = [1] + imageToWeights(im)
    print(regression.predict(weights))
    im = Image.open("letter-v.jpg")
    weights = [1] + imageToWeights(im)
    print(regression.predict(weights))
    
    
    
    
    
    
    
    
    
        