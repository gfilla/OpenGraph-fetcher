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

if __name__ == '__main__':
	print "Initiating parse : CORRECT"
	if len(sys.argv) > 2 : 
		print "Missing URL. Terminating"
		exit()
	else:
		print "Contacting " + sys.argv[1]
		url = sys.argv[1]
	open_graph = og.OG(url)
	open_graph.print_all()
	
	
