import jieba
from util.system import Message as SystemMessage
from util.system import Type as Type
from util.file import Checker as FileChecker
from util.file import Writer as FileWriter
from util.file import Reader as FileReader
from util.file import Cleaner as FileCleaner
from util.file import Remove as FileRemover
from util.list import Cleaner as ListCleaner

jieba.setLogLevel(11)


def cut(input_list):
    if not Type.is_list(input_list):
        SystemMessage.error(3010101)
    output_list = []
    for eachline in input_list:
        eachline_cut = jieba.cut(eachline)
        eachline_cut = ListCleaner.spilt_list_context_all_level(eachline_cut)
        output_list.append(eachline_cut)
    return output_list


def cut_to_file(input_file_path, out_file_path):
    if not FileChecker.input_output_file_check(input_file_path, out_file_path):
        SystemMessage.die()
    input_file_list = FileReader.read(input_file_path)
    cutted_list = cut(input_file_list)
    output_file_list = []
    output_file_str = ''

    for sentence in cutted_list:
        output_file_list.append(' '.join(sentence))

    for sentence in output_file_list:
        output_file_str  = output_file_str + sentence + '\n'

    FileWriter.write(out_file_path, output_file_str)
    FileCleaner.remove_space_emptyline(out_file_path, out_file_path + 'tmp')
    FileCleaner.remove_space_emptyline(out_file_path + 'tmp', out_file_path)
    FileRemover.remove_file(out_file_path + 'tmp')



