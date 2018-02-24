# NwTranslate
A simple  and effective python module for multi language (web) applications

For now, take a look at :
- testtranslate.py
- (for using with flask) how-to-use-in-flask.py

# Usage

```
# Import class NwTranslate

from nwtranslate import NwTranslate

# Create an instance 
# Params: 
# 1 the folder where the translations live
# 2 the default language (language used in your code base)
#   - you may choose anything for the default language

translator = NwTranslate('./translations', 'dl')  
```

Let's create some translations from `dl` into `en` (english)
Create `dl_en.py` in the `.translations` folder



print("""
The constructor of the NwTranslate class, needs two params:
- the folder where the translation files live
- the base (default) language
Just press <enter> for defaults
""")


thedir    = input('directory  (./test) > ') or './test'
deflan    = input('deflan         (en) > ') or 'en'
targetlan = input('targetlan      (nl) > ') or 'nl'
translator = NwTranslate(thedir,deflan)
translator.set_target(targetlan)
T = translator.translate


while True:
    to_translate = input('(Try: to bad, ugly, tree, Python, AI) Translate? > ')
print(T(to_translate))


