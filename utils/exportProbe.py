import pickle
def ExportProbe(thingsToTransfer=None,loadOrGet='load',fileName= 'dic.pkl'):
  print(thingsToTransfer)
  if thingsToTransfer==None:
    with open(fileName, 'rb') as dicFile:
      thingsToTransfer = pickle.load(dicFile)
      
    return thingsToTransfer

  elif thingsToTransfer!=None:
    with open(fileName, 'wb') as dicFile:
    
      pickle.dump(thingsToTransfer, dicFile)