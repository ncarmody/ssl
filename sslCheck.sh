#!/bin/bash

path="$(pwd)/data"
hostname="swisscom.ch"
quiet=false
compare=false
info=false
verbose=false
while getopts "qcivn:p:h" option; do
	case $option in
		h ) #display help info
			python -c "print('''
      SSL CHECK
      
      -n                 - Custom hostname for ssl check e.g.: -n swisscom.ch
      -p                 - Provide custom path to save cert e.g.: -p /myCert
      -h                 - Print this help summary page. e.g: -h
      -i                 - Get additional Information regarding the ssl connection of server. e.g.: -i
      -c                 - get ciphers of server and compare against https://ciphersuite.info/api/cs regarding connection security. e.g.: -c
      -q                 - Minimize debug messages to terminal. e.g.: -q
      -v                 - verbose output. e.g.: -v

      
        ''')"
			exit;;
		n ) #echo "** n, custom hostname supplied **"
			echo "-n option is: ${OPTARG:- "swisscom.ch"}"
			hostname=${OPTARG:- "swisscom.ch"};;
		p ) #echo "** p, path supplied **"
			echo "-p option is: ${OPTARG:- "./"}"
			path=${OPTARG:- "./"};;
		i ) #echo "** i, path supplied **"
			echo "-i option is: ${OPTARG:- true}"
			info=${OPTARG:- true};;
		c ) #echo "** c, compare supplied **"
			echo "-c option is: ${OPTARG:- true}"
			compare=${OPTARG:- true};;
		q ) #echo "** q, quiet mode supplied **"
			echo "-q option is: ${OPTARG:- true}"
			quiet=${OPTARG:- true};;
      # echo "quiet: $quiet";;
		v ) #echo "** v, verbose mode supplied **"
			echo "-v option is: ${OPTARG:- true}"
			verbose=${OPTARG:- true};;

		* )
      echo "run './sslCheck.sh -h' for additional information"
			exit 1
	esac
done

echo ""

[ -d "$path" ] && ( [ $verbose = true ] && echo "folder does exits" || echo "" ) || { echo "provided folder does not exist!"; exit 1; };

if [ $# -eq 0 ]
then
  ! [ $quiet = true ] && echo "no arguments supplied. default hostname: ${hostname}"
  ! [ $quiet = true ] && echo "for custom hostname run ./analyzeSSL.sh -n <hostname> or run ./analyzeSSL.sh -h for help"
fi

ping google.ch -w 2 -c 1 -q  >> /dev/null 2>&1;

[ $? -ne 0 ] && echo "check your internet connection! you might be disconnected" && exit || ! [ $quiet = true ] && echo "" && echo "internet connection ok" && echo ""

curl -s --head ${hostname} | head -n 1 | grep "HTTP/1.[01] [23]..">> /dev/null 2>&1 && echo "starting main.py" &&  poetry run python main.py -n ${hostname} -p ${path} -q ${quiet} -i ${info} -c ${compare} -v $verbose


