import numpy as np
import pandas as pd
import random
import pickle
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import csv


key_data= np.genfromtxt("/Users/mahalakshmimaddu/Downloads/Key_data.txt", delimiter=",", dtype=str)
pic = ['Data-2003-1000000', 'Data-2003-2000000',  'Data-2004-1000000', 'Data-2004-2000000', 'Data-2005-1000000', 'Data-2005-2000000']
##pictest = ['Data-2006-1000000','Data-2006-2000000']
conn = S3Connection(key_data[0], key_data[1])
bucket = conn.get_bucket('sdmairlines')
k = Key(bucket)
theta = []



def typeconvert(findata):
    dfMaster = pd.DataFrame(np.array(findata))

    dfMaster.fillna(0, inplace=True)
    dfMaster[0] = 1
    dfMaster[1] = dfMaster[1].astype('int')
    dfMaster[2] = dfMaster[2].astype('int')
    dfMaster[3] = dfMaster[3].astype('int')
    dfMaster[4] = dfMaster[4].astype('int')
    dfMaster[5] = dfMaster[5].astype('int')
    dfMaster[6] = dfMaster[6].astype('int')
    dfMaster[7] = dfMaster[7].astype('int')
    dfMaster[8] = dfMaster[8].astype('int')
    dfMaster[9] = dfMaster[9].astype('int')

    findata = dfMaster.values
    return findata


for el in pic:
    k.key = el
    k.get_contents_to_filename(el)
    findata = pickle.load(open(el, 'rb'))
    findata = typeconvert(findata)


################## Graphs,....


















