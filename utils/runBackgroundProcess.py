import subprocess as sp
import os

from utils.parseArgs import getBoolean
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def RunBackgroundProcess(hostname,verbose, *args, **kwargs):
  if getBoolean(verbose): print("run RunBackgroundProcess")
  if os.path.exists(f"{ROOT_DIR}/data/testssl.csv"):
    os.remove(f"{ROOT_DIR}/data/testssl.csv")
  sp.run(["testssl" " -e" " --quiet" " --csvfile"  f" {ROOT_DIR}/data/testssl.csv"  f" {hostname}" f" >> /dev/null 2>&1"], shell = True)
  