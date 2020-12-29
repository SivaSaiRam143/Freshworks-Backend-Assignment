import threading 
from threading import*
import time

datastore={}

def create(key,val,timeout=0):
    if key in datastore:
        print("ERROR: Key provided is already present in the datastore")
    else:
        if(key.isalpha()):
            if len(datastore)<(1024*1020*1024) and val<=(16*1024*1024): #checking size of datastore < 1 GB and value  is < 16 KB
                if timeout==0:
                    t=[val,timeout]
                else:
                    t=[val,time.time()+timeout]
                if len(key)<=32: #key< 32chars
                    datastore[key]=t
            else:
                print("ERROR: Memory Limit Exceeded!! ")#ERROR: Memory Limit Violation
        else:
            print("ERROR: Invalid keyname is entered")

            
def read(key):
    if key not in datastore:
        print("ERROR: Key not found in datastore")
    else:
        temp=datastore[key]
        if temp[1]!=0:
            if time.time()<temp[1]: 
                s=str(key)+":"+str(temp[0])
                return s
            else:
                print("ERROR: TTL expired") 
        else:
            s=str(key)+":"+str(temp[0])
            return s

        
def delete(key):
    if key not in datastore:
        print("ERROR: Key not found")
    else:
        temp=datastore[key]
        if temp[1]!=0:
            if time.time()<temp[1]:
                del datastore[key]
                print("Key is removed")
            else:
                print("ERROR: TTL expired")
        else:
            del datastore[key]
            print("Key deleted")
