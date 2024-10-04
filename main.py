from package_test import test
from ml import *

def input_commands(input):
    

def main():
    # Ensure libraries are installed from requirements.txt
    test()
    
if __name__ == '__main__':
    main()
    print('Welcome to an interactive experience of machine learning\'s version of \'hello world\'',
          'This program will be getting its data from the 1936 Iris dataset, and logic from a tutorial',
          'Found here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/')
    
    while True:
        text = input("Enter your command: ")
        input_commands(text)