import pandas as pd
import os

from utils.exportProbe import ExportProbe

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def CombineDataFrame(respJson):
  dfAnalysis = pd.read_csv(f"{ROOT_DIR}/data/testssl.csv").set_index("id").assign(ianaRfcName = lambda x: x.finding.apply(lambda y: y.split(" ")[-1]))

  print("compared ciphers of server:\n")
  dfApi = pd.DataFrame([item_i[list(item_i.keys())[0]] for item_i in respJson["ciphersuites"]], index=[list(item_i.keys())[0] for item_i in respJson["ciphersuites"]]).assign(ianaRfcName=lambda x: x.index.values).reset_index(drop=True)

  dfAnalysis.dropna(axis=1, inplace=True)
  dfApi.dropna(axis=1, inplace=True)


  dfm = dfAnalysis.merge(dfApi, how="inner", on="ianaRfcName").reset_index(drop=True).fillna({k: "notFound" for k in ["security"]})[["ianaRfcName", "security", "tls_version", "enc_algorithm", "hash_algorithm"]]

  # ExportProbe([dfm, dfAnalysis, dfApi])
  return dfm