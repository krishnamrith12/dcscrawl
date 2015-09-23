import os
from bs4 import BeautifulSoup
pathname = "/home/amrith/segmentation/htmls"

dirRange = range(1,7)
print dirRange
verbDoc = open('verbDoc.csv','w')
verbDoc2 = open('verbDoc2.csv','w')

for item in dirRange:
    pathname = pathname + str(item)+'/'
    for filename in os.listdir(pathname):
        soup = BeautifulSoup(open(pathname+filename).read())
        a = soup.find("div",{"id":"content"})
        finalText = a.h1.text.encode('utf-8').replace('Details for ','').split('(')[0].strip()
        print finalText
        textVerbs = soup.find("div",{"id":"textVerbs"})
        if textVerbs:
            for trs in textVerbs.findAll('tr'):
                verbMain = ''
                for tds in trs:
                    if tds.strong:
                        print tds.text
                        verbMain = tds.text
                    else:
                        tdsText = tds.text.encode('utf-8')
                        anchors = tds.findAll('a')
                        for item in anchors:
                            print item.text.encode('utf-8'),item['href'].split('IDVerbalform=')[-1].split('&')[0]
                            print >>verbDoc,filename.split('.')[0],','+verbMain+',',item.text.encode('utf-8'),','+item['href'].split('IDVerbalform=')[-1].split('&')[0]

                        if '[' in tdsText:
                            for item in tdsText.split('['):
                                stuff = item.split(']')
                                print stuff[0]
                                print>>verbDoc2,filename.split('.')[0],','+verbMain+','+stuff[0]

        else:
            print 'nothing here'
verbDoc.close()
verbDoc2.close()
