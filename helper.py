"""
    Helper class for taking the raw data and producing a quality input data source for 
    model training
"""
import pandas as pd
import numpy as np
import platform
from transformers import pipeline
import tensorflow as tf
import torch
from flax import nnx
from transformers import AutoTokenizer, AutoModelForSequenceClassification



class TrainingDataCreator:

    def __init__(self, filename):
        self.filename = filename
        self.final_df = None

    def create_merged_df(self):
        esg_documents_df = pd.read_csv(self.filename, sep="|")
        cdp_scores_df = pd.read_csv('./cdp_scores.csv')
        esg_documents_df = esg_documents_df.drop("Unnamed: 0", axis=1)
        merged_df = pd.merge(esg_documents_df, cdp_scores_df, how='left', left_on='symbol', right_on='Ticker')
        merged_df.dropna(subset=['CDP Score'], inplace=True) # drop rows without a CDP score
        self.merged_df = merged_df
        return merged_df
    

    def get_all_environmental_sentences(self, merged_df):
        new_df = merged_df
        for i, row in new_df.iterrows():
            print(f"working on: {row['company']}")
            content = row['content']
            list_of_sentences = content.split(".")
            print("num sentences:", len(list_of_sentences))
            text = ""
            sum = 0
            for s in list_of_sentences:
                if sum % 100 == 0:
                    print("analyzing sentence:", sum)
                sum += 1
                if self.predict_environmental_sentence(s):
                    text += s
                else:
                    continue
            row['content'] = text
        
        return new_df

    
    def predict_environmental_sentence(self, s):
        tokenizer_name = "ESGBERT/EnvironmentalBERT-environmental"
        model_name = "ESGBERT/EnvironmentalBERT-environmental"
        
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, max_len=512)

        pipe = pipeline("text-classification", model=model, tokenizer=tokenizer) # set device=0 to use GPU
        score_df = pipe(s, padding=True, truncation=True)


        if score_df[0]['label'] == "environmental" and score_df[0]['score'] >= 0.85:
            return True
        else:
            return False



        

    def analyze(self):
        pass


        


    

