# bring in all the methods from ./utils directory
from utils.combineDataFrame import CombineDataFrame
from utils.getSSLInformation import GetAPIInfo, GetSSLInformation, GetServerCertificate
from utils.runBackgroundProcess import RunBackgroundProcess
from utils.parseArgs import ParseArgs, getBoolean
from utils.writeInfoFile import WriteInfoFile

# first iteration: I will go through the code and explain roughly what the script does
# in a second iteration: I will go into the different methods that are being used here and explain the code in the utils folder

if __name__ == "__main__":
  
  # create object where all text information is stored
  writeInfo=""
  args = ParseArgs()
  
  # fetch the SSL-certificate
  # Retrieve the certificate from the server at the specified address, and return it as a PEM-encoded string
  # PEM (originally “Privacy Enhanced Mail”) is the most common format for X. 509 certificates, CSRs, and cryptographic keys. A PEM file is a text file containing one or more items in Base64 ASCII encoding, each with plain-text headers and footers (e.g. -----BEGIN CERTIFICATE----- and -----END CERTIFICATE----- )
  writeInfo += GetServerCertificate(**vars(args))
  
  # if -i is enabled-> get additional information
  if getBoolean(args.info): writeInfo+= GetSSLInformation(**vars(args))
  
  # if -c is supplied
  # fetch server ciphers and compare to online DB
  if getBoolean(args.compare):
     
    # run testssl to get server ciphers and store them into csv file in ./data
    RunBackgroundProcess(**vars(args))
    
    # get API information about the security of ciphers (https://ciphersuite.info/api/cs)
    respJson = GetAPIInfo(**vars(args))
    
    # check server ciphers in terms of security
    # combine the two seperate dataframes into one file based on the cipher name
    dfm = CombineDataFrame(respJson)
    
    writeInfo+=f"\n--------------------\n\nDATAFRAME WITH CIPHER SECURITY INFORMATION\n{dfm}\n"
    
    
  # print out all the gathered information to the terminal
  print(f"\n\nCERTIFICATE & RELATED INFORMATION\n\n{writeInfo}")
    
  # write the information to file in the ./data directory
  WriteInfoFile(writeInfo=writeInfo, **vars(args))
  
  # most important pieces of information are:
  # - public key (certificate)
  # - the name of the server (commonName)
  # - trusted authority (caIssuer)
  # - period of validity (notBefore, notAfter)
  
  
  
  
  
  
  
  
  