import glob, os
import numpy as np
import pandas as pd

# user editable vars
projectRoot = "/Users/deepak/Downloads/empty_proj/"
outputFileName = "scanResults"
outputDirectory = "/Users/deepak/Downloads/empty_proj/"

# strutcture data used to start DataFrame w/ a single blank data row
data = [('', '', '', '', '')]

# create a DataFrame object w/ column labels
dfObj = pd.DataFrame(data, columns=['file', 'path', 'parent', 'child', 'otherFiles'])

print('Beginning search in ' + projectRoot)

# go through each file in every directory/subdir in the project
for path, subdirs, files in os.walk(projectRoot):
    for name in files:
        # add each file + path to the dataframe
        dfObj = dfObj.append({'file': name, 'path' : os.path.join(path, name).replace(projectRoot, "")}, ignore_index=True)

    print('Added ' + str(len(files)) + ' first-level files from ' + path)

    # debug break to speed up testing by cutting run time down
    if len(files) == 1692:
        break

# iterate through DataFrame rows
for index, row in dfObj.iterrows():
    # do some logic to assign parents, children, and more
    print(row['file'], row['path']) # for now just printing rows

# remove the first blank row used for structure
dfObj = dfObj.drop(dfObj.index[0])

# export as CSV file
dfObj.to_csv(outputDirectory + outputFileName + '.csv', index = False)

print('Scan Complete. Exported to ' + projectRoot + 'FileName.csv')