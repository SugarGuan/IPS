from util.system import Message as SystemMessage

def create(path):
    try:
        file = open(path, 'w')
        file.close()
    except IOError as e:
        SystemMessage.error(2040101)
    except FileExistsError as fee:
        SystemMessage.error(2040102)
