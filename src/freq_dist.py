from typing import Iterable

from nltk.corpus import stopwords
from nltk import FreqDist


def plot(tokens: Iterable[str], *, first_n: int=None, omit: Iterable[str]=None):
    if omit is None:
        omit = []
    
    omit.extend(stopwords.words("english"))

    def is_clean(s: str):
        return all([
            len(s) > 2, 
            s.isalpha(), 
            s not in omit, 
        ])

    clean_tokens = filter(is_clean, tokens)

    freq = FreqDist(clean_tokens)

    if first_n is None:
        freq.plot()
    else:
        freq.plot(first_n)