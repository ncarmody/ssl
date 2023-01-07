# bring in all the methods from ./utils directory
from utils.combineDataFrame import CombineDataFrame
from utils.getSSLInformation import GetAPIInfo, GetSSLInformation, GetServerCertificate
from utils.runBackgroundProcess import RunBackgroundProcess
from utils.parseArgs import ParseArgs, getBoolean
from utils.writeInfoFile import WriteInfoFile




if __name__ == "__main__":
  
  # create object where all text information is stored
  writeInfo=""
  args = ParseArgs()
  
  # if -c is supplied
  # fetch server ciphers and compare to online DB
  if getBoolean(args.compare):
     
    # run testssl to get server ciphers and store them into csv file in ./data
    RunBackgroundProcess(**vars(args))
    
    # get API information about the security of ciphers
    respJson = GetAPIInfo(**vars(args))
    
    # check server ciphers in terms of security
    dfm = CombineDataFrame(respJson)
    
    print(dfm)
    writeInfo+=f"compared ciphers of server:\n{dfm}\n"
    
    
    
  # fetch the SSL-certificate
  writeInfo += GetServerCertificate(**vars(args))
  
  # if -i is enabled-> get additional information
  if getBoolean(args.info): writeInfo+= GetSSLInformation(**vars(args))
  
  # write the information to file in the ./data directory
  WriteInfoFile(writeInfo=writeInfo, **vars(args))
  
  
  
  
  