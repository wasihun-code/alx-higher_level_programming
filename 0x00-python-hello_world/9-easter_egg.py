#!/usr/bin/python3
import sys, cStringIO
zen = cStringIO.StringIO()
old_stdout = sys.stdout
sys.stdout = zen
import this
sys.stdout = old_stdout
print(zen.getvalue())