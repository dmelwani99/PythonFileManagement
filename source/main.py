import glob, os
import numpy as np
import pandas as pd

def addToDataFrame(file, dataframe):
        return dataframe.append({'file': os.path.basename(file), 'path' : file.replace(projectRoot, "")}, ignore_index=True)

# user editable vars
projectRoot = "/Users/deepak/Documents/PythonFiles/data/empty_proj"
outputFileName = "scanResults"
outputDirectory = "/Users/deepak/Documents/PythonFiles/data/outputFiles"

# strutcture data used to start DataFrame w/ a single blank data row
data = [('', '', '', '', '', '', '', '', '')]

# create a DataFrame object w/ column labels
dfObj = pd.DataFrame(data, columns=['file', 'path', 'parent', 'child', 'sub', 'ses', 'task', 'run', 'otherFiles'], index=['file'])

print('Beginning search in ' + projectRoot)

#print('Processing .nii.gz Files now')

#niigzFiles = glob.glob(projectRoot + '/**/*.nii.gz', recursive=True)
#for name in niigzFiles:
#    dfObj = addToDataFrame(name, dfObj)

#print('Processing .json Files now')
#
#jsonFiles = glob.glob(projectRoot + '/**/*.json', recursive=True)
#for name in jsonFiles:
#    dfObj = addToDataFrame(name, dfObj)

print('Processing .gii Files now')

giiFiles = glob.glob(projectRoot + '/**/*.gii', recursive=True)
for name in giiFiles:
    dfObj = addToDataFrame(name, dfObj)

dfObj.drop_duplicates(inplace=True)
# iterate through DataFrame rows
for index, row in dfObj.iterrows():

    fileName = row['file']
    #split file name into labels separated by '_'
    labels = fileName.split('_')

    for label in labels:
        if '-' in label:
            info = label.split('-')
            if info[0] == 'sub' or info[0] == 'ses' or info[0] == 'task' or info[0] == 'run':
                dfObj.at[fileName, info[0]] = info[1]
            else:
                existingOtherFiles = dfObj.at[fileName, 'otherFiles']
                dfObj.at[fileName, 'otherFiles'] = (str(existingOtherFiles) + '("label": "{}", "value": "{}")'.format(info[0], info[1]))

# remove the first blank row used for structure
dfObj = dfObj.drop(dfObj.index[0])

# export as CSV file
dfObj.to_csv(outputDirectory + outputFileName + '.csv', index = False)

print('Scan Complete. Exported to ' + projectRoot + '/' + outputFileName)