import web_tokens
import freq_dist

tokens = web_tokens.get("https://en.wikipedia.org/wiki/NLP")

freq_dist.plot(tokens, omit=["retrieved", "archived", "wikipedia"])
