from bs4 import BeautifulSoup
import re 
import wget
import os
import shutil

filename = input("File name = ")
print(filename)

with open('example.html', 'r') as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')
    input = [tag.get('href').split('?')[0] for tag in soup.find_all('a', text = re.compile("Input \#.*"))]
    output =[tag.get('href').split('?')[0] for tag in soup.find_all('a', title = "Correct output for given output")]
    print(input)
    print(output)
    
    if (len(input) != len(output)):
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
    print("COMPRESS DONE!!!")
# https://he-s3.s3.amazonaws.com/media/hackathon/march-circuits-22/problems/0fc497feab7911ec.txt