# Basic Interactive Machine Learning Terminal Program
Applies a couple different machine learning model algorithms to the [Iris dataset](https://archive.ics.uci.edu/dataset/53/iris) with ML logic from [here](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/).

This is my first exposure to ML and libraries such as pandas, scipy, numpy, matplotlib, and sklearn. The tutorial I followed provied most of the code, but I wanted an easier way
to trigger the different segments of code. Printed information is also better labeled though could be better explained.

## Instructions
1. Before getting started, be sure to have [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) installed

2. Open up a terminal and change directory to a new, empty folder.

3. Clone this repository 

    `git clone https://github.com/sharktrexer/first_ml_project`

4. Install the required packages

    `pip install -r requirements.txt`

5. Use this command to start the program:
   
    `python main.py`

## Info
Listed below are some machine learning algorithms used in this program and the different commands you can enter and what they do.

### Used Algos
- Logistic Regression
- Linear Discriminant Analysis
- K-Nearest Neighbors
- Classification And Regression Tree
- Gaussian Naive Bayes
- Support Vector Machine

### Available Commands
- shape - number of rows and cols of dataset
- head [ur_num_here] - get the first inputted # of data entries 
- desc - summary of data
- dist - amount of each class in data
- plot - displays box and whisker plots
- histogram - displays histograms of the data
- matrix - displays scatter plot of the data
- eval - runs algos and prints accuracy stats
- compare - displays data from eval in a box plot.*
- predict [algo_name_here] - accuracy of the inputted algorithm's data prediction*
- algo - prints each available ml algorithm
- help - prints this list
- exit - stop script

*requires eval command to have been used first
