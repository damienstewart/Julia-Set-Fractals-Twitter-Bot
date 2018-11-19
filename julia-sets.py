#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import random
import tweepy
import os
# driver function 
if __name__ == "__main__": 
    
	# setting the width, height and zoom  
	# of the image to be created 
	w, h, zoom = 1200, 600, 1
	
	bitmap = Image.new("RGB", (w, h), "white")
	pix = bitmap.load() 
	
	cX, cY = round(random.uniform(-1, 0),5), round(random.random(),5)
	print("Drawing Set (" + str(cX) + ", " + str(cY) + ") . . .")
	moveX, moveY = 0.0, 0.0
	maxIter = 255

	for x in range(w): 
		for y in range(h): 
			zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX 
			zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY 
			i = maxIter 
			while zx*zx + zy*zy < 4 and i > 1: 
				tmp = zx*zx - zy*zy + cX 
				zy,zx = 2.0*zx*zy + cY, tmp 
				i -= 1
				
  			# colors
			pix[x,y] = (i << 14) + (i << 29) + i*11
			
	fnt = ImageFont.truetype('hermit-medium-webfont.ttf', 15)
	d = ImageDraw.Draw(bitmap)
	d.text((10,10), str(cX) + ", " + str(cY) + "i", font=fnt, fill=(255, 255, 255))
	
	full_path = full_path = os.path.realpath(__file__)
	print full_path
	filename = 'output-' + str(random.randint(100000, 999999)) + '.png'
	print("Saving File " + filename + " . . .")
	bitmap.save(os.path.dirname(full_path) + "/img/" + filename)
	
	#enter the corresponding information from your Twitter application:
	CONSUMER_KEY = ''
	CONSUMER_SECRET = ''
	ACCESS_KEY = ''
	ACCESS_SECRET = ''
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	
	status = "Random Complex (" + str(cX) + ", " + str(cY) + ")"
	print("Sending Tweet . . .")
	api.update_with_media(os.path.dirname(full_path) + "/img/" + filename, status)
	print("Tweet Sent Successfully.")
