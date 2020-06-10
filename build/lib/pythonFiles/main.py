import glob, os
import numpy as np
import pandas as pd

# user editable vars
projectRoot = "/Users/deepak/Documents/PythonFiles/data/empty_proj"
extensionsToSearch = ['.nii.gz', '.json', '.gii']
labelsToParse = ['sub', 'ses', 'task', 'run']
outputFileName = "scanResults"
outputDirectory = "/Users/deepak/Documents/PythonFiles/data/outputFiles"

# create a DataFrame object w/ column labels
dfObj = pd.DataFrame(columns=['file', 'parent', 'child'] + labelsToParse + ['otherData'])

print('Beginning search in ' + projectRoot)

for extension in extensionsToSearch:
    print('Searching for ' + extension + ' files now')
    files = glob.glob(projectRoot + '/**/*' + extension, recursive=True)
    for name in files:
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
                existingOtherData = dfObj.at[index, 'otherData'] #todo: condensed-if to check that an empty otherData = nan
                dfObj.at[index, 'otherData'] = (str(existingOtherData) + 'label: "{}", value: "{}"; '.format(info[0], info[1]))


# export as CSV file
dfObj.to_csv(outputDirectory + outputFileName + '.csv')

print('Scan Complete. Exported to ' + projectRoot + '/' + outputFileName)