import os
import sys #because we are going to use customexception class
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # basically used to create class variables in short

#any kind of input that data ingestion requires comes through the following class
@dataclass #while working in a class we need to use __init__ function to create class variab;les but this decorator is used to create class variables directly.
class DataIngestionConfig:
    train_data = os.path().join("artifacts","train.csv")# it will create a folder named artifacts and all the outputs of data ingestion are stored in this folder.
    test_data = os.path().join("artifacts","test.csv")
    raw_data = os.path().join("artifacts","data.csv")
# above are the inputs that we are going to give our data ingestion component so that it will know where to store test,train and raw data.

#if you are only definig the variables in class then @dataclass decorator is used but your class have various functions then it is best to use __init__ function.
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #jese hi DataIngestion ka object bne ga to DataIngestionConfig class k variables initialize ho kr ingestion_config
        #mein store ho jayen ge
    
    #Following method is used to read the dataset whether from a database or from a local file.
    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or component.")
        try:
            df = pd.read_csv("notebook\data\Student Performance new.csv")
            logging.info('Read dataset as a dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data),exist_ok=True) # ye train data k naam ka folder bnaye ga
            # self.ingestion_config.train_data → this is a file path (like "artifacts/train.csv").
            # os.path.dirname(...) → takes only the folder part of that path (e.g. "artifacts").
            # os.makedirs(..., exist_ok=True) → makes that folder if it does not already exist.
            # If the folder already exists, exist_ok=True means “don’t give an error.” 
            df.to_csv(self.ingestion_config.raw_data,index=False,header=True) # saves your dataset (df) into a CSV file inside that folder.

            logging.info("Train-test split initiated")
            train_set,test_set = train_test_split(df,test_size = 0.2,random_state = 42)
            train_set.to_csv(self.ingestion_config.train_data,index=False,header=True) #saving train data in train data defined path
            test_set.to_csv(self.ingestion_config.test_data,index=False,header=True) #saving test data in train data defined path

            logging.info("Ingestion of data is completed.")

            return( # following information is required by data transformation component
                self.ingestion_config.train_data,
                self.ingestion_config.test_data
                )

        except Exception as e:
            raise CustomException(e,sys) #automatically exception will be raised

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
            

