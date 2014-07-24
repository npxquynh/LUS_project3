import nltk
import training_data as td
import testing_data as ted
import pdb

def write_result(filename):
    with open('./result/' + filename, 'w') as output:
        output.writelines("%s\n" % item for item in abc)

if __name__ == '__main__':
    # TRAIN_FOLDER = './train_questions/tokenized'
    # TEST_FOLDER = './test_questions/tokenized'
    TRAIN_FOLDER = './train_set/stemmed'
    TEST_FOLDER = './test_set/stemmed'

    train = td.create_training_data(TRAIN_FOLDER)
    test = ted.create_testing_data(TEST_FOLDER)

    classifier = nltk.classify.NaiveBayesClassifier.train(train)
    abc = classifier.classify_many(test)
    write_result('bayes.txt')

    classifier = nltk.classify.DecisionTreeClassifier.train(
        train,
        entropy_cutoff=0,
        support_cutoff=0
    )
    abc = classifier.classify_many(test)
    write_result('decision_tree.txt')

