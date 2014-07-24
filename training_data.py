import file_operation as fo
import os
import pdb

import feature_extractor as fe

def create_training_data(train_folder):
    train = []

    question_files = fo.list_all_files(os.path.join(train_folder, 'question'))
    for file in question_files:
        train += read_training_data(os.path.join(train_folder, 'question', file), True)

    answer_files = fo.list_all_files(os.path.join(train_folder, 'answer'))
    for file in answer_files:
        train += read_training_data(os.path.join(train_folder, 'answer', file), False)

    return train

def read_training_data(file_path, question_type):
    train = []
    with open(file_path) as f:
        for line in f:
            elements = line.strip().split('\t')
            feature = fe.get_feature(elements[4])
            if question_type:
                train.append((feature, elements[1]))
            else:
                train.append((feature, elements[2]))

    return train

