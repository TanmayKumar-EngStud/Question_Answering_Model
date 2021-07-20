import re , requests, os
from sys import dont_write_bytecode
os.system('clear')

from bs4 import BeautifulSoup
# this will be our starting URL.
URLs = open('/home/tanmay/Desktop/NLP Workflow/Working with a big data/new_links.txt','r')
i=0
for urls in URLs.readlines():
    urls = urls.strip()
    r = requests.get(urls)
    #type(r) ==> <class 'requests.models.Response'>
    # r ==> <Response [200]>
    # here Response is the actual html content.

    htmlContent = r.content
    soup= BeautifulSoup(htmlContent, 'html.parser')


    linkadder = open('/home/tanmay/Desktop/NLP Workflow/Working with a big data/new_links.txt','a')
    abstract1 = re.findall('(?<=<a href=\")/wiki/[a-zA-Z_]*(?=")',str(soup))
    #Now it is working fine

    i += 1
    for link in abstract1:
        #if re.search('\'',link) is None:
        verifier = open('/home/tanmay/Desktop/NLP Workflow/Working with a big data/new_links.txt','r')
        print(link)
        if link not in verifier.read():
            linkadder.write('https://en.wikipedia.org'+link+'\n')
            # In order to not repeat the same process again and again...
        verifier.close()
    print("\n\ndone!! "+str(i))

print('\n\n\n\nDone all!!')