# Basic Interactive Machine Learning Terminal Program
Applies a couple different machine learning model algorithms to the [Iris dataset](https://archive.ics.uci.edu/dataset/53/iris) with ML logic from [here](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/).

This is my first exposure to ML and libraries such as pandas, scipy, numpy, matplotlib, and sklearn. The tutorial I followed provied most of the code, but I wanted an easier way
to trigger the different segments of code. Printed information is also better labeled though could be better explained.

### Used Algos
- Logistic Regression
- Linear Discriminant Analysis
- K-Nearest Neighbors
- Classification And Regression Tree
- Gaussian Naive Bayes
- Support Vector Machine

### Available Commands
- shape - number of rows and cols of dataset
- head ur_num_here - get the first inputted # of data entries 
- desc - summary of data
- dist - amount of each class in data
- plot - displays box and whisker plots
- histogram - displays histograms of the data
- matrix - displays scatter plot of the data
- eval - runs algos and prints accuracy stats
- compare - displays data from eval in a box plot.*
- predict algo_name_here - accuracy of the algorithm\'s data prediction*
- algo - prints each available ml algorithm
- help - this command
- exit - stop script

*requires eval command to have been used first
