import numpy as np
import pandas as pd
import srt
from loguru import logger
#from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from src.data import DATA_DIR


class Subtitle:
    # TODO: df should be a class variable (so must be modified) for more than one movie for only one user
    def __init__(self, file_path):
        self.file_path = file_path
        self.user_all_subtitles = []
        
        with open(self.file_path) as f:
            subtitle_generator = srt.parse(f)
            self.present_subtitle_partitions = [sub.content for sub in subtitle_generator]
            self.user_all_subtitles.append(''.join(self.present_subtitle_partitions))
           

    def tokenize(self):
        logger.info('tokenizing is in progress')
 
        df = pd.DataFrame({'subtitles': ['friends.s01e01'], 'text':self.user_all_subtitles})

        # initialize
        cv = CountVectorizer(stop_words='english') 
        cv_matrix = cv.fit_transform(df['text']) 
        # create document term matrix
        df_dtm = pd.DataFrame(cv_matrix.toarray(), index=df['subtitles'].values, columns=cv.get_feature_names_out())

        return df_dtm
        
if __name__ ==  '__main__':
    from src.data import DATA_DIR
    
    sub_file_path = DATA_DIR / 'subtitles' / 'friends.s01e02.720p.srt'
    sub = Subtitle(sub_file_path)
    top_ten = sub.tokenize().iloc[0, :].sort_values(ascending=False)[:10].to_string()
    print ('The most common words are : ', top_ten, sep='\n')
 