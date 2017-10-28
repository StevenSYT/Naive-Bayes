import preProcess as pp
from pathlib import Path
import numpy as np
import os

class NB_Classifier:
   def __init__(self, trainPath, testPath):
      self.totalDocs=0
      self.clasLists=[]

   #needs to store the names of the classes in the clasList
   def trainOnDir(self, aDir):
      pathes = Path(aDir).iterdir()
      self.clasLists = list(map(lambda x: Clas(x), pathes))
      self.totalDocs=sum(map(lambda x: x.N_docs, self.clasLists))
      for x in clasLists:
         x.prior = x.N_docs/totalDocs

   def classifyDoc(self, docName):
      estimates = list(map(lambda x: x.logAPosterioriEstimate(docName), self.clasLists))
      return clasLists[np.argmax(estimates)].name

   def testOnDir(self, aDir):
      pathes = Path(aDir).iterdir()

class Clas:
   def __init__(self, naem, clasPath=None):
      #eh?
      self.name = naem
      self.N_docs=0
      self.prior=0
      #token store the tokens from all documents in the class
      self.tokenCounts={}
      #total number of seen words in the data set does not change after training period.
      self.totalWordCount=0
      if clasPath != None:
         trainFromCorpus(clasPath)
   class Doc:
      def __init__(self):
         self.tokens=[]

   def trainFromCorpus(self, dirname):
      pathe = Path(dirname)
      if pathe.is_dir():
        for x in pathe.iterdir():
           if x.is_file():
              self.train(genTokens(x))
              self.N_docs += 1

   def train(self, trainingList):
      for token in trainingList:
         self.tokenCount[token]+=1
         self.totalWordCount+=1

   def logAPosterioriEstimate(self, doc):
      wordList = genTokens(doc)
      #adds unseen words to the list of token counts.
      for word in wordList:
         self.tokenCounts[word]+=0
      return log(self.prior)+sum(map(lambda x: log(laplace(self.tokenCounts[x], self.totalWordCount, 1, len(self.tokenCounts)), wordList))

# directory = os.fsencode("20news-bydate/20news-bydate-train/comp.graphics")
# for file in os.listdir(directory):
def laplace(x, N, pseudocount, newVocabSize):
   return (x+pseudocount)/(N+pseudocount*newVocabSize)
