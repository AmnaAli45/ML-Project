# All the functionalities that are common in whole project are created in this file
import os
import sys
import pandas as pd
import numpy as np
import dill #this library help us to create pickle file
from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        #yeh function file_path se directory ka part nikalta hai.
        #Example: agar file_path = "models/model.pkl" hai → dir_path = "models"
        os.makedirs(dir_path,exist_ok=True) #Yeh directory create karta hai agar wo pehle se exist na karti ho.
        with open(file_path,"wb") as file_obj: 
        #File ko binary write mode mein khola ja raha hai (wb).
        #Matlab file overwrite hogi aur new binary data likha jaaega.
            dill.dump(obj,file_obj) 
            #dill ek library hai jo Python objects ko serialize (convert to binary form) karke file mein store kar sakti hai (pickle ke tarah).
            #Isse baad mein aap wahi object file se load karke dobara use kar sakte ho.
    except Exception as e:
        raise CustomException(e,sys)

