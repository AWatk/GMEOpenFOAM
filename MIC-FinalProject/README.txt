This is the final project for Model-Integrated Computing

Basic description:
	The OpenFOAMPreProcessing meta-model is divided into:
		reusable basic components (mainly dictionaries such as physical properties and solver and case settings)
		solver model (composed of the specific reusable components needed to describe a model)
	The OpenFOAM Examples is an example gme model using the OpenFOAMPreProcessing paradigm
	See the writeup folder for more in depth descriptions

Dependencies:
	Python 2.7
		Universal Data Model (http://www.isis.vanderbilt.edu/tools/UDM)
	GME
	
To use the premade example:
	run the OpenFOAM_Interpreter python script (that was easy)
	
To modify and update:
	1. Make modifications to the meta-model
	2. Export meta-model to uml using GME uml interpreter
	3. Update the paradigm
	4. Open the uml and export to xml using GME interpreter
	5. Make a model using the paradigm
	6. Point the python interpreter to the model and xml meta-model files as done in the example interpreter