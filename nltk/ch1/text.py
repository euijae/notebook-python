# import init
from nltk.book import (
    text1,
    text2,
    text3,
    text4
)

# searching text
text1.concordance("monstrous")
text2.common_contexts(["monstrous", "very"])
text3.concordance("lived")
text4.similar("monstrous")

arr = ["citizens", "democracy", "freedom", "duties", "America"]
# text4.dispersion_plot(arr)
