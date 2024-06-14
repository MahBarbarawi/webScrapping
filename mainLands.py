import multiprocessing as mp
import time

from FileMangment.jsonFolders import JsonType
from  webScrappingTemplets.landsTemplets import  postLinks,getData,extractID

OpenSouqDataModel =JsonType(FilePath="I:\pytron\DataLands",
                            AllawIndex=True)
#
def DataWrite(link):
    Data = getData(link)
    OpenSouqDataModel.writeRow(Data)
if __name__ == '__main__':
    start_time = time.perf_counter()
    counter=0
    pool = mp.Pool(6)
    for i in range(0,1200):
        print("pageNumber :",i)
        time.sleep(1)
        linksTopost = postLinks("https://jo.opensooq.com/en/real-estate-for-sale/lands-for-sale?search=true&page={}".format(i) )
        jobs = []
        for itemsNum in range(len(linksTopost)):
            # print(linksTopost[itemsNum])
            ITEMS=linksTopost[itemsNum]
            index ,rest = extractID(ITEMS)
            if OpenSouqDataModel.IndexSearchAndWirte(index):
                print('mistake')
                continue

            counter += 1
            print(counter)
            job = pool.apply_async(DataWrite, (ITEMS,))

            jobs.append(job)
            if len(jobs)==4 or itemsNum-len(linksTopost)==0:
                for job in jobs:
                    job.get()
                jobs = []
                time.sleep(2)

        time.sleep(2)

    pool.close()
    pool.join()
    finish_time = time.perf_counter()
    print(f"1---Program finished in {finish_time - start_time} seconds")
