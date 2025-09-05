import os
import sys
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl") # agr kisi model ko pickle file mein save krna hai to us ko path ki zroort ho gy

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        # Tis function in responsible for data transformation
        try:
            Numerical_features =  ['reading score percentage', 'writing score percentage']
            Categorical_features = ['race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'sex']

            #Numerical Pipeline
            num_pipeline = Pipeline(
                steps = [
                    ("Simple Imputer" , SimpleImputer(strategy = "median")), # to fill missing values with median... because there are some outliers in numeriacla columns
                    ("Scaler",StandardScaler())
                ]
            )
            # Categorical Pipeline
            cat_pipeline = Pipeline(
                steps = [
                    ("Simple Imputer" , SimpleImputer(strategy = "most_frequent")), # to fill missing values with mode... 
                    ("one_hot_encoder",OneHotEncoder()),
                    ("Scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info("Scaling of numerical feature completed.")
            logging.info("Encoding of categorical feature completed.")

            #combinig the numerical and categorical pipeline
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,Numerical_features),
                    ("cat_pipeline",cat_pipeline,Categorical_features)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e)
    
    def initiate_data_transformation(self,train_path,test_path): # we get this test and train path from data_ingestion
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read test and train data completed.")
            logging.info("obtaining preprocessing object.")

            preprocessing_object = self.get_data_transformer_object()
            target_column = "math percentage"
            Numerical_features =  ['reading score percentage', 'writing score percentage']

            input_feature_train_df = train_df.drop([target_column],axis = 1)
            target_feature_train_df = train_df[target_column]

            input_feature_test_df = test_df.drop([target_column],axis = 1)
            target_feature_test_df = test_df[target_column]

            logging.info("Preprocessing object on training and testing object.")

            input_feature_train_arr=preprocessing_object.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_object.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)] # np.c_ is used for column wise cocatenation
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object.")
            #saving pickle file in hard disk
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path, # complete path jahan save ho gy pickle file
                obj=preprocessing_object
            )
                
            return(train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file_path)

        
        
        except Exception as e:
            raise CustomException(e,sys)

         

