from util.file import Checker as FileChecker
from util.system import Message as SystemMessenger


def read(file_path):
    if FileChecker.path_empty_check(file_path):
        SystemMessenger.error(2000101)
    if not FileChecker.path_type_check(file_path):
        SystemMessenger.error(2000102)
    if not FileChecker.file_exists(file_path):
        SystemMessenger.error(2000103)
    if not FileChecker.file_readable(file_path):
        SystemMessenger.error(2000104)
    file_content = []
    try:
        file = open(file_path, 'r', encoding='utf-8-sig')
        file_content = file.readlines()
        file.close()
    except MemoryError as moe:
        SystemMessenger.error(2000105)
    except IOError as ioe:
        SystemMessenger.error(2000106)
    # except FileNotFoundError as fnfe:
    #     SystemMessenger.error(2000107)
    # except FileExistsError as fee:
    #     SystemMessenger.error(2000108)
    return file_content


def read_part(file_path, startline, stopline):
    pass
