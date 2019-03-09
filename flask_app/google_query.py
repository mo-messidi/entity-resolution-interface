import time
from optparse import OptionParser

from googlesearch import search
 
##################################################

parser = OptionParser()

#Person identoty
parser.add_option("-f", "--first_name", dest="first_name", help="First Name of person.", default="")
parser.add_option("-l", "--last_name", dest="last_name", help="Last Name of person." , default="")
parser.add_option("-o", "--org", dest="org", help="Organization of person.", default="")
parser.add_option("-p", "--location", dest="location", help="Location of person.", default="")

#Query Parameters
parser.add_option("-t", "--tld", dest="tld", help="Top Level domain ex: com, co.in, co.ru etc", default="com")
parser.add_option("-n", "--num_query", dest="num_query", help="Maxm number of queries", default=100)
parser.add_option("-s", "--stop_query", dest="stop_query", help="Index of the last query you want to fetch from the generator", default=100)
parser.add_option("-d", "--pause_time", dest="pause_time", help="Pause time between consecutive queries, set minm  = 2 to avoid IP blocking by google", default=2)

#Extra filtering option
parser.add_option("-e", "--extra_filter", dest="extra_filter", help="Extra filtering", default=True)
parser.add_option("-w", "--to_file", dest="to_file", help="Will write results to a txt file of given Name", default=None)


(options, args) = parser.parse_args() 

first_name = options.first_name
last_name = options.last_name
org = options.org
location = options.location

tld_in = str(options.tld)
num_query = int(options.num_query)
stop_query = int(options.stop_query)
pause_time = int(options.pause_time)

extra_filter = options.extra_filter

if options.to_file:
	to_file = str(options.to_file) + '.txt'

##################################################

query = first_name + ' ' + last_name + ' ' + org + ' ' + location
print('Given Query : ', query)

urls = []

time_start = time.time()

for j in search(query, tld=tld_in, num=num_query, stop=stop_query, pause=pause_time): 
    urls.append(j)

time_end = time.time()
print('Time elapsed: ', time_end-time_start, ' seconds')
print(' ')


##################################################
print(' ')
if extra_filter:

	print('Applying extra filters..... ')
	social_media = []
	open_source = []
	portfolio = []

	for url in urls:
 		if ('git' in url) | ('code' in url):
 			open_source.append(url)

 		if ('linkd' in  url) | ('linkedin' in url) | ('stack' in url):
 			portfolio.append(url)

 		if ('fb' in url) | ('facebook' in url) | ('twitter' in url) | ('instagram' in url) | ('quora' in url) | ('kaggle' in url) | ('wiki' in url):
 			social_media.append(url)

	print(' ')
	print('Possible Open Source work: \n')
	for url in open_source:
 		print(url)

	print(' ')
	print('Social Media: \n')
	for url in social_media:
 		print(url)

	print(' ')
	print('Portfolio: \n')
	for url in portfolio:
 		print(url)

	print(' ')
	print('Other: \n')
	for url in urls:
		if (url not in open_source) & (url not in social_media) & (url not in portfolio):
 			print(url)
else:

	print ('Queried URLS for given person details:')
	for url in urls:
		print(url)


#################################################
print(' ')

if options.to_file:

	print('Writng to text file..... \n')
	f = open(to_file,"w+")

	f.write("OPEN SOURCE RELATED:" + "\n")
	f.write(" " + "\n")
	for url in open_source:
		f.write(url + "\n")
	f.write(" " + "\n")

	f.write("PORTFOLIO:" + "\n")
	f.write(" " + "\n")
	for url in portfolio:
		f.write(url + "\n")
	f.write(" " + "\n")

	f.write("SOCIAL MEDIA:" + "\n")
	f.write(" " + "\n")
	for url in social_media:
		f.write(url + "\n")
	f.write(" " + "\n")

	f.write("OTHER:" + "\n")
	f.write(" " + "\n")
	for url in urls:
		if (url not in open_source) & (url not in social_media) & (url not in portfolio):
			f.write(url + "\n")


	f.close()

	print('Written to text file successfully ! ')
 ##################################################