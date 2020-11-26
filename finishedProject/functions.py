#no need to change anything in this file!

#SMS Spam Filter Imports
import random
import pandas as pd
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def categorize_words():
    '''
    Catagorizes each spam/non-spam word into a corresponding list
    Repeating words in each list will help with categorizing
    '''
    spam_words = []
    ham_words = []
    for sms in data['processed'][data['label'] == 'spam']:
        for word in sms:
            spam_words.append(word)
    for sms in data['processed'][data['label'] == 'ham']:
        for word in sms:
            ham_words.append(word)
    return spam_words, ham_words

def predict(user_input):
  spam_counter = 0
  ham_counter = 0

  #add text colour : ham is green, spam is red
  red = [220,50,50]
  green = [100,220,50]

  for word in user_input:
    spam_counter += spam_words.count(word)
    ham_counter += ham_words.count(word)

  if ham_counter > spam_counter:
    #adding accuracy
    certainty = round((ham_counter / (ham_counter + spam_counter)) * 100, 2)
    return 'message is not spam, with {}% certainty'.format(certainty), green
  elif spam_counter > ham_counter:
    certainty = round((spam_counter / (ham_counter + spam_counter)) * 100, 2)
    return 'message is spam, with {}% certainty'.format(certainty), red
  else:
    return 'message could be spam, with 50% certainty', [255,255,255]

def pre_process(sms):
    '''
    Remove punctuation and stop words from the custom sms
    '''
    remove_punct = "".join([word.lower() for word in sms if word not in string.punctuation])
    tokenize = nltk.tokenize.word_tokenize(remove_punct)
    remove_stop_words = [word for word in tokenize if word not in nltk.corpus.stopwords.words('english')]
    return remove_stop_words

data = pd.read_csv('SMSSpamCollection.txt', sep = '\t', header=None, names=["label", "sms"])
data['processed'] = data['sms'].apply(lambda x: pre_process(x))

#creating lists to store spam/non-spam associated words and their instances
spam_words, ham_words = categorize_words()
