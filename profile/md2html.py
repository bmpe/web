#!/usr/bin/env python 
import glob
import os

files = glob.glob("*.md")
for f in files:
  cmd = "pandoc -c style.css -o {1} {0}".format(f, f.replace(".md",".html"))
  print cmd
  os.system(cmd)
