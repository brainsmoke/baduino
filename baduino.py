#!/usr/bin/python

from pathtokicad import *

fill_paths = [

	(BACK_MASK,   "baduino/backmask.path"), # soldermask back
	(BACK_COPPER,   "baduino/backcopper.path"),
	(FRONT_MASK,   "baduino/text.path"),
	(FRONT_COPPER, "baduino/text.path"),
]

segment_paths = [
	(EDGES,        "baduino/edges.segments", .9),
]

pads = [
]

print_module("baduino", fill_paths, segment_paths, pads)
 
