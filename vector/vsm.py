from util.file import Checker as FileChecker
from sklearn.feature_extraction.text import TfidfVectorizer

def generate(list):
    '''

    :param list:
    :return: vsm: type:list
    '''

    vectorizer = TfidfVectorizer()
    svm = vectorizer.fit_transform(list)




    vsm = []
    return vsm

def generate_from_file(file_path):
    FileChecker.input_file_check(file_path)