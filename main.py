from utils.combineDataFrame import CombineDataFrame
from utils.getSSLInformation import GetAPIInfo, GetSSLInformation, GetServerCertificate
from utils.runBackgroundProcess import RunBackgroundProcess
from utils.parseArgs import ParseArgs, getBoolean
from utils.writeInfoFile import WriteInfoFile




if __name__ == "__main__":
  writeInfo=""
  args = ParseArgs()
  
  if getBoolean(args.compare): 
    RunBackgroundProcess(**vars(args))
    respJson = GetAPIInfo(**vars(args))
    dfm = CombineDataFrame(respJson)
    print(dfm)
    writeInfo+=f"compared ciphers of server:\n{dfm}\n"
    
    
    
  
  writeInfo += GetServerCertificate(**vars(args))
  
  if getBoolean(args.info): writeInfo+= GetSSLInformation(**vars(args))
  
  
  WriteInfoFile(writeInfo=writeInfo, **vars(args))