from nltk.stem import *
from nltk.stem.porter import *

STEMMER = PorterStemmer()
print STEMMER.stem("shotted")