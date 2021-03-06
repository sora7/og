# -*- coding: utf-8 -*-

# ost grab
# version 0.2
# requires python 2.7

from urllib2 import urlopen
from urllib2 import Request
#from threading import Thread
from time import sleep
import re
import os

class OG:
    URL = 'http://tenshi.ru/anime-ost/'
    PARENT_DIR = '/anime-ost/'
    OST_DIR = ''
    
    titlelist = []
    
    TITLENAME = ''
    SAVE_DIR = ''
    
    ##userful lists
    snd_list = []
    img_list = []
    vid_list = []
    txt_list = []
    zip_list = []
    
    def __init__(self):
        pass

    def grab(self):
        count=0
        for titlename in self.titlelist:
            count = count + 1
            print 'LOADING TITLE ', count, ' OF ', len(self.titlelist)
            self.TITLENAME = titlename
            
            self.snd_list = []
            self.img_list = []
            self.vid_list = []
            
            self.SAVE_DIR = ''.join([self.OST_DIR, titlename])
            os.mkdir(self.SAVE_DIR)
            url = ''.join([self.URL, titlename])
            self.find(url)
            download_lst = self.lst_join(self.snd_list, self.img_list, self.vid_list)
            self.download(download_lst)

    def find(self,url):
        headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:16.0) Gecko/20120815 Firefox/16.0'}
        req = Request(url, None, headers)
        url_lines = urlopen(req)
        
        for line in url_lines:
            ##dir
            match = re.search(r'.*alt="\[DIR\]"> <a href="(.*)"', line)
            if match:
                item = match.group(1)
                if not re.search(self.PARENT_DIR,item):
                    dirpath = re.search(''.join([''.join([self.URL, self.TITLENAME]),'(.*)']), ''.join([url, item])).group(1)
                    dirpath = self.fix(dirpath)
                    #print dirpath
                    os.mkdir(''.join([self.SAVE_DIR, dirpath]))
                    #print ''.join([url,item])
                    self.find(''.join([url, item]))
            
            ##sound
            match = re.search(r'.*alt="\[SND\]"> <a href="(.*)"', line)
            if match:
                item = match.group(1)
                if not re.search(self.PARENT_DIR, item):
                    dlitem1 = {}
                    dllk1 = ''.join([url,item])
                    dlpath1 = re.search(''.join([''.join([self.URL, self.TITLENAME]), '(.*)']), dllk1).group(1)
                    dlpath1 = ''.join([self.SAVE_DIR,dlpath1])
                    dlitem1['link'] = dllk1
                    dlitem1['file'] = dlpath1
                    #print dllk1
                    self.snd_list.append(dlitem1)
                    pass
            ##images
            match = re.search(r'.*alt="\[IMG\]"> <a href="(.*)"', line)
            if match:
                item = match.group(1)
                if not re.search(self.PARENT_DIR, item):
                    dlitem2 = {}
                    dllk2 = ''.join([url, item])
                    dlpath2 = re.search(''.join([''.join([self.URL, self.TITLENAME]), '(.*)']), dllk2).group(1)
                    dlpath2 = ''.join([self.SAVE_DIR, dlpath2])
                    dlitem2['link'] = dllk2
                    dlitem2['file'] = dlpath2
                    self.img_list.append(dlitem2)
                    pass
            ##videos
            match = re.search(r'.*alt="\[VID\]"> <a href="(.*)"', line)
            if match:
                item = match.group(1)
                if not re.search(self.PARENT_DIR, item):
                    dlitem3 = {}
                    dllk3 = ''.join([url,item])
                    dlpath3 = re.search(''.join([''.join([self.URL, self.TITLENAME]), '(.*)']), dllk3).group(1)
                    dlpath3 = ''.join([self.SAVE_DIR, dlpath3])
                    dlitem3['link'] = dllk3
                    dlitem3['file'] = dlpath3
                    self.vid_list.append(dlitem3)
                    pass

            ##txt files
            match = re.search(r'.*alt="\[TXT\]"> <a href="(.*)"', line)
            if match:
                item = match.group(1)
                if not re.search(self.PARENT_DIR, item):
                    dlitem4 = {}
                    dllk4 = ''.join([url,item])
                    dlpath4 = re.search(''.join([''.join([self.URL, self.TITLENAME]), '(.*)']), dllk4).group(1)
                    dlpath4 = ''.join([self.SAVE_DIR, dlpath4])
                    dlitem4['link'] = dllk4
                    dlitem4['file'] = dlpath4
                    self.txt_list.append(dlitem4)
                    pass
                
            ##zip archives    
            match = re.search(r'.*alt="\[   \]"> <a href="(.*)"', line)
            if match:
                item = match.group(1)
                if not re.search(self.PARENT_DIR, item):
                    dlitem5 = {}
                    dllk5 = ''.join([url,item])
                    dlpath5 = re.search(''.join([''.join([self.URL, self.TITLENAME]), '(.*)']), dllk5).group(1)
                    dlpath5 = ''.join([self.SAVE_DIR, dlpath5])
                    dlitem5['link'] = dllk5
                    dlitem5['file'] = dlpath5
                    self.zip_list.append(dlitem5)
                    pass
        #print line
        
    def download_file(self,url,path):
        mp3file = urlopen(url)
        output = open(path,'wb')
        output.write(mp3file.read())
        output.close()
####        os.system('wget -P ' + path + ' ' + url)

    def lst_join(self,list1,list2,list3):
        lst=[]
        for i in list1:
            lst.append(i)
        for i in list2:
            lst.append(i)
        for i in list3:
            lst.append(i)
        for i in list4:
            lst.append(i)
        for i in list5:
            lst.append(i)
        
        return lst 

    def download(self,lst):
        count = 0
        for link2load in lst:
            count = count + 1
            print 'downloading file',count,'of',len(lst)
            l = link2load['link']
            link2load['link'] = l.replace('&amp;','&')
            print link2load['link']
            link2load['file'] = self.fix(link2load['file'])
            print link2load['file']
            
##            t1 = Thread(target=self.download_file, args=(link2load['link'],link2load['file']))
##            t1.start()
##            t1.join()
####            lol = link2load['file']
####            lol = lol.replace(' ','\ ')
####            self.download_file(link2load['link'],lol)
            self.download_file(link2load['link'],link2load['file'])
            sleep(1.5)
        
    def fix(self,s):
        a = s
        a = a.replace('&amp;','&')
        a = a.replace('%5b','[')
        a = a.replace('%5d',']')
        a = a.replace('%20',' ')
        return a
    
    def setOSTdir(self, dir_):
        self.OST_DIR = dir_
    
    def add(self, title):
        if (len(title) != 0):
            if (title[-1] != '/'):
                title = title + '/'
            self.titlelist.append(title)

class PathFind(object):
    snd_list = []
    img_list = []
    vid_list = []
    pass
