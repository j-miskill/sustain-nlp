"""
    Helper class for taking the raw data and producing a quality input data source for 
    model training
"""
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification



class TrainingDataCreator:

    def __init__(self, filename):
        self.filename = filename

    def create_merged_df(self):
        esg_documents_df = pd.read_csv(self.filename, separator="|")
        cdp_scores_df = pd.read_csv('./cdp_scores.csv')
        esg_documents_df = esg_documents_df.drop("Unnamed: 0", axis=1)
        merged_df = pd.merge(esg_documents_df, cdp_scores_df, how='left', left_on='symbol', right_on='Ticker')
        merged_df.dropna(subset=['CDP Score'], inplace=True) # drop rows without a CDP score
        return merged_df
    
    def create_good_training_data(self):
        pass


        


    

