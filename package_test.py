# Check the versions of libraries
def test():
    try:
        # Python
        import sys
        print('Python: {}'.format(sys.version))
        # scipy
        import scipy
        print('scipy: {}'.format(scipy.__version__))
        # numpy
        import numpy
        print('numpy: {}'.format(numpy.__version__))
        # matplotlib
        import matplotlib
        print('matplotlib: {}'.format(matplotlib.__version__))
        # pandas
        import pandas
        print('pandas: {}'.format(pandas.__version__))
        # scikit-learn
        import sklearn
        print('sklearn: {}'.format(sklearn.__version__))
    except:
        raise Exception("One or more libraries are not installed. Aborted")