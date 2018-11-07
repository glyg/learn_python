"""
Header creation utility

"""
import json
import sys
from datetime import datetime


def create_header(authors_json, date=None, place="Paris"):
    """

    Parameters
    ----------
    authors_json : str, path to the authors json file
    date: optional, a datetime.date object, default to today
    palce: a location

    """
    if date is None:
        date = datetime.today()

    try:
        date_str = date.strftime('%d-%m-%Y')
    except AttributeError:
        print(f'date argument is of type datetime not'
              f' {type(date)}')
        date_str = str(date)

    with open(authors_json, 'r') as authors_json_read:
        authors = json.load(authors_json_read)

    if not len(authors):
        raise ValueError("Authors dictionnary can't be empty")

    str_list = [date_str, '\n']
    for author in authors.values():
        author_str = ' '.join([author.get('firstname', ''),
                               author.get('lastname', '')])
        str_list.append(author_str)
    return '\n'.join(str_list)


if __name__ == '__main__':

    json_path = sys.argv[1]
    print(create_header(json_path))
