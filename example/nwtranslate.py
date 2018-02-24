# nwtranslate.py
VERSION = '0.4 2017-03-07'

'''
Started: 2016-02-07
Purpose: easy translation of web-apps (flask)
Python:  3.x
Platform: win7+
Author:  dickschrauwen
USAGE:   see => testtranslate.py
----------------- ----------------- ----------------- ----------------- ----------------- ----------------- 
TODO:
-     
    
----------------- ----------------- ----------------- ----------------- ----------------- ----------------- 
'''

# ----------------------------------
#  LOCAL CONSTANTS
# ----------------------------------

FN_NOTFOUND = 'missing.txt'   # in <data_folder>/<src_target>
MAX_PHRASE_LENGTH = 128
NOT_ALLOWED_FILENAME_CHARS = '><:"/\\|?*' + ''.join([chr(i) for i in range(0,32)])
# https://msdn.microsoft.com/en-us/library/windows/desktop/aa365247%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396

# ----------------------------------
# IMPORTS
# ----------------------------------

from collections import OrderedDict
import os, sys

# ----------------------------------
# NICEWARE TRANSLATE
# ----------------------------------

class NwTranslate(object):
    
    
     # ---------------------------------- # ----------------------------------
     # translator = NwTranslate('w:/sites/flask/translations', 'nl')
     # set: data-folder & source language
     # ---------------------------------- # ----------------------------------

    def __init__(self, data_dir='.', default_language='en'):
        self.data_dir = data_dir #+'/'
        self.def_lan  = default_language
        
    def set_target(self, target_language):
        self.target_lan = target_language
        self.target_body = self.def_lan + '_' + target_language
        self.target_file = self.target_body + '.py'
        self.target_full = self.data_dir +'/' + self.target_file
        # check / create translation file
        if not os.path.isfile(self.target_full):
            with open(self.target_full, 'w', encoding='UTF-8', errors='surrogateescape') as f:
                f.write('# ' + self.target_file + '\n')
                f.write("""
from collections import OrderedDict
td = OrderedDict([
('''<default>''', '''<target>'''),

])""")
        if not(self.data_dir=='.' or  self.data_dir in sys.path):
            sys.path.append(self.data_dir)
        self.translations = __import__(self.target_body)
    
# return translated string
    def translate(self, phrase, file=None):
        # do nothing
        if self.target_lan == self.def_lan: return phrase

        # folders en files
        file_folder      = self.data_dir + '/' + self.def_lan + '_' + self.target_lan
        missing_filename = file_folder + '/' + FN_NOTFOUND

        # explicit file or long phrase => translation from file
        is_block = False
        if file:
            full_filename    = file_folder + '/' + str(file) + '.txt'
            is_block = True
        else:
            if len(phrase) > MAX_PHRASE_LENGTH:
               full_filename =  file_folder + '/' + self.phrase_to_filebody(phrase) +  '.txt'
               is_block = True

        # translate('something_BIG')
        if is_block:
            # read the translation file, or write source language phrase to file in target folder
            return self.translate_block(phrase, file, full_filename, file_folder)
            
        # translate('something_small')
        else:
            ttd = self.translations.td
            if phrase in ttd:
                return ttd[phrase]
            else:
                # ..... save missing ...
                self.add_missing_phrase(missing_filename, phrase)
                return(phrase)
            pass
    
        

    # --------------------------------------------------
    # HELPERS
    # --------------------------------------------------
    
    @staticmethod
    def phrase_to_filebody(phrase):
        raw_body = phrase[:MAX_PHRASE_LENGTH]
        return ''.join([c for c in list(raw_body) if c not in NOT_ALLOWED_FILENAME_CHARS])
    
    @staticmethod
    def translate_block(phrase, file, full_filename, file_folder):
        '''Read the translation file (full_filename),
        or write source language phrase to file (full_filename+FN_NOTFOUND)
        in target folder (file_folder).'''
        
        try:
            with open(full_filename,'r', encoding='UTF-8', errors='surrogateescape') as f:
               return f.read()
        except:
            try:
                os.mkdir(file_folder)
            except:
                pass
            file_to_write = full_filename + FN_NOTFOUND
            if os.path.isfile(file_to_write):
                return phrase  # write file only once
            else:
                with open(file_to_write,'w', encoding='UTF-8', errors='surrogateescape') as f:
                    f.write(phrase)
            return phrase

    
    @staticmethod
    def add_missing_phrase(filename, missing_phrase):
        is_there = False
        to_write = """('''{0}''','''{0}'''),\n""".format(missing_phrase)
        if os.path.isfile(filename):
            # check
            with open(filename, 'r', encoding='UTF-8', errors='surrogateescape') as f:
                all = f.read()
                is_there = (to_write in all)
            if not is_there:
                # append
                with open(filename,'a', encoding='UTF-8',errors='surrogateescape') as f:
                    f.write(to_write)
        else:
            # create
            with open(filename,'w', encoding='UTF-8', errors='surrogateescape') as f:
                f.write(to_write) 


    
