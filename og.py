import BeautifulSoup
import sys
import urllib2
class OG: 
	
	def __init__(self, url): 
		try:
			self.content = urllib2.urlopen(url).read()
		except urllib2.URLError: 
			print "The URL speficied was not valid. Terminating"
			exit()
		self.soup = BeautifulSoup.BeautifulSoup(self.content)
		
	
	def get_property(self, name):
		og_title = self.soup.findAll(property=name)
		if( len(og_title) > 0 ):
			og_title = og_title[0]["content"]
			return og_title
		else:
			return "No "+ name + " tag found"
			
	def print_all(self):
		print "----------------------------------"
		print "Title " + self.get_property("og:title")
		print "Type " + self.get_property("og:type")
		print "Image " + self.get_property("og:image")
		print "URL " + self.get_property("og:url")
		print "Description " + self.get_property("og:description")
		print "Site name " + self.get_property("og:site_name")
		print "Email " + self.get_property("og:email")
		print "Phone Number " + self.get_property("og:phone_number")
		print "----------------------------------"