import glob, os
import numpy as np
import pandas as pd


#create a DataFrame object w/ column labels
def create_new_dataframe(withlabels):
    return pd.DataFrame(columns=['file', 'parent', 'child'] + withlabels + ['otherData'])


def find_files(with_extensions, in_directory, to_dataframe):
    for extension in with_extensions:
        print('Searching for ' + extension + ' files now')
        files = glob.glob(in_directory + '/**/*' + extension, recursive=True)
        for name in files:
            to_dataframe.at[(name.replace(in_directory, ".")), 'file'] = os.path.basename(name)


def parse_data(oflabels, in_dataframe):
    print('Finding labels now')
    # iterate through DataFrame rows
    for index, row in in_dataframe.iterrows():

        fileName, file_extension = os.path.splitext(os.path.basename(index))
        # split file name into labels separated by '_'
        labels = fileName.split('_')

        for label in labels:
            if '-' in label:
                info = label.split('-')
                if info[0] in oflabels:
                    in_dataframe.at[index, info[0]] = info[1]
                else:
                    existingOtherData = in_dataframe.at[
                        index, 'otherData']  # todo: condensed-if to check that an empty otherData = nan
                    in_dataframe.at[index, 'otherData'] = (
                            str(existingOtherData) + 'label: "{}", value: "{}"; '.format(info[0], info[1]))

#dfObj.drop_duplicates(inplace=True)




# export as CSV file
#dfObj.to_csv(outputDirectory + outputFileName + '.csv')

#print('Scan Complete. Exported to ' + projectRoot + '/' + outputFileName)
