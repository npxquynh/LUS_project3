import nltk
import training_data as td
import testing_data as ted
import pdb

def write_result(filename):
    with open('./result/' + filename, 'w') as output:
        output.writelines("%s\n" % item for item in abc)

def classifier_result(train_folder, test_folder):
    train = td.create_training_data(train_folder)
    test, test_label = ted.create_testing_data(test_folder)

    # Naive Bayes
    classifier = nltk.classify.NaiveBayesClassifier.train(train)
    print nltk.classify.accuracy(classifier, train)
    print nltk.classify.accuracy(classifier, test)

    # abc = classifier.classify_many(test)
    # write_result('bayes.txt')

    # Decision Tree
    classifier = nltk.classify.DecisionTreeClassifier.train(
        train,
        entropy_cutoff=0,
        support_cutoff=0
    )
    print nltk.classify.accuracy(classifier, train)
    print nltk.classify.accuracy(classifier, test)
    # abc = classifier.classify_many(test)
    # write_result('decision_tree.txt')

if __name__ == '__main__':
    print "Tokenized"
    TRAIN_FOLDER = './train_set/tokenized'
    TEST_FOLDER = './test_set/tokenized'
    classifier_result(TRAIN_FOLDER, TEST_FOLDER)

    print "Stemmed"
    TRAIN_FOLDER = './train_set/stemmed'
    TEST_FOLDER = './test_set/stemmed'
    classifier_result(TRAIN_FOLDER, TEST_FOLDER)



