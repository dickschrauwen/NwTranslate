# example.py

# Import class NwTranslate
from nwtranslate import NwTranslate

# Create an instance 
# Params: 
# 1 the folder where the translations live
# 2 the default language (language used in your code base)
#   - you may choose anything for the default language
translator = NwTranslate('./translations', 'dl')

# Set the target language
# You may change this anytime
translator.set_target('en')

# Create a shorthand, for example
myT = translator.translate

# Do it
print(myT('appel'))
print(myT('monster'))
print(myT("Het bestand '{0}' bestaat niet").format('crucial.err'))

# Does not exist in dl_en.py
print(myT('This is not in dl_en.py'))
