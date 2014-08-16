Wall-E
=======

A lightweight python wallpaper changer for Gnome 3, Unity and Pantheon

Guide
=======

To install Wall-E, simply place the **.wall-e.cnf** configuration file in your users home directory (~).

Wall-E uses json for its configuration, so it is very simple to setup.  There are only 2 configuration options:

* **Path** - The folder containing the wallpapers.
* **Minutes** - The duration, in minutes, between each wallpaper change.

Lastly, run Wall-E!  This can be achieved by doing the following:

1. Set the script to be exectuable: ```chmod +x /path/to/wall-e.py```
2. Move the script to a location in your $PATH, this should work on most systems: ```sudo mv /path/to/wall-e.py /usr/bin/```
3. Run the script: ```wall-e.py```

You will probably want to set this up to run as a startup application.
