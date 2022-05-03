# Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary

#{"merry":"good", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

# and use it to translate Christmas wished from English to Swedish

def translate(bilingual_dict, english_words_list):
    # Write your logic here
    swedish_words_list = []
    for word in english_words_list:
        swedish_words_list.append(bilingual_dict[word])

    return swedish_words_list


bilingual_dict = {"merry": "good", "christmas": "jul",
                  "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
english_words_list = ["merry", "christmas"]
print("The bilingual dict is:", bilingual_dict)
print("The english words are:", english_words_list)

swedish_words_list = translate(bilingual_dict, english_words_list)
print("The equivalent Swedish words are:", swedish_words_list)


# i just dont even know where to begin with this one
