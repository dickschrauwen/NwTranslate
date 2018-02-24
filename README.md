# NwTranslate
A simple  and effective python module for multi language (web) applications

For now, take a look at :
- testtranslate.py
- (for using with flask) how-to-use-in-flask.py

# Usage

```
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
```

Let's create some translations from `dl` into `en` (english)
- Create `dl_en.py` in the `.translations` folder
- Edit `dl_en.py` as follows

```
# translations/dl_en.py
from collections import OrderedDict
td = OrderedDict([
  # ('''<default>''', '''<target>'''),
  ('appel','apple'),
  ('monster','monster'),
  ("Het bestand '{0}' bestaat niet",  "'{0}' does not exist"),
  # ...
])
```
**Missing translations**
- Create a folder `dl_en` in `translations`
- Create a plain empty UTF-8 text file `missing.txt` in `translations/dl_en`
- When a translation is not available in `td` (the translation-dict) it will be written to `translations/dl_en/missing.txt`
- and the actual output of `myT('unknown/missing')` will be `'unknown/missing'`

**Now you can translate phrases in `example.py`**
```
# example.py
# ...
print(myT('appel'))
print(myT('monster'))
print(myT("Het bestand '{0}' bestaat niet").format('crucial.err'))
# ...
```

# Notes
- Make sure the user running `example.py` has the right permissions for writing and updating the `translations`-folder
