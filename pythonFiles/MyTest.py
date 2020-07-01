import unittest
import numpy as np
from .mainFunctions import create_new_dataframe, find_files, parse_data
import pandas as pd

def add(x):
    return x + 1

class MyTest(unittest.TestCase):

    # user editable vars
    projectRoot = "/Users/deepak/Documents/PythonFiles/data/empty_proj"
    extensionsToSearch = ['.nii.gz', '.json', '.gii']
    labelsToParse = ['sub', 'ses', 'task', 'run']
    outputFileName = "scanResults"
    outputDirectory = "/Users/deepak/Documents/PythonFiles/data/outputFiles"


    def test_NewDataFrame_isDataFrame(self):
        dfObj = create_new_dataframe(self.labelsToParse)
        self.assertIsInstance(dfObj, pd.DataFrame)

    def test_NewDataFrame_hasAllLabels(self):
        dfObj = create_new_dataframe(self.labelsToParse)
        contains = True
        for label in self.labelsToParse:
            if not label in dfObj.columns:
                contains = False

    def test_NewDataFrame_isEmpty(self):
        dfObj = create_new_dataframe(self.labelsToParse)
        self.assertTrue(dfObj.empty)
