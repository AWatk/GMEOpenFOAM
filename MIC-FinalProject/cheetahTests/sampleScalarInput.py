import sys
import os
import os.path
from templates import sampleScalarInitialCondition

bds =[
	{"name":"inlet", "type":"calculated", "value":"uniform 0"},
	{"name":"outlet", "type":"calculated", "value":"uniform 0"},
	{"name":"wall", "type":"compressible::alphatWallFunction", "value":"uniform 0"}
	]
# mp = {"object":"alphat", "dimensions":"[1 -1 -1 0 0 0 0]", "internalField":"uniform 0", "boundaries":bds}

# tmpl =Template(file="sampleScalarInitialCondition.tmpl", searchList=[mp])
tmpl = {"t":sampleScalarInitialCondition()}

# tmpl = sampleScalarInitialCondition()
# print tmpl.keys()
tmpl["t"].object = "alphat"
tmpl["t"].dimensions = "[1 -1 -1 0 0 0 0]"
tmpl["t"].internalField = "uniform"
tmpl["t"].boundaries = bds

# print tmpl["t"].respond()
# tmpl["t"].respond()

f = open("test", 'w')
f.write(tmpl["t"].respond())
f.close()