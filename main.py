from __future__ import print_function

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import datetime  
import time

import json
import requests

from web3 import Web3, HTTPProvider, EthereumTesterProvider
from ens import ENS


import sha3

import base64


open('firebase.json')

cred = credentials.Certificate('firebase.json')


databaseurl = ""

firebase_admin.initialize_app(cred, {'databaseURL': databaseurl})

def wl(tokenid, name, epoch_time, ftime):
  ref = db.reference(f"/")
  ref.update({tokenid:{'epoch':epoch_time, 'timestamp': ftime, "name": name}})
  return


def getDate(tokenid, name):

  epoch_time = "1234567"
  ftime = "nulltime"
  
  response = requests.get('https://metadata.ens.domains/mainnet/0x57f1887a8bf19b14fc0df6fd9b2acc9af147ea85/' + str(tokenid))
  jresp = response.json()

  if "attributes" in jresp:
    epoch_time=jresp['attributes'][3]['value']
    epoch_time = int(epoch_time)/1000

    ftime = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch_time))
    ftime = str(ftime)

  wl(tokenid, name, epoch_time, ftime)

  return

def getToken(ensName):

    str_1_encoded = bytes(ensName,'UTF-8')


    k = sha3.keccak_256()
    k.update(str_1_encoded)
    j = k.hexdigest()

    b = int(j,16)

    name = str(ensName) + '.eth'

    getDate(b, name)

    return(b)


for i in range(5000,7500):
    print(i)
    time.sleep(.02)
    getToken(str(i))
