import sys
import ml
from package_test import test

MODELS = [
    '\'LR\' - Logistic Regression',
    '\'LDA\' - Linear Discriminant Analysis',
    '\'KNN\' - K-Nearest Neighbors',
    '\'CART\' - Classification And Regression Tree',
    '\'NB\' - Gaussian Naive Bayes',
    '\'SVM\' - Support Vector Machine'
]

COMMANDS = [
    'shape - number of rows and cols of dataset ',
    'head ur_num_here - get the first inputted # of data entries ',
    'desc - summary of data',
    'dist - amount of each class in data',
    'plot - displays box and whisker plots',
    'histogram - displays histograms of the data',
    'matrix - displays scatter plot of the data',
    'eval - runs algos and prints accuracy stats',
    'compare - displays data from eval in a box plot.*',
    'predict algo_name_here - accuracy of the algorithm\'s data prediction*',
    'algo - prints each available ml algorithm',
    'help - this command',
    'exit - stop script',
    '*requires eval command to have been used first'
]

def input_commands(input):
    input = str(input).split()
    input[0].lower()
    if(input[0] == 'shape'):
        ml.print_shape()
    elif(input[0] == 'head' and len(input) == 2):
        ml.print_head(int(input[1]))
    elif(input[0] == 'desc'):
        ml.print_desc()
    elif(input[0] == 'dist'):
        ml.print_dist()
    elif(input[0] == 'plot'):
        ml.show_plot()  
    elif(input[0] == 'histogram'):
        ml.show_histogram()  
    elif(input[0] == 'matrix'):
        ml.show_matrix()
    elif(input[0] == 'eval'):
        ml.evaluate_models()
        ml.ran_algos = True   
    elif(input[0] == 'compare' and ml.ran_algos):
        ml.show_algorithm_comparison()  
    elif(input[0] == 'predict' and len(input) == 2 and input[1] in MODELS and ml.ran_algos):
        ml.predict_model(input[1])
    elif(input[0] == 'exit'):
       sys.exit()
    elif(input[0] == 'help'):
       for s in COMMANDS:
           print(s)
    elif(input[0] == 'algo'):
       for s in MODELS:
           print(s)
    else:
        print("Invalid input")       

def main():
    # Ensure libraries are installed from requirements.txt
    print('\nChecking imports...\n')
    test()
    
    print('\nWelcome to an interactive experience of machine learning\'s version of \'hello world\'',
          'This program will be getting its data from the 1936 Iris dataset, and logic from a tutorial',
          'found here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/',
          '\nEnter \'help\' to get list of commands')
    
    while True:
        text = input("Enter your command: ")
        if(input):
            input_commands(text)
    
if __name__ == '__main__':
    main()
    