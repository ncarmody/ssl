import argparse
import textwrap
import os

def ParseArgs():
    
  parser = argparse.ArgumentParser(
      description='this script analyzes the SSL connection between you and a server of your choise',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''
      SSL CHECK
      
      -n                 - Custom hostname for ssl check e.g.: -n swisscom.ch
      -p                 - Provide custom path to save cert e.g.: -p /myCert
      -h                 - Print this help summary page. e.g: -h
      -i                 - Get additional Information regarding the ssl connection of server. e.g.: -i
      -c                 - get ciphers of server and compare against https://ciphersuite.info/api/cs regarding connection security. e.g.: -c
      -q                 - Minimize debug messages to terminal. e.g.: -q
      -v                 - verbose output. e.g.: -v
      
        '''))


  parser.add_argument('-n', '--hostname', help='custom hostname for ssl check e.g.: -n swisscom.ch')
  parser.add_argument('-p', '--path', help='provide custom path to save cert e.g.: -p /myCert')
  parser.add_argument('-i', '--info', help='Get additional Information regarding the ssl connection of server. e.g.: -i')
  parser.add_argument('-c', '--compare', help='get ciphers of server and compare against https://ciphersuite.info/api/cs regarding connection security. e.g.: -c')
  parser.add_argument('-q', '--quiet',help='Minimize debug messages to terminal. e.g.: -q')
  parser.add_argument('-v', '--verbose',help='verbose output. e.g.: -v')
  


  args = parser.parse_args()

  return args

def getBoolean(flag):
  return flag.lower() in ('true', '1', 't')