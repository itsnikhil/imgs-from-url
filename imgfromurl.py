import re #for regular expressions
import urllib #make sure u have active internet connnection
import requests
import os, time

#### ADD URL ##### PLEASE ADD A VALID URL WHICH MUST END WITH A FORWARDSLASH /
url = 'http://ncuindia.edu/'
home_url= re.search(r'.+\.\w+',url)

#### EDIT REQUIRED #####
newpath = 'YOUR PATH'+'\src' # FILES WILL BE SAVED IN NEWFOLDER WITH NAME SRC TO YOUR GIVEN PATH


if not os.path.exists(newpath):
    os.makedirs(newpath)

# READING SOURCE CODE
ul = urllib.urlopen(url)

#### EDIT REQUIRED #####
textfile = open('YOUR PATH'+'\data.txt', 'w')

matches_html = []
matches_html2 = []
matches_css = []
matches_css2 = []
#for line in textfile:
# FINDING .JPG & .PNG FILES FROM THE SOURCE CODE AND MAKING LIST OF IT
for line in ul:
    matches_html += re.findall(r'src=".+.jpg"',line)
    matches_html2 += re.findall(r'src=".+.png"',line)
    #matches_css += re.findall(r'background: url(.+.jpg)',line)
    #matches_css += re.findall(r'background: url(.+.png)',line)
    #matches_css2 += re.findall(r'background:url(.+.jpg)',line)
    #matches_css2 += re.findall(r'background:url(.+.png)',line)

# SUM TOTAL IMAGES FOUND
matches = len(matches_css2)+len(matches_css)+len(matches_html)+len(matches_html2)
print(str(matches) + ' image(s) found, initiating download...')

# HTML IMAGES
i=1
#JPG
for img_html in matches_html:
	# OPTIMISING A LIL BIT
	check = re.search(home_url.group(),img_html)
	if check:
		print('Trying on: '+img_html[5:-1]+'.jpg')
		# DOWNLOADING IMAGE
		request = requests.get(img_html[5:-5]+'.jpg')
		if request.status_code == 200:
			print('Success!')
			urllib.urlretrieve(img_html[5:-5]+'.jpg','src/img'+str(i)+'.jpg')
			textfile.write('Success: '+img_html[5:-5]+'.jpg'+'\n')
		else:
			print('Image does not exist!')
			i = int(i)-1
			textfile.write('Failed: '+img_html[5:-5]+'.jpg'+'\n')
		i = int(i)+1
	else:
		print('Trying on: '+url+img_html[5:-5]+'.jpg')
		# DOWNLOADING IMAGE
		request = requests.get(url+img_html[5:-5]+'.jpg')
		if request.status_code == 200:
			print('Success!')
			urllib.urlretrieve(url+img_html[5:-5]+'.jpg','src/img'+str(i)+'.jpg')
			textfile.write('Success: '+url+img_html[5:-5]+'.jpg'+'\n')
		else:
			print('Image does not exist!')
			i = int(i)-1
			textfile.write('Failed: '+url+img_html[5:-5]+'.jpg'+'\n')
		i = int(i)+1

#PNG

for img_html in matches_html2:
	# OPTIMISING A LIL BIT
	check = re.search(home_url.group(),img_html)
	if check:
		print('Trying on: '+img_html[5:-1]+'.png')
		# DOWNLOADING IMAGE
		request = requests.get(img_html[5:-5]+'.png')
		if request.status_code == 200:
			print('Success!')
			urllib.urlretrieve(img_html[5:-5]+'.png','src/img'+str(i)+'.png')
			textfile.write('Success: '+img_html[5:-5]+'.png'+'\n')
		else:
			print('Image does not exist!')
			i = int(i)-1
			textfile.write('Failed: '+img_html[5:-5]+'.png'+'\n')
		i = int(i)+1
	else:
		print('Trying on: '+url+img_html[5:-5]+'.png')
		# DOWNLOADING IMAGE
		request = requests.get(url+img_html[5:-5]+'.png')
		if request.status_code == 200:
			print('Success!')
			urllib.urlretrieve(url+img_html[5:-5]+'.png','src/img'+str(i)+'.png')
			textfile.write('Success: '+url+img_html[5:-5]+'.png'+'\n')
		else:
			print('Image does not exist!')
			i = int(i)-1
			textfile.write('Failed: '+url+img_html[5:-5]+'.png'+'\n')
		i = int(i)+1
'''
# CSS IMAGES

# TOO LAZY TO FIX IMAGES HIDDEN INSIDE CSS :/
for img_css in matches_css:
	#OPTIMISING A LIL BIT
	check = re.search(home_url.group(),img_css)
	if check:
		print(img_css[16:-1])
		# DOWNLOADING IMAGE
		#urllib.urlretrieve(img_css[16:-1],'img'+str(i)+'.jpg')
		i = int(i)+1
	else:
		print(url+img_css[16:-1])
		# DOWNLOADING IMAGE
		#urllib.urlretrieve(url+img_css[16:-1],'img'+str(i)+'.jpg')
		i = int(i)+1
# CSS DIFFERENT SYNTAX
for img_css2 in matches_css2:
	#OPTIMISING A LIL BIT
	check = re.search(home_url.group(),img_css2)
	if check:
		print(img_css2[15:-1])
		# DOWNLOADING IMAGE
		#urllib.urlretrieve(img_css2[15:-1],'img'+str(i)+'.jpg')
		i = int(i)+1
	else:
		print(url+img_css2[15:-1])
		# DOWNLOADING IMAGE
		#urllib.urlretrieve(url+img_css2[15:-1],'img'+str(i)+'.jpg')
		i = int(i)+1
'''
i = int(i)-1

print('Success = '+ str(i)+' & Failed = '+str(matches-i))
print('download completed!')

textfile.close()
ul.close()

time.sleep(3)