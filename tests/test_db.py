import pandas as pd
from app.db_csv import save_deck
from datetime import datetime
from app.codes_info.parallel_tcg import regions


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


def test_save_deck_with_code_info(tmp_path):
    p = tmp_path / TEST_PATH
    f = p / TEST_NAME_FILE
    
    code = "CB-379,CB-240,3xCB-204"
    save_deck(path=f, name=TEST_NAME, code=code)
    
    df = pd.read_csv(f)
    print(df)
    assert df['code'][0] == code
    assert df['paragon'][0] == "Niamh, Wielder of Faith"
    assert df['region'][0] == regions.shroud.value


def test_save_multiple_decks(tmp_path):
    p = tmp_path / TEST_PATH
    f = p / TEST_NAME_FILE

    code_1 = "CB-379,CB-240,3xCB-204"
    code_2 = "CB-21,CB-517,3xCB-25"
    save_deck(path=f, name="deck_01", code=code_1)
    save_deck(path=f, name="deck_02", code=code_2)

    df = pd.read_csv(f)

    assert df['code'][0] == code_1
    assert df['paragon'][0] == "Niamh, Wielder of Faith"
    assert df['region'][0] == regions.shroud.value
    
    assert df['code'][1] == code_2
    assert df['paragon'][1] == "Arak, Combat Overseer"
    assert df['region'][1] == regions.augencore.value
