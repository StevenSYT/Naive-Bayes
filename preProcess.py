import nltk
import string
from stop_words import get_stop_words
# sentence="i love machine learning. lol"
# tokens= nltk.word_tokenize(sentence)
#
# print(tokens)
# fileName="../20news-bydate/20news-bydate-train/comp.graphics/38291"
#doc=open(path,'r', encoding='latin_1')
def genTokens(fileName):
   #delete useless lines
   print("loading"+ fileName)
   doc = open(fileName,'r', encoding='latin_1')
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
      line=line.lower()
      line=line.translate(translator)
      tokens+=nltk.word_tokenize(line)

   #exclude stop words
   stop_words=get_stop_words('en')
   tokenList=[]
   for i in tokens:
      if i not in stop_words and len(i)<=10 and len(i)>=3:
         tokenList.append(i)


   doc.close()
   return tokenList

# fileName="../20news-bydate/20news-bydate-train/comp.graphics/38291"
# print (genTokens(fileName))
