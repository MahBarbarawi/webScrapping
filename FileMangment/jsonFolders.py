import json
import os

import time
from  FileMangment.DataControl import DataManger

class JsonType(DataManger):

    def __init__(self
                 , FilePath:str
                 , FilesNamingType:str= "index"
                 , AllawIndex:bool= False
                 ,
                 ):

        if FilesNamingType not  in ["time", 'index', 'default']:
            raise "Enter one of the Values --['time' ,'index','default']"
        if FilePath is None:
            raise "NO path is declared"

        super().__init__(AllawIndex= AllawIndex,
                         indexPath=FilePath,)
        # self.AllawIndex=AllawIndex
        self.FilesNamingType = FilesNamingType

        self.FilePath =os.path.join(FilePath, "DataLocation")
        os.makedirs(self.FilePath, exist_ok=True)
        self.rangedData=0

    def ColllectRows(self):
        pass

    def writeROWS(self):
        pass

    def fileNaming(self):
        if self.FilesNamingType== 'index':
            pass


    def writeRow(self,Data:dict):

        if self.FilesNamingType== 'index':
            if not Data.get('index',False):
                print (Data)
                raise 'Data Have no column Called index'
            path=  os.path.join(self.FilePath,str(Data['index'])+".json")

        if self.FilesNamingType == 'default':
            path=  os.path.join(self.FilePath,str(self.rangedData))
            self.rangedData+=1

        if self.FilesNamingType == 'time':
            path = os.path.join(self.FilePath,self.DataTiming() )


        with open(path, 'w') as f:
            json.dump(Data, f)
