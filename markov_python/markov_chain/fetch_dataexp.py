# This part fetches the html of the page with the lyrics on it
import urllib2

# Test with these 3 songs.
# https://www.azlyrics.com/lyrics/lilwayne/amilli.html
# https://www.azlyrics.com/lyrics/lilwayne/6foot7foot.html
# https://www.azlyrics.com/lyrics/lilwayne/lollipop.html
inp = raw_input('What will your lyrics be? Please enter your url: ')
f = urllib2.urlopen(inp)
html = f.read()

# This part locates the bulk of the lyrics inside the html
slicestart = 0
slicefinish = 0
for i in range(len(html)):
    if html[i:i + 17] == 'Sorry about that.':
        slicestart = i
    elif html[i:i + 19] == '<!-- MxM banner -->':
        slicefinish = i

# This part filters out all of the line breaks
edit = html[slicestart:slicefinish]

banlist = ['<i>', '</i>', '[Hook]', '</div>', '. ', '<br>', 'Sorry about that-->', '[Lil Wayne - Verse 1]',
           '[Cory Gunz]', '>', '[Lil Wayne - Verse 2].', '[4x]', '[2x]', '[Lil Wayne:]', '[3x]', '[Static Major:]',
           'Sorry about that--']
for i in banlist:
    if i == '<br>':
        edit = edit.replace(i, '.')
    else:
        edit = edit.replace(i, '')

# Writes to a textfile
final = raw_input("To what will you write these lyrics?: ")
with open(final, 'w') as tf:
    tf.write(edit)
