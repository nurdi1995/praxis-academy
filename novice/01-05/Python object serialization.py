#Persistence of External Objects

#Simple example presenting how persistent ID can be use to pickle
#external object bt reference

import pickle
import sqlite3
from collections import namedtuple

#Simple class representing a record in out database
MemoRecord = namedtuple("MemoRecord","key, task")

class DBPpickler(pickle.Pickler):

    def persistent_id(self, obj):
        #Persistent ID
        if isinstance(obj,MemoRecord):
            return ("Memorecord", obj.key)
        else:
            return None

class  DBUnpickler(pickle.Unpickler):

    def __init__(self, file, connection):
        super().__init__(file)
        self.connection = connection

    def persistent_load(self, pid):

        cursor = self.connection.cursor()
        type_tag, key_id = pid
        if type_tag == "MemoRecord":
            cursor.execute("Select * FROM memos Where key=?", (str(key_id)))
            key, task = cursor.fetchone()
            return MemoRecord(key, task)
        else:
             # Always raises an error if you cannot return the correct object.
            # Otherwise, the unpickler will think None is the object referenced
            # by the persistent ID.
            raise pickle.UnpicklingError("unsupported persistent object")

def main():
    import io 
    import pprint

    #Initialize and populate our database.
    conn=sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE memos(key INTEGER PRIMARY KEY, task TEXT)")
    tasks = (
        'give food to fish',
        'prepare group meeting',
        'fight with a zebra',
        )
    for tasks in tasks:
        cursor.execute("INSERT INTO memos VALUES(NULL,?)",(task,))
        memos = [MemoRecord(key, task) for key, task in cursor]
        #Save the record using out custom DBpickler
        file = io.BytesIO()
        DBPpickler(file).dump(memos) 

        #print("pickled records:")
        pprint.pprint(memos)

        #update a record, just for good measure.
        cursor.execute("UPDATE memos SET task='learn italian' WHERE key=1")

        #load the records from the pickle data stream.
        file.seek(0)
        memos = DBPpickler(file, conn).load() 
        pprint.pprint(memos)

    if __name__=='__main__':
        main()



    

        

        