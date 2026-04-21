import pandas as pd
from pandas.errors import EmptyDataError
from pathlib import Path
from datetime import datetime
from app.codes_info.parallel_tcg import code_info


DEFAULT_PATH = Path().home() / '.save-deck'

DEFAULT_FILE_PATH = DEFAULT_PATH / 'decks.csv'



# name, code, date
def save_deck(name:str, code:str, path: Path=DEFAULT_FILE_PATH):
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


if __name__ == '__main__':
    # test
    save_deck('a', 'b')
