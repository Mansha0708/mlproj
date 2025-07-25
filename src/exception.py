import sys #lib for exception handling
import logging

def error_msg_detail(error,error_detail:sys): #error_details will present in sys
    _,_,exc_tb=error_detail.exc_info()  # this will give 3 info we only want the last one
    #all info will provided like in which line
    file_name=exc_tb.tb_frame.f_code.co_filename # will give file name jisme error h
    error_msg="error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    
    )
    return error_msg
class customexp(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg=error_msg_detail(error_msg,error_detail=error_detail)
    def __str__(self):
        return self.error_msg
