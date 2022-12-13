import os

CURRENT_FOLDER = os.getcwd()
WORK_FOLDER = 'TextFiles'
FILE_NAME = 'TextResult.txt'

full_path = os.path.join(CURRENT_FOLDER, WORK_FOLDER, FILE_NAME)

with (open('TextFiles/1.txt', encoding='utf-8') as f1,
      open('TextFiles/2.txt', encoding='utf-8') as f2,
      open('TextFiles/3.txt', encoding='utf-8') as f3):
    content1 = f1.readlines()
    line_counter1 = len(content1)
    content2 = f2.readlines()
    line_counter2 = len(content2)
    content3 = f3.readlines()
    line_counter3 = len(content3)

text_dict = {
    line_counter1: ['1.txt', content1],
    line_counter2: ['2.txt', content2],
    line_counter3: ['3.txt', content3]
    }

with open (full_path, 'w', encoding='utf-8') as result_file:
    for counter, content in sorted(text_dict.items()):
        result_file.write(f'{content[0]}\n')
        result_file.write(f'{str(counter)}\n')
        result_file.write(f'{("".join(content[1]))}\n')