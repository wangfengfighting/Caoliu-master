# coding: utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import os

def DownloadFiles(url, targetPath):
    # Create directories if not exist
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    # Get links
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"}
    req = urllib2.Request(url, headers=headers)
    content = urllib2.urlopen(req)
    content = content.read()
    soup = BeautifulSoup(content)
    fileList = soup.find_all('a', href=re.compile('.*.jpeg'))
    # Download
    for fileLink in fileList:
        try:
            print("Downloading " + fileLink.string + "...")
            urllib.urlretrieve(url+fileLink.attrs['href'], targetPath + fileLink.string)
        except Exception, e:
            print e
    print("Task done!")

if __name__ == '__main__':
    url = 'http://www.cl529.com/htm_data/16/1512/1775897.html/'
    targetPath = "D:\\PythonDownloads\\"
    DownloadFiles(url, targetPath)