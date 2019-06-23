from util.system import Type
from util.system import Message as SystemMessage
from util.list import Cleaner as ListCleaner
from util.file import Checker as passFileChecker
from util.file import Writer as FileWriter
from util.file import Reader as FileReader
from util.file import Cleaner as FileCleaner

def remove_stopword(input_list, stopword_file_path):
    if not Type.is_list(input_list):
        SystemMessage.error(31101)

    if not passFileChecker.input_file_check(stopword_file_path):
        SystemMessage.die()

    output_list = []
    stopword_list = ListCleaner.spilt_list_context_front_level(FileReader.read(stopword_file_path))
    for sentence in input_list:
         sentence_stopword_removed = []
         for word in sentence:
             if word not in stopword_list:
                 sentence_stopword_removed.append(word)
             else:
                 pass
         output_list.append(sentence_stopword_removed)

    return output_list


def remove_stopword_list(input_path, stopword_file_path):
    if not passFileChecker.input_file_check(input_path):
        SystemMessage.die()
    input_file_list = FileReader.read(input_path)
    input_list = []
    for sentence in input_file_list:
        word_list = sentence.replace('\n', '').split(' ')
        input_list.append(word_list)
    return remove_stopword(input_list, stopword_file_path)


def remove_stopword_file(input_path, output_path, stopword_file_path):
    if not passFileChecker.output_file_check(output_path):
        SystemMessage.die()
    removed_word_list = remove_stopword_list(input_path, stopword_file_path)
    output_file_list = []
    output_file_str = ''
    for sentence in removed_word_list:
        output_file_list.append(' '.join(sentence))
    for sentence in output_file_list:
        output_file_str = output_file_str + sentence + '\n'
    FileWriter.write(output_path, output_file_str)
    FileCleaner.remove_space_emptyline(output_path, output_path)
