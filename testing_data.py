import os
import pdb

import file_operation as fo
import feature_extractor as fe

def create_testing_data(test_folder):
    files = fo.list_all_files(test_folder)
    print files
    test = []
    test_label = []
    class_label = ["C2", "C2", "IKEA_IT", "IKEA_IT", "IKEA_EN", "IKEA_EN"]


    for index, file in enumerate(files):
        temp = read_testing_data(os.path.join(test_folder, file), class_label[index])
        test += temp
        test_label += [class_label[index] for i in range(len(temp))]

    return test, test_label

def read_testing_data(file_path, label):
    test = []
    with open(file_path) as f:
        for line in f:
            elements = line.strip().split('\t')
            feature = fe.get_feature(elements[4])
            test.append((feature, label))

    return test

