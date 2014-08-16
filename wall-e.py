#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, random, sys, time, json
from gi.repository import Gio
from os.path import expanduser

class Cycle():
	def background(self):
		gsettings = Gio.Settings.new('org.gnome.desktop.background')
		home = expanduser("~")
		config_file=open(home + '/.wall-e.cnf')
		config = json.load(config_file)
		path = config['path']		
		filename = random.choice(os.listdir(path))
		gsettings.set_string('picture-uri', 'file://' + path + filename)
		gsettings.apply()
		minutes = config['minutes']
		time.sleep(60*minutes)		

if __name__ == "__main__":
	while True:
		Cycle().background()

