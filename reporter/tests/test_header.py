import datetime
import json
import tempfile
from header import create_header


def test_header_str():
    tmp_json = tempfile.mktemp(suffix='json')
    authors = {'auth0': {'firstname': 'tuytu',
                         'lastname': 'tuytu'},
               'auth2': {'firstname': 'tuytu'}}

    with open(tmp_json, 'w') as fh:
        json.dump(authors, fh)

    date = datetime.date(2018, 11, 25)
    result = create_header(tmp_json, date=date, place='Paris')
    print(result)
