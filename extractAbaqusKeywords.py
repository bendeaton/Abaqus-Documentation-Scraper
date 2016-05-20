
from bs4 import BeautifulSoup
import glob


# Inputs
pathToHtmlKeywordDocs = ''


# Initialize lists
keywordList = []
parameterList = []
parameterValueList = []


# Main loop over html files
for fname in glob.glob(pathToHtmlKeywordDocs):
    name = str(fname)

    print "Processing documentation file ", name
    f = open(name)
    soup = BeautifulSoup(f)

    words = soup.find_all('span', attrs={'class': 'abqkeywordnostar'})
    for word in words:
        param = word.string.strip()
        if param not in keywordList:
            keywordList.append(param)

    words = soup.find_all('span', attrs={'class': 'abqparameter'})
    for word in words:
        param = word.string.strip()
        if param not in parameterList:
            parameterList.append(param)

    words = soup.find_all('span', attrs={'class': 'abqparamvalue'})
    for word in words:
        param = word.string.strip()
        if param not in parameterValueList:
            parameterValueList.append(param)


# Write collected list of words to text files
# (Sort by reversed length to avoid short matches
#  overwriting subsets of longer matches)

keywordList.sort(key=len)
keywordList = keywordList[::-1]
out = 'abqkeywordnostar.txt'
Out = open(out, 'w')
for keyword in keywordList:
    outkeyword = str(keyword)
    outkeyword = outkeyword[1:]
    Out.write(outkeyword + '|')

parameterList.sort(key=len)
parameterList = parameterList[::-1]
out = 'abqparameter.txt'
Out = open(out, 'w')
for keyword in parameterList:
    Out.write(str(keyword) + '|')

parameterValueList.sort(key=len)
parameterValueList = parameterValueList[::-1]
out = 'abqparamvalue.txt'
Out = open(out, 'w')
for keyword in parameterValueList:
    Out.write(str(keyword) + '|')

# The end
