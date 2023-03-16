import shutil
from pathlib import Path


CATEGORIES = {'image': ['.JPEG', '.PNG', '.JPG', '.SVG'],
              'video': ['.AVI', '.MP4', '.MOV', '.MKV'], 'document': ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.XLS', '.PPTX'], 'music':
              ['.MP3', '.OGG', '.WAV', '.AMR'], 'archives': ['.ZIP', '.GZ', '.TAR', '.LNN']}


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

CYRILLIC_SYMBOLS1 = [i for i in CYRILLIC_SYMBOLS]
CYRILLIC_SYMBOLS = ", ".join(CYRILLIC_SYMBOLS1)
BAD_SYMBOLS = tuple(chr(i) for i in range(32, 48) if i != 46) + \
    tuple(chr(i) for i in range(58, 65)) + \
    tuple(chr(i) for i in range(91, 97)) + \
    tuple(chr(i) for i in range(123, 128))


def normalize(item):

    for c, l in zip(CYRILLIC_SYMBOLS1, TRANSLATION):

        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    for a in BAD_SYMBOLS:

        TRANS[ord(a)] = '_'

    name1 = str(item).translate(TRANS)
    return name1


def move_file(file: Path, root_dir: Path, category: str):

    if category != "other":
        file = file.rename(normalize(file.name))

    target_folder = root_dir / category
    if not target_folder.exists():
        target_folder.mkdir()
    if file.suffix.upper() in CATEGORIES['archives']:
        archive_folder = target_folder / file.stem
        if not archive_folder.exists():
            archive_folder.mkdir()
        shutil.unpack_archive(str(file), str(archive_folder))
        file.unlink()
        return

    return file.replace(target_folder / file.name)


def get_categories(file: Path):
    extension = file.suffix.upper()
    # print(extension)
    for cat, exts in CATEGORIES.items():

        if extension in exts:
            # file = file.rename(normalize(file.name))
            return cat

    return 'other'


def sort_dir(root_dir: Path, current_dir: Path):

    for item in [f for f in current_dir.glob('*') if f.name not in CATEGORIES.keys()]:

        if not item.is_dir():

            category = get_categories(item)

            new_path = move_file(item, root_dir, category)

        else:
            sort_dir(root_dir, item)
            if not any(item.iterdir()):
                item.rmdir()


def main():
    try:
        path = Path('C:/Users/Operator/Desktop/Мотлох')

    except IndexError:
        return f'No path to folder. Take as patametr'

    if not path.exists():
        return 'Sorry, folder not exist'

    sort_dir(path, path)

    return "All ok"


if __name__ == '__main__':
    print(main())
