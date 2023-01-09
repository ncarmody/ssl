import pandas as pd
import os

from utils.exportProbe import ExportProbe
# find the absolute path to the root folder
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def CombineDataFrame(respJson):
  
  # get the CSV file of the server ciphers and extract the last info from the finding column
  # ensure the ianaRfcName column for later merge
  dfAnalysis = pd.read_csv(f"{ROOT_DIR}/data/testssl.csv").assign(ianaRfcName = lambda x: x.finding.apply(lambda y: y.split(" ")[-1]))
  
  # bring the JSON from the online DB in the right form for pandas
  # ensure the ianaRfcName column for later merge
  itemList = respJson["ciphersuites"]
  # [{key: {key: value, ...}, key: {key: value, ...}...}]->[{index: {columns: rows, ...},index: {columns: rows, ...}...}]
  # item_i.keys()->dict_keys(['TLS_AES_128_CCM_8_SHA256'])
  # list(item_i.keys())[0]->'TLS_AES_128_CCM_8_SHA256'
  dfApi = pd.DataFrame([item_i[list(item_i.keys())[0]] for item_i in itemList], index=[list(item_i.keys())[0] for item_i in itemList]).assign(ianaRfcName=lambda x: x.index.values)
  
  # drop some cells which have no useful information
  dfAnalysis.dropna(axis=1, inplace=True)
  dfApi.dropna(axis=1, inplace=True)

  # merge online DB on security of ciphers with server ciphers and gain insights into the security of ciphers used by the server
  dfm = dfAnalysis.merge(dfApi, how="inner", on="ianaRfcName").reset_index(drop=True).sort_values("security")[["ianaRfcName", "security", "tls_version", "enc_algorithm", "hash_algorithm"]]

  return dfm