from util.system import Type
from util.system import Message as SystemMessage


def spilt_str(input_context):
    if Type.is_int(input_context):
        input_context = str(input_context)
    if not Type.is_str(input_context):
        SystemMessage.error(21101)
    return input_context.strip()


def spilt_list_context_front_level(input_list):
    output_list = []
    for value in input_list:
        if Type.is_str(value) or Type.is_int(value):
            output_list.append(spilt_str(value))
        else:
            output_list.append(value)
    return output_list


def spilt_list_context_all_level(input_list):
    output_list = []
    for value in input_list:
        if Type.is_str(value) or Type.is_int(value):
            output_list.append(spilt_str(value))
        elif Type.is_list(value):
            output_list.append(value)
        else:
            SystemMessage.error(21102)
    return output_list


def spaceline_remove(input_list):
    output_list = []
    if not Type.is_list(input_list):
        SystemMessage.error(2110401)
    if len(input_list) == 0:
        SystemMessage.error(2110402)

    for line in input_list:
        if Type.is_list(line):
            output_list.append(spaceline_remove(line))
        if not Type.is_str(line) and not Type.is_int(line):
            SystemMessage.error(2110403)
        line = spilt_str(line)
        if line != '' and line != '\n':
            output_list.append(line)
    return output_list


