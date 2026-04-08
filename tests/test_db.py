import pandas as pd
from app.db_csv import save_deck
from datetime import datetime


TEST_PATH = 'decks-data'
TEST_NAME_FILE = 'decks.csv'
TEST_NAME = 'deck-prueba-01'
TEST_CODE = 'abc-123-123-abc'


def test_create_directory(tmp_path):
    p = tmp_path / TEST_PATH
    f = p / TEST_NAME_FILE

    save_deck(path=f, name=TEST_NAME, code=TEST_CODE)
    assert p.exists()
    assert p.is_dir()
    assert len(list(tmp_path.iterdir())) == 1


def test_create_file(tmp_path):
    p = tmp_path / TEST_PATH
    f = p / TEST_NAME_FILE

    save_deck(path=f, name=TEST_NAME, code=TEST_CODE)
    assert f.exists()
    assert f.is_file()


def test_data_saved(tmp_path):
    p = tmp_path / TEST_PATH
    f = p / TEST_NAME_FILE
    
    save_deck(path=f, name=TEST_NAME, code=TEST_CODE)
    date_now = datetime.now().strftime("%d/%m/%Y")
    df = pd.read_csv(f)
    print(df)
    print(df['name'][0], type(df['name'][0]))
    
    assert df['name'][0] == TEST_NAME
    assert df['code'][0] == TEST_CODE
    assert df['date'][0] == date_now
    # assert 0

