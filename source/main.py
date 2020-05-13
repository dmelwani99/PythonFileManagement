import glob, os
import numpy as np
import pandas as pd

def addToDataFrame(file, dataframe):
        dataframe

# user editable vars
projectRoot = "/Users/deepak/Documents/PythonFiles/data/empty_proj"
labelsToParse = ['sub', 'ses', 'task', 'run']
outputFileName = "scanResults"
outputDirectory = "/Users/deepak/Documents/PythonFiles/data/outputFiles"

# create a DataFrame object w/ column labels
dfObj = pd.DataFrame(columns=['file', 'parent', 'child'] + labelsToParse + ['otherData'])

print('Beginning search in ' + projectRoot)

print('Processing .nii.gz Files now')

niigzFiles = glob.glob(projectRoot + '/**/*.nii.gz', recursive=True)
for name in niigzFiles:
    dfObj.at[(name.replace(projectRoot, ".")), 'file'] = os.path.basename(name)

print('Processing .json Files now')

jsonFiles = glob.glob(projectRoot + '/**/*.json', recursive=True)
for name in jsonFiles:
    dfObj.at[(name.replace(projectRoot, ".")), 'file'] = os.path.basename(name)

print('Processing .gii Files now')

giiFiles = glob.glob(projectRoot + '/**/*.gii', recursive=True)
for name in giiFiles:
    dfObj.at[(name.replace(projectRoot, ".")), 'file'] = os.path.basename(name)

dfObj.drop_duplicates(inplace=True)

print('Finding labels now')
# iterate through DataFrame rows
for index, row in dfObj.iterrows():

    fileName, file_extension = os.path.splitext(os.path.basename(index))
    #split file name into labels separated by '_'
    labels = fileName.split('_')

    for label in labels:
        if '-' in label:
            info = label.split('-')
            if info[0] in labelsToParse:
                dfObj.at[index, info[0]] = info[1]
            else:
                existingOtherData = dfObj.at[index, 'otherData']
                dfObj.at[index, 'otherData'] = (str(existingOtherData) + 'label: "{}", value: "{}"; '.format(info[0], info[1]))

    if file_extension == '.json': #and find if there is a matching .nii.gz
        print(fileName) #then get its index and set the otherdata relation

# export as CSV file
dfObj.to_csv(outputDirectory + outputFileName + '.csv')

print('Scan Complete. Exported to ' + projectRoot + '/' + outputFileName)