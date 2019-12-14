import os

RAW_DATA_DIR = '/Users/holker/University/Diploma/Processing/images'  # path where raw non-sorted images are located
MIN_AGE = 12  # minimum age for sorting


# parse filenames and sort files by gender
def sort_genders():
    for filename in os.listdir(RAW_DATA_DIR):
        if filename != 'female' \
                and filename != 'male' \
                and filename != '.DS_Store' \
                and filename != 'too_young' \
                and filename != 'glasses' \
                and filename != 'no_glasses':
            filename_parts = filename.split('_')
            print(filename)
            if int(filename_parts[0]) < MIN_AGE:
                os.rename(f'{RAW_DATA_DIR}/{filename}', f'{RAW_DATA_DIR}/too_young/{filename}')
            elif filename_parts[1] == '0':
                os.rename(f'{RAW_DATA_DIR}/{filename}', f'{RAW_DATA_DIR}/male/{filename}')
            elif filename_parts[1] == '1':
                os.rename(f'{RAW_DATA_DIR}/{filename}', f'{RAW_DATA_DIR}/female/{filename}')
            else:
                print('Wrong file name')


# import info about glasses from meta.txt file
def import_meta():
    images_map = dict()
    with open('meta.txt') as meta_file:
        for line in meta_file:
            line_parts = line.split(" ")
            images_map[line_parts[0]] = line_parts[1]
    return images_map


# sort images by glasses
def sort_glasses():
    images_map = import_meta()
    for filename in os.listdir(RAW_DATA_DIR):
        if filename != 'female' \
                and filename != 'male' \
                and filename != '.DS_Store' \
                and filename != 'too_young' \
                and filename != 'glasses' \
                and filename != 'no_glasses':
            if images_map[filename] == '0\n':
                os.rename(f'{RAW_DATA_DIR}/{filename}', f'{RAW_DATA_DIR}/no_glasses/{filename}')
            elif images_map[filename] == '1\n':
                os.rename(f'{RAW_DATA_DIR}/{filename}', f'{RAW_DATA_DIR}/glasses/{filename}')
            else:
                print('Current file was not mapped')
