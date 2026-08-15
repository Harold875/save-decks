import os

from dotenv import load_dotenv, set_key
import pandas as pd
from pandas.errors import EmptyDataError
from pathlib import Path
from datetime import datetime
from app.codes_info.parallel_tcg import code_info


DEFAULT_PATH = Path().home() / '.save-deck'

DEFAULT_FILE_PATH = DEFAULT_PATH / 'decks.csv'

ENV_FILE_PATH = DEFAULT_PATH / 'config' / '.env'
load_dotenv(dotenv_path=ENV_FILE_PATH)

CUSTOM_PATH = os.getenv('CUSTOM_SAVE_PATH')

# Use CUSTOM_PATH or DEFAULT_FILE_PATH
if CUSTOM_PATH is not None:
    deck_save_path = Path(CUSTOM_PATH)
else:
    deck_save_path = DEFAULT_FILE_PATH


# name, code, date
def save_deck(name:str, code:str, path: Path | None=None):

    if path is None:
        path = deck_save_path


    data = {
        "name": name.strip(),
        "date": datetime.now().strftime("%d/%m/%Y")
    }
    new_df = pd.DataFrame([data])

    # add info code (paragon and region)
    info = code_info(code.strip())
    if info is not None:
        df_code = pd.DataFrame([info])
        new_df = pd.concat([new_df, df_code], axis=1)
    
    
    # add code at the end of the dataframe
    new_df['code'] = code.strip()
    
    if not path.exists():
        # create directory is not exists
        if not path.parent.exists():
            path.parent.mkdir()
        
        # create file and save data.
        new_df.to_csv(path, index=False)
        print('File created and saved')
        return
    
    try:
        df = pd.read_csv(path)
    except EmptyDataError:
        df = pd.DataFrame()

    save_df = pd.concat([df, new_df])
    save_df.to_csv(path, index=False)
    
    print('Data saved')


def update_custom_path(new_path: str, path: Path=ENV_FILE_PATH):
    """
    Esta funcion sirve para cambiar la ruta donde se guardan los decks.
    
    Parameters:
        new_path: Es la nueva ruta en donde se guardaran los decks. Debe ser un directorio.
    
        path: Es la ruta donde se guardan las variables de entorno. 
            Debe ser la ruta del archivo.
    
    """
    global deck_save_path
    
    if not isinstance(new_path, str):
        raise TypeError("new_path is not a string. Must be a string.")
    
    def create_directory_is_not_exist(path:Path):
        if path.exists():
            return
        create_directory_is_not_exist(path.parent)
        path.mkdir()
        
    
    if not path.exists():
        # create directory is not exists
        p = path.parent
        create_directory_is_not_exist(p)
        
        # create file.
        path.touch()
    
    p = Path(new_path) / "decks.csv"
    set_key(dotenv_path=path, key_to_set='CUSTOM_SAVE_PATH', value_to_set=str(p))
    deck_save_path = p
    print('Enviroment Variable changed')
    print(deck_save_path)


def get_deck_save_path():
    global deck_save_path
    return deck_save_path

if __name__ == '__main__':
    # test
    save_deck('a', 'b')
