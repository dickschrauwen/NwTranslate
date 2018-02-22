# how-to-use-in-flask.py
# --------------------------------------------
# Flask Example 
# --------------------------------------------

# Import NwTranslate class from nwtranslate module
from ..translate.nwtranslate import NwTranslate

# Create an instance `translator` with a translations folder
# defined in a flask config and default language `xx`
# xx is used in development and will be showed if no translation into
# a target language  is available

translator = NwTranslate(app.config['TRANSLATEFOLDER'], 'xx')

# Set the initial target language
translator.set_target('nl')

# Create a concise function
trnslt = lambda to_translate_str: translator.translate(to_translate_str)

# --------------------------------------------
# Make `trnslt` available in Jinja2 templates
# --------------------------------------------

# Jinja filter {{ src | T }}
app.jinja_env.filters['T'] = trnslt

# Jinja function {{ TT('static text') }}
@app.context_processor
def utility_processor():
    return dict(TT=trnslt, LEN=len)

jinjastr = lambda x: str(x)
@app.context_processor
def utility_processor():
    return dict(jinja_str=jinjastr, LEN=len)

