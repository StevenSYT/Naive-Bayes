import preProcess as pp
import os
class NB_Classifier:
   def __init__(self, trainPath, testPath):
      self.vocabulary=[]
      self.N_docs=0
      self.clasLists=[]
class Clas:
   def __init__(self, clasPath):
      self.N_docs=0
      #token store the tokens from all documents in the class
      self.tokens=[]
   class Doc:
      def __init__(self):
         self.tokens=[]

# directory = os.fsencode("20news-bydate/20news-bydate-train/comp.graphics")
# for file in os.listdir(directory):
