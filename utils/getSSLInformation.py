import socket
import ssl
import requests
import os

from utils.parseArgs import getBoolean
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



port=443
context = ssl.create_default_context()


def GetSSLInformation(hostname, verbose, **kwargs):
  writeInfo=""
  # print out additional information
  if getBoolean(verbose): print("run GetSSLInformation")
  
  # start SSL connection
  with socket.create_connection((hostname, port)) as sock:
      with context.wrap_socket(sock, server_hostname=hostname) as ssock:
          # initiate the handshake to establish the secret key for communication
          ssock.do_handshake()
          # get the certificate from the server with additional information
          cert = ssock.getpeercert()
          
          # read this information out from cert object if interesting
          # example of cert structure to be iterated over:
          # cert: {'subject': ((('countryName', 'CH'),), (('stateOrProvinceName', 'BE'),), (('localityName', 'Worblaufen'),), (('organizationName', 'Swisscom (Schweiz) AG'),), (('commonName', 'www.swisscom.com'),)), 'issuer': ((('countryName', 'CH'),), (('organizationName', 'SwissSign AG'),), (('commonName', 'SwissSign RSA TLS OV ICA 2021 - 1'),)), 'version': 3, 'serialNumber': '29BB185B451904A2180BB4435080333ECB84A57E'...} 
          # 
          # ->cert strucutre: dictionary(key: tuples(tuples(tuples(key, values))), key: string, ...)
          
          for keys, values in zip(cert.keys(), cert.values()):
            # read out the tuples in a specified order
            if str(type(values))!="<class 'tuple'>":
              writeInfo+="\n".join([f"{keys}: {values}"])
            
            # read out the subject information
            elif keys=="subject": 
              
              # show:
              # main information
              #      subinformation
              writeInfo+="\n".join([f"{keys}:", *[f"\t{keyValue[0][0]}: {keyValue[0][1]}" for keyValue in values]])
            
            elif keys=="subjectAltName": 
              # read out the subjectAltName information
              writeInfo+="\n".join([f"{keys} (SAN):", *[f"\t{keyValue[0]}: {keyValue[1]}" for keyValue in values]])
            
            elif keys=="caIssuers": 
              # read out the certificate authority issuer information
              writeInfo+="\n".join([f"{keys}:", *[f"\t{value}" for value in values]])
              
            writeInfo+="\n"

          
          # read out information about server peer name
          writeInfo+="\n".join(["peerName: ", *[f"\t{peerKey}: {peerValue}" for peerKey, peerValue in zip(["ip", "port"], ssock.getpeername())]])
  return writeInfo

def GetServerCertificate(hostname, verbose,  path=f"{ROOT_DIR}/data", **kwargs):
  # print out additional information about the task
  if getBoolean(verbose): print("run GetServerCertificate"); print(f"path: {path}")

  # create a new file with hostname as a prefix
  f = open(f"{path}/{str(hostname).replace('.', '_')}_cert.der",'wb')
  
  # read out the certificate
  # Retrieve the certificate from the server at the specified address, and return it as a PEM-encoded string (Base64 ASCII encoding)
  cert = ssl.get_server_certificate((hostname, port))
  
  # dave it as .der file into the path provided
  f.write(ssl.PEM_cert_to_DER_cert(cert))
  
  # write information out to stdout
  writeInfo = f"**************\n CERTIFICATE OF {str(hostname).upper()}\n  {cert}\n**************\n"
  return writeInfo

def GetAPIInfo(verbose, **kwargs):
  # print out additional information
  if getBoolean(verbose): print("run GetServerCertificate")

  # fetch the information about cipher security from online DB
  response = requests.get("https://ciphersuite.info/api/cs")
  
  # check if get request was successful
  if getBoolean(verbose):
    if response.status_code == 200:
      print("The request was a success!")
    elif response.status_code == 404:
      print("Result not found!")
  return response.json()