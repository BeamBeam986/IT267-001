import numbers
import re
from select import select
from tokenize import Number
from unicodedata import name


class Account:
    def __init__(self) -> None:
        self.type=''
        self.number= ''
        self.balance=0
    
    def open_account(self,name:str,type:str,accno:str,balance:int=0) -> None:
        self.name = name
        self.type = type
        self.accno = accno
        self.balance = balance
    
    def ditsplay(self) -> None:
        return f'{self.name} account balance = {self.balance}baht'