import nltk
import string
from stop_words import get_stop_words
# sentence="i love machine learning. lol"
# tokens= nltk.word_tokenize(sentence)
#
# print(tokens)
path="../deeta/20news-bydate-train/comp.graphics/38291"
doc=open(path,'r', encoding='latin_1')
def genTokens(doc):
   #delete useless lines
   docLineList=doc.readlines()
   i=0
   while(i<len(docLineList)):
      if 'Lines' in docLineList[i]:
         break
      i+=1
   docLineList=docLineList[i+1:]

   #filter the lines: exclude punctuations and digits("0123456789")

   filterKeys=string.punctuation+string.digits
   translator= str.maketrans(dict.fromkeys(filterKeys))

   #tokenize the document
   tokens=[]
   for line in docLineList:
      line=line.translate(translator)
      tokens+=nltk.word_tokenize(line)

   #exclude stop words
   stop_words=get_stop_words('en')
   tokens=[i for i in tokens if i not in stop_words]

   return tokens
print (genTokens(doc))
