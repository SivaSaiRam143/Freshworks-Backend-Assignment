import main as datastore 
# importing the datastore

datastore.create("key1",10)
#Creating key1 without TTL

datastore.create("key2",20,2400) 
#creating key2 with TTL

datastore.read("key1")
#value for key1 in the datastore is returned

datastore.read("key2")
#value for key2 in the datastore is returned and if the TTL expires ERROR will be returned

datastore.create("key1",50)
#As the key1 is already present in the datastore error will be returned
datastore.delete("key1")
#data for key1 in the datastore will be removed

#Code for using multiple threads
thread1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
thread1.start()
thread1.sleep()
thread2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
thread2.start()
thread2.sleep()
#two threads were used here
