
####################################################
# basic imports

import sys
import os
import os.path

sys.path.append(r"C:\Program Files\ISIS\Udm\bin")
if os.environ.has_key("UDM_PATH"):
    sys.path.append(os.path.join(os.environ["UDM_PATH"], "bin"))

sys.path.append(os.path.join(os.path.dirname(__file__), "../../bin/"))
import udm

####################################################
#case processing functions

#process the model root node to find case root node
def processCases(node,d):

	#dictionary map of functions for valid cases (just one for now)
	cases = {"rhoSimpleFoamCase":rhoSimpleFoamCase}
	
	#create folder to write output
	if not os.path.exists(d):
		os.makedirs(d)
	os.chdir(d)
	
	#iterate through root node children and find and execute all valid cases
	for child in node.children():
		if child.type.name == "Folder":
			processCases(child,child.name)
		elif child.type.name in cases:
			print child.type.name + " case found: " + child.name
			func = cases[child.type.name]
			func(child)
			
	#return to original directory
	os.chdir("..")
	
#execute the rhoSimpleFoamCase
def rhoSimpleFoamCase(node):
	# print "function rhoSimpleFoam was called"
	#import necessary templates for this case
	print "Importing necessary templates..."
	from templates.scalarInitialCondition import scalarInitialCondition
	from templates.vectorInitialCondition import vectorInitialCondition
	from templates.controlDict import controlDict
	from templates.fvSchemes import fvSchemes
	from templates.fvSolution import fvSolution
	from templates.RASProperties import RASProperties
	from templates.thermophysicalProperties import thermophysicalProperties
	
	#create template object dictionary
	tmpls = {
			"alphat":scalarInitialCondition(),
			"T":scalarInitialCondition(),
			"U":vectorInitialCondition(),
			"epsilon":scalarInitialCondition(),
			"k":scalarInitialCondition(),
			"mut":scalarInitialCondition(),
			"p":scalarInitialCondition(),
			"controlDictProperties":controlDict(),
			"fvSchemesProperties":fvSchemes(),
			"fvSolution":fvSolution(),
			"RProperties":RASProperties(),
			"thermoProperties":thermophysicalProperties()
			}
	
	#create file names and location
	filenames = {
				"alphat":"0/alphat",
				"T":"0/T",
				"U":"0/U",
				"epsilon":"0/epsilon",
				"k":"0/k",
				"mut":"0/mut",
				"p":"0/p",
				"controlDictProperties":"system/controlDict",
				"fvSchemesProperties":"system/fvSchemes",
				"fvSolution":"system/fvSolution",
				"RProperties":"constant/RASProperties",
				"thermoProperties":"constant/thermophysicalProperties"
				}

	#create case directory and cd to it
	print "Creating file directory..."
	d = node.name
	if not os.path.exists(d):
		os.makedirs(d)
	if not os.path.exists(d+"/0"):
		os.makedirs(d+"/0")
	if not os.path.exists(d+"/constant"):
		os.makedirs(d+"/constant")
	if not os.path.exists(d+"/system"):
		os.makedirs(d+"/system")
	saveddir = os.getcwd()
	
	#change to case directory
	os.chdir(d)
	
	#pair templates with corresponding objects and write to file
	print "Writing files..."
	for tmpl in tmpls.keys():
		tmpls[tmpl].node = findNode(node,tmpl)
		f = open(filenames[tmpl], 'w')
		f.write(tmpls[tmpl].respond())
		f.close
		
	#move back to parent directory
	os.chdir(saveddir)
	print "Done!"

####################################################
#define helper functions

#find node that matches the given type and return it
def findNode(node,type):
	if node.type.name == type:
		return node
	elif len(node.children()) != 0:
		for child in node.children():
			tmp = findNode(child, type)
			if tmp != "":
				return tmp
	return ""

	#print function
def printTree(filename, tree):
	f = open(filename, 'w')
	total = printTreeHelper(f,tree, 0)
	f.write("\n"+"The total number of items in the model is: "+str(total))
	f.close()

#recursively print tree
def printTreeHelper(f, tree, numindents):
	total = 1
	indentation = ""
	if numindents != 0:
		for x in range(0, numindents):
			indentation = indentation+"\t"				
	f.write("".join([indentation,tree.type.name,"\n"]))
	if len(tree.children()) != 0:
		for x in range(0, len(tree.children())):
			total += printTreeHelper(f, tree.children()[x], numindents+1)
	return total
####################################################		
#Finally, do some work

test_meta_dn= udm.SmartDataNetwork(udm.uml_diagram())
print "Reading xml meta model into udm..."
test_meta_dn.open(r"OpenFOAMPreProcessing.xml", "")
test_meta = udm.map_uml_names(test_meta_dn.root)
dn = udm.SmartDataNetwork(test_meta_dn.root)
print "Opening Model..."
dn.open(r"OpenFOAMExamples.mga", "")


print "Finding valid cases..."
processCases(dn.root, dn.root.name)


# print "Printing structure to file..."
# printTree("ModelStructure.txt",dn.root)


