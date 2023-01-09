import pickle
import os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ExportProbe(thingsToTransfer=None,loadOrGet='load',fileName= f'{ROOT_DIR}/debug/dic.pkl'):
  print(thingsToTransfer)
  if thingsToTransfer==None:
    with open(fileName, 'rb') as dicFile:
      thingsToTransfer = pickle.load(dicFile)
      
    return thingsToTransfer

  elif thingsToTransfer!=None:
    with open(fileName, 'wb') as dicFile:
    
      pickle.dump(thingsToTransfer, dicFile)
      
      