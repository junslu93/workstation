# -*- coding:utf-8 -*-
        #bb[0]:股票名  bb[1]:今日开盘价    bb[2]：昨日收盘价    bb[3]:当前价格   bb[4]:今日最高价    bb[5]:今日最低价
        #bb[6]:买一报价 bb[7]:卖一报价     bb[8]:成交股票数/100 bb[9]:成交金额/w bb[10]:买一申请股数 bb[11]:买一报价
        #bb[12]:买二股数 bb[13]:买二报价   bb[14]:买三股数      bb[15]:买三报价  bb[16]:买四申请股数 bb[17]:买四报价
        #bb[18]:买五股数 bb[19]:买五报价   bb[20]:卖一股数      bb[21]:卖一报价  bb[22]:卖二申请股数 bb[23]:卖二报价
        #bb[24]:卖三股数 bb[25]:卖三报价   bb[26]:卖四股数      bb[27]:卖四报价  bb[28]:卖五股数     bb[29]:卖五报价
        #bb[30]:日期     bb[31]:时间     bb[8]:不知道
 
import urllib2
import time
from stockSort import stocksort
stockDict={}
stockTimeList=[]
 
class updateData(object):
    def __init__(self):
        self.url = 'http://hq.sinajs.cn/list='
 
    def getData(self,stockID):
        dataList={}
        try:
            request = urllib2.Request(self.url+str(stockID))
            response = urllib2.urlopen(request)
            contents = response.read()
 
            for content in str(contents).splitlines():
                temp=(content).split(",")
                if float(temp[1])!=0:
                    hehe=str((float(temp[3])-float(temp[2]))/float(temp[1])*100)
                    dataList[str(temp[0][11:19])]=[hehe,temp[31]]
                else:
                    dataList[str(temp[0][11:19])]=[0,temp[31]]
            return dataList
 
        except urllib2.URLError, e:
            print "BadxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxBad"
 
    def getPart(self,stockID):
 
        bb=self.getData(stockID)
        #print bb
 
        #print 'a'+str(len(bb))
        if len(bb)>0:
            for key in bb:
                stockDict[key].append(bb[key][0])
 
            stockTimeList.append(bb[key][1])
 
if __name__=='__main__':
 
    ttjj=updateData()
    ff=open("stockCodeList.txt","r")
    #print ff.readline().split(",")
 
    nameA=""
    count=0
    dataTemp=ff.readline().strip(",").split(",")
    ff.close()
    for  stockI in dataTemp:
        stockDict[stockI]=[]
        count+=1
        if count<800:
            nameA+=stockI+","
        else:
            ttjj.getPart(nameA.strip(","))
            nameA=""
            count=0
    ttjj.getPart(nameA.strip(","))
 
    print stockDict
    while(True):
        time.sleep(1)
        nameA=""
        count=0
        for  stockI in dataTemp:
            count+=1
            if count<800:
                nameA+=stockI+","
            else:
                ttjj.getPart(nameA.strip(","))
                nameA=""
                count=0
        ttjj.getPart(nameA.strip(","))
 
        #print stockDict
        xx=stocksort(stockDict)
        print xx.getSort()[0:10]
class stocksort(object):
    def __init__(self,stockDict):
        self.stockDict=stockDict
 
    def getSort(self):
        sortList={}
 
        for key in self.stockDict:
            if len(self.stockDict[key])!=0:
                sortList[key]=self.stockDict[key][-1]
 
        return sorted(sortList.items(), lambda x, y: cmp(x[1], y[1]),reverse=True)
