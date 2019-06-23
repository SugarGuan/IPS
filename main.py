from util.file import Cleaner as FileCleaner
from util.file import Reader as FileReader
from pre_process import cutting
from pre_process import filter

# file_path = 'D:/Project/Python/NLP/K-means-classification/Text-lib/1.txt'
# # file_path2 = 'D:/Project/Python/NLP/K-means-classification/Text-lib/12.txt'
# # file_path3 = 'D:/Project/Python/NLP/K-means-classification/Text-lib/13.txt'
# file_path4 = 'D:/Project/Python/NLP/K-means-classification/Text-lib/14.txt'
# file_path5 = 'D:/Project/Python/NLP/K-means-classification/Text-lib/15.txt'
# pass_path = 'D:/Project/Python/NLP/K-means-classification/Text-lib/stopword.txt'
# # FileCleaner.remove_space_emptyline(file_path, file_path2)
# # cutting.cut_to_file(file_path2, file_path3)
#
#
# cutting.cut_to_file(file_path, file_path4)
# filter.remove_stopword_file(file_path4, file_path5, pass_path)


file_base = 'D:/Project/Python/NLP/IPS/library/'
input_file = file_base + 'input.txt'
stopword_file = file_base + 'stopword.txt'
cleaned_file_save_as = file_base + 'cleanedoutput.txt'
cutting_file_saveas = file_base + 'cuttingoutput.txt'
stopword_fliter_saveas = file_base + 'filteroutput.txt'


print(input_file)
print(cleaned_file_save_as)

FileCleaner.remove_space_emptyline(input_file, cleaned_file_save_as)
cutting.cut_to_file(cleaned_file_save_as, cutting_file_saveas)
# filter.remove_stopword_file(cutting_file_saveas, stopword_fliter_saveas, stopword_file)
