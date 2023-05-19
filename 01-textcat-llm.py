from spacy import util

config = util.load_config("config/config.cfg")
nlp = util.load_model_from_config(config, auto_fill=True)
doc = nlp("A Loud G.O.P. Minority Pledges to Make Trouble on Ukraine Military Aid")
print(doc.cats)