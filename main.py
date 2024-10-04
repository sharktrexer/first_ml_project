import sys
import ml
from package_test import test

MODELS = [
    'LR',
    'LDA',
    'KNN',
    'CART',
    'NB',
    'SVM'
]

def input_commands(input):
    input = str(input).split()
    input[0].lower()
    if(input[0] == 'shape'):
        ml.print_shape()
    elif(input[0] == 'head'):
        ml.print_head()
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
    elif(input[0] == 'predict' and input[1] in MODELS and ml.ran_algos):
        ml.predict_model(input[1])
    elif(input[0] == 'exit'):
       sys.exit()
    else:
        print("Invalid input")       

def main():
    # Ensure libraries are installed from requirements.txt
    test()
    
    print('Welcome to an interactive experience of machine learning\'s version of \'hello world\'',
          'This program will be getting its data from the 1936 Iris dataset, and logic from a tutorial',
          'found here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/')
    
    while True:
        text = input("Enter your command: ")
        if(input):
            input_commands(text)
    
if __name__ == '__main__':
    main()
    