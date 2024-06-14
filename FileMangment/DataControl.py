import csv
import json

import os

from datetime import datetime

class DataManger:
    def readIndex(self):

        if not os.path.isfile( self.indexPath):
            with open( self.indexPath, "x") as st:
                pass
            self.IndexData = dict()
        elif os.path.getsize(self.indexPath) != 0:
            index = open( self.indexPath, "r")
            self.IndexData = json.loads(index.read())
            index.close()
        else :
            self.IndexData = dict()


    def __init__(self, indexPath:str=None, AllawIndex=True,):
        # print("s", AllawIndex and (indexPath is None))
        # print("s", AllawIndex )
        # print("s", (indexPath is None))
        self.SetUpFolderPath = os.path.join(indexPath, "SetUpFolder")
        os.makedirs(self.SetUpFolderPath, exist_ok=True)
        self.AllawIndex =AllawIndex
        if self.AllawIndex :
            if indexPath is None:
                raise "index path is requered"
            else :
                #index Set Up
                self.indexPath = os.path.join(self.SetUpFolderPath,'indexInfo.json')
                self.readIndex()



        # print(self.indexPath )



    def insertIndex(self):
        with open(self.indexPath, "w") as index:
            json.dump(self.IndexData, index)

    def IndexSearch(self, index):
        if not self.AllawIndex:
            raise "set AllawIndex attribute to True to use this feature"
        if self.IndexData.get(index, True):
            return False
        return True
    def IndexSearchAndWirte(self, index):
        if not self.AllawIndex:
            raise "set AllawIndex attribute to True to use this feature"

        if self.IndexData.get(index, True):
            self.IndexData[index] = None
            self.insertIndex()
            return False
        return True


    def DataTiming(self, sep:str ="|")->"DateFormate 'sip' TimeFormate":
        current_datetime = datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()
        return str(current_date) + sep + str(current_time)
