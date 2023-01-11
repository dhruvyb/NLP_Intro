import spacy
nlp = spacy.load("en_core_web_sm")

# Garden path sentence strings
sent1 = '''The old man the boat.'''

sent2 = "The complex houses married and single soldiers and their families."

sent3 = "The cotton clothing is made of grows in Mississippi."

sent4 = "I know the words to that song about the Queen don\'t rhyme."

sent5 = "The man who hunts ducks out on weekends."

# sentences put into list
gardenpathSentences = [sent1, sent2, sent3, sent4, sent5]


# for loop to iterate through sentences
for i in gardenpathSentences:

    # sentences processed with language model
    sent_doc = nlp(i)

    #sentence tokenised to obtain token value
    print([(token, token.orth_, token.orth) for token in sent_doc ])
    

    example = nlp(i)
    
    # sentence put through entity recognition.
    print([(j, j.label_, j.label) for j in example.ents])
    print("\n")


# The above sentences do not go through the entity recognition successfully, with the exception of the words; 'Mississippi', 'Queen' and 'weekend'
# This is because these words are unambiguous and only have one meaning.
# With garden path sentences, the language processor model is unable to carry out the entitity recognition because of the ambiguity of the type of word, whether it is a noun or verb and returns a blank list.
# 'Queen' is identified as a Person because of the capital 'Q'
# 'Mississippi' is identified as 'GPE' which means Geopolitical Entity, which is simply a geographical place like a city or state.