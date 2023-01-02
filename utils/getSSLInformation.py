import socket
import ssl
import requests
import os

from utils.parseArgs import getBoolean
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



port=443
context = ssl.create_default_context()


def GetSSLInformation(hostname,verbose,  **kwargs):
  writeInfo=""
  if getBoolean(verbose): print("run GetSSLInformation")

  with socket.create_connection((hostname, port)) as sock:
      with context.wrap_socket(sock, server_hostname=hostname) as ssock:

          ssock.do_handshake()
          cert = ssock.getpeercert()
          
          for keys, values in zip(cert.keys(), cert.values()):
            if str(type(values))!="<class 'tuple'>":
              writeInfo+="\n".join([f"{keys}: {values}"])
              
              
            elif keys=="subject": 
              writeInfo+="\n".join([f"{keys}:", *[f"\t{keyValue[0][0]}: {keyValue[0][1]}" for keyValue in values]])
            
            elif keys=="subjectAltName": 
              writeInfo+="\n".join([f"{keys} (SAN):", *[f"\t{keyValue[0]}: {keyValue[1]}" for keyValue in values]])
            
            elif keys=="caIssuers": 
              writeInfo+="\n".join([f"{keys}:", *[f"\t{value}" for value in values]])
              
            writeInfo+="\n"


          writeInfo+="\n".join(["peerName: ", *[f"\t{peerKey}: {peerValue}" for peerKey, peerValue in zip(["ip", "port"], ssock.getpeername())]])
  print(writeInfo)
  return writeInfo

def GetServerCertificate(hostname,verbose,  path=f"{ROOT_DIR}/data", **kwargs):
  if getBoolean(verbose): print("run GetServerCertificate"); print(f"path: {path}")

  f = open(f"{path}/{str(hostname).replace('.', '_')}_cert.der",'wb')
  cert = ssl.get_server_certificate((hostname, port))
  f.write(ssl.PEM_cert_to_DER_cert(cert))
  writeInfo = f"**************\n CERTIFICATE OF {str(hostname).upper()}\n  {cert}\n**************\n"
  print(writeInfo)
  return writeInfo

def GetAPIInfo(verbose, **kwargs):
  if getBoolean(verbose): print("run GetServerCertificate")


  response = requests.get("https://ciphersuite.info/api/cs")

  if getBoolean(verbose):
    if response.status_code == 200:
      print("The request was a success!")
    elif response.status_code == 404:
      print("Result not found!")
  return response.json()