from util.file import Checker as FileChecker
from util.file import Creator as FileCreator
from util.system import Message as SystemMessenger
from util.system import Type as VarietyType


def write(file_path, context):
    '''
        :param file_path: type(str)
        :param context: type(str)
        :return: None
    '''
    if not file_check(file_path):
        SystemMessenger.error(2010101)

    if not context_check(context):
        SystemMessenger.error(2010102)

    try:
        file = open(file_path, 'w', encoding='utf-8-sig')
        file.write(context)
        file.close()
    except IOError as ioe:
        SystemMessenger.error(2010103)
    except FileNotFoundError as fnfe:
        SystemMessenger.error(2010104)
    except FileExistsError as fee:
        SystemMessenger.error(2010105)


def file_check(file_path):
    if FileChecker.path_empty_check(file_path):
        SystemMessenger.error(2010201)
        return False

    if not FileChecker.path_type_check(file_path):
        SystemMessenger.error(2010202)
        return False

    if FileChecker.file_exists(file_path):
        SystemMessenger.warning(2010203)
        ###############################
    else:
        FileCreator.create(file_path)

    if not FileChecker.file_writeable(file_path):
        SystemMessenger.error(2010204)
        return False

    return True


def context_check(context):
    if not VarietyType.is_str(context) and not VarietyType.is_int(context):
        return False
    return True


def write_part(file_path, context, startline, stopline):
    '''
    :param file_path:
    :param context:
    :param startline:
    :param stopline:
    :return:
    '''
    pass


def write_append(file_path, context):
    '''
    :param file_path: 
    :param context: 
    :return: 
    '''
    pass
