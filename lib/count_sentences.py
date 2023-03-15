#!/usr/bin/env python3

import re

class MyString:
  
    def __init__(self, value=""):
        self.value = value

    def set_value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")
    
    def get_value(self):
        return self._value

    value = property(get_value, set_value)

    def is_sentence(self):
        if self._value[-1] == ".":
            return True
        else:
            return False
    
    def is_question(self):
        if self._value[-1] == "?":
            return True
        else:
            return False
    
    def is_exclamation(self):
        if self._value[-1] == "!":
            return True
        else:
            return False
        
    def count_sentences(self):
        new_value = re.split("\.+|\?|\!+", self._value)
        if len(new_value) == 1:
            return 0
        else:
            return len(new_value) -1

        


