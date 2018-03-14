#This part fetches the html of the page with the lyrics on it
import urllib2
f = urllib2.urlopen('https://www.azlyrics.com/lyrics/lilwayne/amilli.html')
html = f.read()

#This part splits all of the html into pseudo 'words'
wordlist = html.split(' ')

#This part locates the bulk of the lyrics inside the html
slicestart = 0
slicefinish = 0
for i in range(len(wordlist)):
    if wordlist[i] == 'that.':
        slicestart = i
    elif wordlist[i] == 'MxM':
        slicefinish = i

#This part filters out all of the line breaks
banlist = ['<br>']
edit = wordlist[slicestart:slicefinish]
edit3 = []
for i in range(len(edit)):
    spl = edit[i].split()
    for e in range(len(spl)):
        edit3.append(spl[e])
edit4 = ' '.join(c for c in edit3 if c not in banlist)

#This part filters any excess breaks that were written as part of the word
edit5 = edit4.replace('<br>', '.')


#This part takes one last final cut to replace any excess html on the ends (divs and such)
finalstart = 0
finalfinish = 0
for i in range(len(edit5)):
    if edit5[i:i+3] == "-->":
        finalstart = i
    if edit5[i:i+4] == "<!--":
        finalfinish = i
finalstart += 3
finalfinish -= 1
finaledit = edit5[finalstart:finalfinish]
finaledit = finaledit.replace('</div>', '')
print finaledit

#This writes the cleaned up lyrics to a new text file line
with open('Amilli.txt', 'w') as tf:
    tf.write(finaledit)
