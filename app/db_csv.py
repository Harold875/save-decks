import pandas as pd
from pandas.errors import EmptyDataError
from pathlib import Path
from datetime import datetime


DEFAULT_PATH = Path().home() / '.save-deck/decks.csv'

# name, code, date
def save_deck(name:str, code:str, path: Path=DEFAULT_PATH):
    data = {
        "name": name.strip(),
        "code": code.strip(),
        "date": datetime.now().strftime("%d/%m/%Y")
    }
    new_df = pd.DataFrame([data])

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