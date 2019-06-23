import os
from util.system import Message as SystemMessage
from util.file import Checker as FileChecker

def remove_file(path):
    if not FileChecker.path_type_check(path):
        SystemMessage.error(2060101)
    if FileChecker.path_empty_check(path):
        SystemMessage.error(2060102)
    if not FileChecker.path_length_check(path):
        SystemMessage.error(2060103)
    if not FileChecker.file_exists(path):
        SystemMessage.warning(2060104)
        return
    os.remove(path)