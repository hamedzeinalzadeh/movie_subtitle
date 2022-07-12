from src.data import DATA_DIR
from utils.parse_subtitle import Subtitle

def test_tokenizer():
    sub_file_path = DATA_DIR / 'subtitles' / 'friends.s01e02.720p.srt'
    sub = Subtitle(sub_file_path)
    top_ten = sub.tokenize().iloc[0, :].sort_values(ascending=False)[:10]
    
    assert False == top_ten.isnull().values.any()
