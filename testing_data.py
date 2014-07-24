import os
import pdb

import file_operation as fo
import feature_extractor as fe

def create_testing_data(test_folder):
    files = fo.list_all_files(test_folder)
    print files
    test = []
    for file in files:
        test += read_testing_data(os.path.join(test_folder, file))

    return test

def read_testing_data(file_path):
    test = []
    with open(file_path) as f:
        for line in f:
            elements = line.strip().split('\t')
            feature = fe.get_feature(elements[4])
            test.append(
                (feature)
            )

    return test

