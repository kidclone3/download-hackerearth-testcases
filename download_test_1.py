from bs4 import BeautifulSoup
import re 
import wget
import os
import shutil
import pync

# filename = input("File name = ")
# print(filename)

with open('example.html', 'r') as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')
    
    # get filename from div tag in body.
    filename = soup.find_all('div', 'title')[0].string

    # get testcases links from <a> tag in tbody.
    input = [tag.get('href').split('?')[0] for tag in soup.find_all('a', text = re.compile("Input .*\#.*"))]
    output =[tag.get('href').split('?')[0] for tag in soup.find_all('a', title = "Correct output for given output")]

    # printing process just assure getting link is good.
    print(input)
    print(output)
    
    # Simple exception to prevent making folder and file if download problem appear.
    if len(input) != len(output) or len(input) == 0:
        raise Exception("Input and output files have problem!")

    if len(filename) == 0:
        filename = "data"

    os.mkdir(f'downloaded/{filename}')    
    
    n = len(input)
    for i in range(n):
        url1 = input[i]
        url2 = output[i]
        print(url1, url2)
        
        wget.download(url1, f'downloaded/{filename}/i{i+1:02d}.txt')
        wget.download(url2, f'downloaded/{filename}/o{i+1:02d}.txt')
    print()
    print("DONE!!!")
    shutil.make_archive(f'downloaded/{filename}', 'zip', f'downloaded/{filename}')
    pync.notify("COMPRESS DONE!!!")
# https://he-s3.s3.amazonaws.com/media/hackathon/march-circuits-22/problems/0fc497feab7911ec.txt