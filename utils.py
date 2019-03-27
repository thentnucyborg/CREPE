""" Import fix - check README for documentation """ 
import os,sys,inspect 
__currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, __currentdir[0:__currentdir.find("CREPE")+len("CREPE")])
""" End import fix """

import rpyc
from settings import RPYC_CONFIG
import time

# Waints for and returns a rpyc connection 
# @param port is a port defined in RPCPORT
# @returns an rpyc connection object
class RpycHelper():
    def get_connection(self, name_of_service):
        t = 0.5
        i = 0
        while True:
            if i != 1 and i % 10 == 1:
                print("[CREPE.utils.get_connection] ... still wainting for ", name_of_service, " connection")
            try:
                conn = rpyc.connect("localhost", self.RPCPORTS[name_of_service], config=RPYC_CONFIG)
                print("[CREPE.utils.get_connection] Got the ", name_of_service, " connection! :)")
                return conn
            except:
                if i == 0:
                    print("[CREPE.utils.get_connection] Waiting for a connection to the ", name_of_service, " server") 
                time.sleep(t)
            i += 1

