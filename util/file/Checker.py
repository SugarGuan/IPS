import os
from util.system import Message as SystemMessage
from util.system import Type as SystemType


def path_empty_check(str):
    if SystemType.is_empty_str(str):
        return True
    return False


def path_type_check(str):
    if SystemType.is_str(str):
        return True
    return False


def path_length_check(str):
    if len(str) > 255:
        return False
    return True


def file_exists(path):
    if os.path.exists(path):
        return True
    return False


def file_readable(path):
    if os.access(path, os.R_OK):
        return True
    return False


def file_writeable(path):
    if os.access(path, os.W_OK):
        return True
    return False


def output_file_check(out_file_path):
    if path_empty_check(out_file_path):
        SystemMessage.error(2050101)
        return False
    if not path_type_check(out_file_path):
        SystemMessage.error(2050102)
        return False
    if not path_length_check(out_file_path):
        SystemMessage.error(2050103)
        return False
    if file_exists(out_file_path):
        SystemMessage.warning(2050104)
        if not file_writeable(out_file_path):
            SystemMessage.error(2050105)
            return False
    return True


def input_file_check(input_file_path):
    if path_empty_check(input_file_path):
        SystemMessage.error(2050201)
        return False
    if not path_type_check(input_file_path):
        SystemMessage.error(2050202)
        return False
    if not path_length_check(input_file_path):
        SystemMessage.error(2050203)
        return False
    if not file_exists(input_file_path):
        SystemMessage.error(2050204)
        return False
    if not file_readable(input_file_path):
        SystemMessage.error(2050205)
        return False
    return True


def input_output_file_check(input_file_path, out_file_path):
    if path_empty_check(input_file_path):
        SystemMessage.error(2050301)
        return False
    if path_empty_check(out_file_path):
        SystemMessage.error(2050302)
        return False
    if not path_type_check(input_file_path):
        SystemMessage.error(2050303)
        return False
    if not path_type_check(out_file_path):
        SystemMessage.error(2050304)
        return False
    if not path_length_check(input_file_path):
        SystemMessage.error(2050305)
        return False
    if not path_length_check(out_file_path):
        SystemMessage.error(2050306)
        return False
    if not file_exists(input_file_path):
        SystemMessage.error(2050307)
        return False
    if not file_readable(input_file_path):
        SystemMessage.error(2050308)
        return False
    if file_exists(out_file_path):
        SystemMessage.warning(2050309)
        if not file_writeable(out_file_path):
            SystemMessage.error(2050310)
            return False
    return True


def getsize_B(path):
    if not input_file_check(path):
        SystemMessage.error(2050401)
    return os.path.getsize(path)


def getsize_MB(path):
    return int(getsize_B(path)/1024)


def getsize_GB(path):
    return getsize_B(path)/1048576