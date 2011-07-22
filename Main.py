#!/usr/bin/env python
# encoding: utf-8
import og
""" Creates a OpenGraph fetcher class and prints some info and saves the image n stuff. """
if __name__ == '__main__':
	print "Initiating parse"
	if len(sys.argv) > 2 : 
		print "Missing URL. Terminating"
		exit()
	else:
		print "Contacting " + sys.argv[1]
		url = sys.argv[1]
	open_graph = og.OG(url)
	open_graph.print_all()
	if open_graph.cache_image():
		print "Image has been cached"
	else:
		print "No image found"
	print "Done"
	exit(0)
	
	
