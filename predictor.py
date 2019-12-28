import spacy
nlp = spacy.load('en_core_web_md')
import pickle
infile = open('token_save.pkl','rb')
tokenizer = pickle.load(infile)
infile.close()
from tensorflow.keras.models import load_model
model = load_model('epochBIG.h5')
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
def transform(input_sent, model, tokenizer):
  word_list = input_sent.split()
  print("ded")
  result = word_list[0] +' '+ word_list[1]
  for i in range(len(word_list)-2):
    encoded_text = tokenizer.texts_to_sequences([result])[0]
    pad_encoded = pad_sequences([encoded_text], maxlen=25, truncating='pre')
    pred_word_ind = model.predict(pad_encoded, verbose=0)[0]
    pred_word_ind = pred_word_ind.argsort()[-3:][::-1]
    indx = 0
    similarity = 0
    for j in range(3):
        try:
            this_sim = nlp(str(tokenizer.index_word[pred_word_ind[j]])).similarity(str(nlp(tokenizer.index_word[word_list[i]])))
            if this_sim > similarity:
                indx = j
                similarity = nlp(str(tokenizer.index_word[pred_word_ind[j]])).similarity(str(nlp(tokenizer.index_word[word_list[i]])))
        except:
            indx = 0
    pred_word = tokenizer.index_word[pred_word_ind[indx]] 
    result += ' ' + pred_word

  return result

def wsi_magic(input_string):
    return transform(input_string, model, tokenizer)