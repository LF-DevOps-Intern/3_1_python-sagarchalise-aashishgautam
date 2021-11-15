 
import subprocess
import argparse

# getting arguments from command
parser = argparse.ArgumentParser()
parser.add_argument("--env_name", help="environment name to create.",type=str, required=True)
parser.add_argument("--URL", help="URL from is content is to be extracted",type=str,required=True)
parser.add_argument("--Http_Server", help="flag status; set or reset ",type=str, default="set")
args = parser.parse_args()


env_name = args.env_name
url = args.URL
flag_status = args.Http_Server

cmd1= "virtualenv"+ " " + env_name
mypath = "./"+env_name+ "/Scripts/python"

#create environment and install dependencies. 
subprocess.run(cmd1)
subprocess.call([mypath,'-m','pip', 'install', 'requests' ])

#invoke another script
subprocess.call([mypath,'secondary.py',url,flag_status])

