import sys # built-in standard library module that provides access to variables, functions, and objects that interact 
#directly with the Python interpreter.

def errorMessageDetail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()  # exc_info() --> it will return 3 values (exc_type, exc_value, traceback) but we 
    #are interested only in third one 
    filename = exc_tb.tb_frame.f_code.co_filename #gives the filename where the error happened.
    lineno = exc_tb.tb_lineno  # gives the line number where the error happened.
    error = str (error)
    error_message = f"Error occured in Python script file [{filename}] line number [{lineno}] error message: [{error}] "
    return error_message

#Creating our own exception class that inherits Exception --> built in class. So that our class will act as a standard class
class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message) #calling parent class constructor
        self.error_message = errorMessageDetail(error_message,error_details) # function ne jo customized error msg return krna hai 
        # wo is mein store krwane k lye us function ko call krna hai
    
    def __str__ (self): #__str__ defines what gets printed
        return self.error_message
    
