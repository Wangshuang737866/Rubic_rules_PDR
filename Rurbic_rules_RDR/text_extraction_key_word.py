from nltk import tokenize
from operator import itemgetter
import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import argparse


#print("td_idf_score",tf_idf_score)

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n])
    return result

if __name__ == '__main__':
 parser = argparse.ArgumentParser()
 parser.add_argument('--n', type=int, default=5)
 parser.add_argument('--dataset', type=str, default='answer', help="")
 parser.add_argument('--data_path', type=str, default='data/student_answer')
 #parser.add_argument('--dataname', type=str, default='answer', help="")
 args = parser.parse_args()
 f = open(args.data_path)
 doc = f.read()
 # doc = 'I am a graduate. I want to learn Python. I like learning Python. Python is easy. Python is interesting. ' \
 # 'Learning increases thinking. Everyone should invest time in learning'
 total_words = doc.split()
 total_word_length = len(total_words)
 # print(total_word_length)
 stop_words = set(stopwords.words('english'))
 # print("stop_words",stop_words)
 total_words = doc.split()
 total_word_length = len(total_words)
 # print("total_w_l",total_word_length)
 total_sentences = tokenize.sent_tokenize(doc)
 total_sent_len = len(total_sentences)
 # print("total_sent_len",total_sent_len)
 tf_score = {}
 for each_word in total_words:
     each_word = each_word.replace('.', '')
     if each_word not in stop_words:
         if each_word in tf_score:
             tf_score[each_word] += 1
         else:
             tf_score[each_word] = 1

 # Dividing by total_word_length for each dictionary element
 tf_score.update((x, y / int(total_word_length)) for x, y in tf_score.items())


 # print("tf_score",tf_score)
 def check_sent(word, sentences):
     final = [all([w in x for w in word]) for x in sentences]
     sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
     return int(len(sent_len))


 idf_score = {}
 for each_word in total_words:
     each_word = each_word.replace('.', '')
     if each_word not in stop_words:
         if each_word in idf_score:
             idf_score[each_word] = check_sent(each_word, total_sentences)
         else:
             idf_score[each_word] = 1

 # Performing a log and divide
 idf_score.update((x, math.log(int(total_sent_len) / y)) for x, y in idf_score.items())

 # print("idf_score",idf_score)

 tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
#
#n=5
#n=args.__init__()
#print(str)
 keywords=get_top_n(tf_idf_score, args.n).keys()
 print("keywords",keywords)