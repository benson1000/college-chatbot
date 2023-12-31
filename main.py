#import libraries we are use
import nltk #natural language toolkit for human language interaction

nltk.download('punkt')   # Download required data

from nltk.stem.lancaster import LancasterStemmer  #This tokenizer divides a text into a list of sentences 
stemmer = LancasterStemmer()                     

import numpy as np   # this is for multi-dimensional array and matrices                                  
import pandas as pd  #this is used for data manipulation,  data analysis, and  data cleaning


from preprocessing import data_preprocessing      #import data_preprocessing function from data_preprocessing.py
training, output,labels, words, data = data_preprocessing(stemmer)


    
###### This section is for spliiting the dataset for training and testing purposes.      

from sklearn.model_selection import train_test_split #for spliting dataset into training and testing sets

X_train, X_test, y_train,y_test = train_test_split(training, output, test_size=0.25, random_state=42) #training 75% , testing 25%

# print(X_train.shape,y_train.shape)
# print(X_test.shape,y_test.shape)

from init_model import init_model                      #import init_model function from init_model.py
model = init_model(X_train,y_train,X_test,y_test)      #call function init_model that create model in it 




#####
######### data pre processing module
#The bag_of_words function will transform our string input to a bag of words using our created words list.
def bag_of_words(s, words):                #s:sentence
    bag = [0 for _ in range(len(words))]    #bag with intial value 0

    s_words = nltk.word_tokenize(s)         #tokonize sentence
    s_words = [stemmer.stem(word.lower()) for word in s_words] #stemming words

    for se in s_words:                     #loop for check if wordes already exists or not 
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1                #but 1 if the word already exists
            
    return np.array(bag)               #convert bag to numpy array

            
#### main file   
from chat import  chat                           #import the function that called chat from chat.py
chat(model,bag_of_words,labels,words,data)      #call chat function
