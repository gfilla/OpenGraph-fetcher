#!/usr/bin/env python
# encoding: utf-8

import BeautifulSoup
import sys
import urllib2
import urllib
class OG: 
	""" Open graph fetcher class."""
	def __init__(self, url): 
		try:
			self.content = urllib2.urlopen(url).read()
		except urllib2.URLError: 
			print "The URL speficied was not valid. Terminating"
			exit(0)
		self.soup = BeautifulSoup.BeautifulSoup(self.content)
		
	
	def get_property(self, name):
		og_title = self.soup.findAll(property=name)
		if( len(og_title) > 0 ):
			og_title = og_title[0]["content"]
			return og_title
		else:
			return ""
			
	def print_all(self):
		print "----------------------------------"
		print "Title " + self.get_property("og:title")
		print "Type " + self.get_property("og:type")
		print "Image " + self.get_property("og:image")
		print "URL " + self.get_property("og:url")
		print "Description " + self.get_property("og:description")
		print "Site name " + self.get_property("og:site_name")
		print "Contact"
		print "Email " + self.get_property("og:email")
		print "Phone Number " + self.get_property("og:phone_number")
		print "Fax number" + self.get_property("og:fax_number")
		print "Location"
		print "Latitude " + self.get_property("og:latitude")
		print "Longitude " + self.get_property("og:longitude")
		print "Street Adress " + self.get_property("og:street-address")
		print "Locality " + self.get_property("og:locality")
		print "Region " + self.get_property("og:region")
		print "Postal code " + self.get_property("og:postal-code")
		print "Country name " + self.get_property("og:country-name")
		print "Video"
		print "Video link " + self.get_property("og:video")
		print "height " + self.get_property("og:video:height")
		print "width " + self.get_property("og:video:width")
		print "type " + self.get_property("og:video:type")
		print "Audio"
		print "Audio URL " + self.get_property("og:audio")
		print "Title " + self.get_property("og:audio:title")
		print "Artist " + self.get_property("og:audio:artist")
		print "Album " + self.get_property("og:audio:album")
		print "Type " + self.get_property("og:audio:type")
		print "----------------------------------"
		
	def cache_image(self, filename="cached.jpg"):
		img_url = self.get_property("og:image")
		if img_url != "":
			urllib.urlretrieve(img_url, filename)
			return True
		else:
			return False