import preProcess as pp
from pathlib import Path
import numpy as np
import os
import math as m
import sys

class NB_Classifier:
   def __init__(self):
      self.totalDocs=0
      self.clasLists=[]

   #needs to store the names of the classes in the clasList
   def trainOnDir(self, aDir):
      pathes = Path(aDir).iterdir()
      self.clasLists = list(map(lambda x: Clas(x.parts[-1], x), pathes))
      self.totalDocs=sum(map(lambda x: x.N_docs, self.clasLists))
      for x in self.clasLists:
         x.prior = x.N_docs/self.totalDocs

   def classifyDoc(self, docName):
      wordList = pp.genTokens(str(docName))
      estimates = list(map(lambda x: x.logAPosterioriEstimate(wordList), self.clasLists))
      #list of indices classes which are most likely
      maxList = np.argwhere(estimates == np.amax(estimates)).flatten().tolist()
      priorList = list(map(lambda x: self.clasLists[x].prior, maxList))
      return self.clasLists[maxList[np.argmax(priorList)]].name

   #test on a directory containing subdirectories that contain documents of a single class,
   #return accuracy over all docs tested.
   #rigorously test this, I feel confident I made a mistake, and it could be hard
   #to detect.
   def testOnDir(self, aDir):
      p=Path(aDir)
      pathes = [direct for direct in p.iterdir() if direct.is_dir()]
      pathes2 = pathes
      def aFunc(docList, clas):
         acc=0
         for doc in docList:
            classifee = self.classifyDoc(str(doc))
            arf = int(classifee == clas)
            acc+=arf
            if arf==0:
               print("WRONG! on " + str(doc) + " classifier guessed " + classifee)
         return acc
      #i prefer lambdas, though.
      #aFunc = lambda docList, clas: sum(map(lambda x: int(self.classifyDoc(str(x)) == clas), docList))
      countFiles = lambda path: list(filter(lambda x: x.is_file(), path.iterdir()))
      testSize = sum(map(lambda x: len(countFiles(x)), pathes))
      accuracy = sum(map(lambda x: aFunc(x.iterdir(),str(x.parts[-1])), pathes2)) / testSize
      #count = sum(map(lambda x: aFunc(x.iterdir(),str(x.parts[-1])), pathes2))
      print(testSize)
      #print(count)
      print(accuracy)
      return accuracy

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
         self.trainFromCorpus(clasPath)
   class Doc:
      def __init__(self):
         self.tokens=[]

   def trainFromCorpus(self, dirname):
      pathe = Path(dirname)
      if pathe.is_dir():
        for x in pathe.iterdir():
           if x.is_file():
              self.train(pp.genTokens(str(x)))
              self.N_docs += 1

   def train(self, trainingList):
      for token in trainingList:
         try:
            self.tokenCounts[token]+=1
         except KeyError:
            print("class " + self.name + " adding " + token + " to my vocab")
            self.tokenCounts[token]=1
         self.totalWordCount+=1

   def logAPosterioriEstimate(self, wordList):
            #adds unseen words to the list of token counts.
      for word in wordList:
         try:
            self.tokenCounts[word]
         except:
            self.tokenCounts[word]=0
      return m.log(self.prior)+sum(map(lambda x: m.log(laplace(self.tokenCounts[x], self.totalWordCount, 1, len(self.tokenCounts))), wordList))

   def printCounts(self):
     print()
     print(self.tokenCounts)
     print()
# directory = os.fsencode("20news-bydate/20news-bydate-train/comp.graphics")
# for file in os.listdir(directory):
def laplace(x, N, pseudocount, newVocabSize):
   return (x+pseudocount)/(N+pseudocount*newVocabSize)

nbClassi=NB_Classifier()
nbClassi.trainOnDir(sys.argv[1])
nbClassi.testOnDir(sys.argv[2])
