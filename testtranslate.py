# test_translate.py
from nwtranslate import NwTranslate
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

