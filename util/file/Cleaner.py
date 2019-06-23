from util.system import Type as Type
from util.system import Message as SystemMessage
from util.file import Writer as FileWriter
from util.file import Reader as FileReader
from util.file import Creator as FileCreator
from util.file import Checker as FileChecker
from util.file import Reader as FileReader
from util.list import Cleaner as ListCleaner


def remove_space(input_file_path, out_file_path):
    if not FileChecker.input_output_file_check(input_file_path, out_file_path):
        SystemMessage.die()
    # input_file = FileReader.read(input_file_path)
    # input_file_list = ListCleaner.spilt_list_context_all_level(input_file)
    # =>  ListCleaner.spilt_list_context_all_level(FileReader.read(input_file_path))
    FileWriter.write(out_file_path, '\n'.join(ListCleaner.spilt_list_context_all_level(FileReader.read(input_file_path))))


def remove_emptyline(input_file_path, out_file_path):
    if not FileChecker.input_output_file_check(input_file_path, out_file_path):
        SystemMessage.die()
    # input_file = FileReader.read(input_file_path)
    # input_file_list = ListCleaner.spilt_list_context_all_level(input_file)
    # =>  ListCleaner.spaceline_remove(FileReader.read(input_file_path))
    FileWriter.write(out_file_path, '\n'.join(ListCleaner.spaceline_remove(FileReader.read(input_file_path))))

def remove_space_emptyline(input_file_path, out_file_path):
    if not FileChecker.input_output_file_check(input_file_path, out_file_path):
        SystemMessage.die()
    remove_space(input_file_path, out_file_path)
    remove_emptyline(input_file_path, out_file_path)
