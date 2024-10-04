'''Tutorial from
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/'''

# Used libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# Data printing

# shape
def print_shape():
    print(dataset.shape)
    print('\n')

# head
def print_head():
    print(dataset.head(20))
    print('\n')

# descriptions
def print_desc():
    print(dataset.describe())
    print('\n')

# class distribution
def print_dist():
    print(dataset.groupby('class').size())
    print('\n')

#Visualizations
# box and whisker plots
def show_plot():
    dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    plt.show()

# histograms
def show_histogram():
    dataset.hist()
    plt.show()

# scatter plot matrix
def show_matrix():
    scatter_matrix(dataset)
    plt.show()


# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)


# Spot Check Algorithms
models = []
models.append(('LR', OneVsRestClassifier(LogisticRegression(solver='liblinear'))))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
ran_algos = False
# evaluate each model in turn
results = []
names = []
def evaluate_models():
    print('name  mean   standard deviation')
    for name, model in models:
        kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
        cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
        results.append(cv_results)
        names.append(name)
        print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
     
 
 # Compare Algorithms
def show_algorithm_comparison():
    plt.boxplot(results, tick_labels=names)
    plt.title('Algorithm Comparison')
    plt.show()

# Make predictions on validation dataset
def predict_model(model_name):
    for name, model in models:
        if (model_name != name): 
            continue
        
        model.fit(X_train, Y_train)
        predictions = model.predict(X_validation)

        # Evaluate predictions
        print(name)
        print('Accuracy: %', accuracy_score(Y_validation, predictions))
        print('Confusion Matrix\n')
        print(confusion_matrix(Y_validation, predictions))
        print('Report:\n')
        print(classification_report(Y_validation, predictions))