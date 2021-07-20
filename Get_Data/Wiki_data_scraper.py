import re , requests, os
from sys import dont_write_bytecode
os.system('clear')

from bs4 import BeautifulSoup

# this will be our starting URL.
urls = open('/home/tanmay/Desktop/NLP Workflow/Working with a big data/new_links.txt','r')

for url in urls.readlines():
    cleanUrl = url.strip()
    r = requests.get(cleanUrl)
    #type(r) ==> <class 'requests.models.Response'>
    # r ==> <Response [200]>
    # here Response is the actual html content.

    htmlContent = r.content
    soup= BeautifulSoup(htmlContent, 'html.parser')

    abstract1 = re.findall('(?<= href=\")/wiki/.*(?=\" title=")',str(soup))
    #this abstract1 will be used for future use
    abstract2 = re.findall("(?<=<p>).*(?=</)",str(soup))
    
    rawText =''
    for text in str(abstract2):
        rawText=rawText + text

    # This is to clean all the tags that are comming in the big data
    def clean(text):
        trim = list(text[1:-1]) # in order to remove first and last brackets
        inside = False #tanmay <afdga >
        newText=''
        for i in range(len(trim)):
            if trim[i] is '<':
                inside = True
            elif inside and trim[i][-1]:
                if trim[i] is '>':
                    inside = False
            else:
                newText=newText+trim[i]
        #all the internal tags are removed.
        newText2 =''
        trim = list(newText)
        for i in range(len(trim)):
            if trim[i] is '[':
                inside = True
            elif inside and trim[i][-1]:
                if trim[i] is ']':
                    inside = False
            else:
                newText2=newText2+trim[i]
        #all the internal references are also removed now.
        return newText2

    cleanText = clean(rawText)

    print(cleanText[:10])
    
    file = open('/home/tanmay/Desktop/NLP Workflow/Working with a big data/collected_data.txt','a')
    if cleanText is not '':
        file.write(cleanText+'\n\n')
    file.flush()
    file.close()
urls.close()
print('\n\n\n\nDone!!!')