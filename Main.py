import BeautifulSoup
import sys
import urllib2
import og

def get_og(name, soup):
	og_title = soup.findAll(property=name)
	if( len(og_title) > 0 ):
		og_title = og_title[0]["content"]
		return og_title
	else:
		return "No "+ name + " tag found"

if __name__ != '__main__':
	print "Initiating parse"
	if len(sys.argv) > 2: 
		print "Missing URL. Terminating"
		exit()
	else:
		print "Contacting " + sys.argv[1]
		url = sys.argv[1]
		
	try:
		content = urllib2.urlopen(url).read()
		print "Succecfully read the website"
	except urllib2.URLError: 
		print "The URL speficied was not valid. Terminating"
		exit()
	soup = BeautifulSoup.BeautifulSoup(content)
	print "----------------------------------"
	print "Title " + get_og("og:title", soup)
	print "Type " + get_og("og:type", soup)
	print "Image " + get_og("og:image", soup)
	print "URL " + get_og("og:url", soup)
	print "Description " + get_og("og:description", soup)
	print "Site name " + get_og("og:site_name", soup)
	print "Email " + get_og("og:email", soup)
	print "Phone Number " + get_og("og:phone_number", soup)
	print "----------------------------------"
else:
	print "Initiating parse : CORRECT"
	if len(sys.argv) > 2 : 
		print "Missing URL. Terminating"
		exit()
	else:
		print "Contacting " + sys.argv[1]
		url = sys.argv[1]
	open_graph = og.OG(url)
	open_graph.print_all()
	
	
