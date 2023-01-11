# NLP_Intro
Solution to Task 37

Download python file and requirements file to directory on your local drive.
change the directory on your terminal console to the above directory

type the follwing into the command line:

pip install -r requirements.txt

run python file


Explanation of Code
The above sentences do not go through the entity recognition successfully, with the exception of the words; 'Mississippi', 'Queen' and 'weekend'
This is because these words are unambiguous and only have one meaning.
With garden path sentences, the language processor model is unable to carry out the entitity recognition because of the ambiguity of the type of word, whether it is a noun or verb and returns a blank list.
'Queen' is identified as a Person because of the capital 'Q'
'Mississippi' is identified as 'GPE' which means Geopolitical Entity, which is simply a geographical place like a city or state.
