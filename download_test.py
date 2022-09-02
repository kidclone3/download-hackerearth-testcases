from bs4 import BeautifulSoup
import re 
import wget
import os

with open('example.html', 'r') as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    arr = []
    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        # print(link.get('href'))
        arr.append(link.get('href').split('?')[0])

    # print(arr)
    os.mkdir("data")
    n = len(arr)//2
    for i in range(n):
        url1 = arr[i*2]
        url2 = arr[i*2+1]
        print(url1, url2)
        wget.download(url1, f'data/i{i+1:02d}.txt')
        wget.download(url2, f'data/o{i+1:02d}.txt')
    print()
    print("DONE!!!")
# https://he-s3.s3.amazonaws.com/media/hackathon/march-circuits-22/problems/0fc497feab7911ec.txt