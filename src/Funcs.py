import pandas as pd
import seaborn as sns

def prePrcssPhInfo(df):
    # shcode,time to String Type
    df['shcode'] = df['shcode'].astype(str)
    # shcode,time 6szie Fix
    df['shcode'] = df['shcode'].str.pad(width=6, side='left', fillchar='0')

    return df
    # dfPhInfo['time'] = dfPhInfo['time'].astype(str)
    # dfPhInfo['time'] = dfPhInfo['time'].str.pad(width=6, side='left', fillchar='0')

def readCSV_PH(dateString):
    # Read PH CSV
    dfPhInfo = pd.read_csv("../CSV/" + dateString + "/" + dateString + "_PH_.csv"
                           , encoding='utf-8'
                           , index_col='time')

    # shcode,time to String Type
    dfPhInfo['shcode'] = dfPhInfo['shcode'].astype(str)
    # dfPhInfo['time'] = dfPhInfo['time'].astype(str)

    # shcode,time 6szie Fix
    dfPhInfo['shcode'] = dfPhInfo['shcode'].str.pad(width=6, side='left', fillchar='0')
    # dfPhInfo['time'] = dfPhInfo['time'].str.pad(width=6, side='left', fillchar='0')

    return dfPhInfo

def readCSV_S3(dateString):
    # Read S3 CSV
    dfS3Info = pd.read_csv("../CSV/" + dateString + "/" + dateString + "_S3_.csv"
                           , encoding='utf-8'
                           , index_col='chetime')

    # shcode,chetTime to String Type
    dfS3Info['shcode'] = dfS3Info['shcode'].astype(str)
    # dfS3Info['chetime'] = dfS3Info['chetime'].astype(str)

    # #shcode,chetime 6szie Fix
    dfS3Info['shcode'] = dfS3Info['shcode'].str.pad(width=6, side='left', fillchar='0')
    # dfS3Info['chetime'] = dfS3Info['chetime'].str.pad(width=6, side='left', fillchar='0')

    return dfS3Info

def showClusterMap(df):
    dfCorr = df.corr()
    sns.clustermap(dfCorr
                   , annot=True
                   , cmap='RdYlBu_r'
                   , vmin=-1, vmax=1).fig.suptitle("test")



