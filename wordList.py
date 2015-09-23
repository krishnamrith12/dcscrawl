import os
from bs4 import BeautifulSoup
pathname = "/home/amrith/segmentation/htmls"

dirRange = range(1,7)
print dirRange
verbDoc = open('wordList.csv','w')

for item in dirRange:
    pathname = pathname + str(item)+'/'
    for filename in os.listdir(pathname):
        soup = BeautifulSoup(open(pathname+filename).read())
        a = soup.find("div",{"id":"content"})
        print >> verbDoc,filename.split('.')[0],a.h1.text.encode('utf-8').split('Details for ')[1].split('(')[0]

verbDoc.close()
