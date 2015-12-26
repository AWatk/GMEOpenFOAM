#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1449709164.747
__CHEETAH_genTimestamp__ = 'Wed Dec 09 18:59:24 2015'
__CHEETAH_src__ = 'scalarInitialCondition.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Dec 09 18:58:01 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class scalarInitialCondition(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(scalarInitialCondition, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''/*--------------------------------*- C++ -*----------------------------------*\\
| =========                 |                                                 |
| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\\\    /   O peration     | Version:  2.4.0                                 |
|   \\\\  /    A nd           | Web:      www.OpenFOAM.org                      |
|    \\\\/     M anipulation  |                                                 |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       volScalarField;
    location    "0";
    object      ''')
        _v = VFFSL(SL,"node.type.name",True) # u'$node.type.name' on line 14, col 17
        if _v is not None: write(_filter(_v, rawExpr=u'$node.type.name')) # from line 14, col 17.
        write(u''';
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
''')
        for child in VFN(VFFSL(SL,"node",True),"children",False)(): # generated from line 17, col 1
            if 'Properties' in VFFSL(SL,"child.type.name",True): # generated from line 18, col 1
                write(u'''dimensions      ''')
                _v = VFFSL(SL,"child.dimensions",True) # u'$child.dimensions' on line 19, col 17
                if _v is not None: write(_filter(_v, rawExpr=u'$child.dimensions')) # from line 19, col 17.
                write(u''';

internalField   ''')
                _v = VFFSL(SL,"child.internalField",True) # u'$child.internalField' on line 21, col 17
                if _v is not None: write(_filter(_v, rawExpr=u'$child.internalField')) # from line 21, col 17.
                write(u''';

''')
        write(u'''boundaryField
{
''')
        for child in VFN(VFFSL(SL,"node",True),"children",False)(): # generated from line 27, col 1
            if 'Boundary' in VFFSL(SL,"child.type.name",True): # generated from line 28, col 1
                write(u'''\t''')
                _v = VFFSL(SL,"child.patchName",True) # u'$child.patchName' on line 29, col 2
                if _v is not None: write(_filter(_v, rawExpr=u'$child.patchName')) # from line 29, col 2.
                write(u'''
\t{
\t\ttype\t\t\t''')
                _v = VFFSL(SL,"child.btype",True) # u'$child.btype' on line 31, col 10
                if _v is not None: write(_filter(_v, rawExpr=u'$child.btype')) # from line 31, col 10.
                write(u''';
''')
                if 'inletOutlet' in VFFSL(SL,"child.btype",True): # generated from line 32, col 1
                    write(u'''\t\tinletValue\t\t''')
                    _v = VFFSL(SL,"child.inletValue",True) # u'$child.inletValue' on line 33, col 15
                    if _v is not None: write(_filter(_v, rawExpr=u'$child.inletValue')) # from line 33, col 15.
                    write(u''';
''')
                if 'compressible::turbulentMixingLengthDissipationRateInlet' in VFFSL(SL,"child.btype",True): # generated from line 35, col 1
                    write(u'''\t\tmixingLength\t''')
                    _v = VFFSL(SL,"child.mixingLength",True) # u'$child.mixingLength' on line 36, col 16
                    if _v is not None: write(_filter(_v, rawExpr=u'$child.mixingLength')) # from line 36, col 16.
                    write(u''';
''')
                if 'turbulentIntensityKineticEnergyInlet' in VFFSL(SL,"child.btype",True): # generated from line 38, col 1
                    write(u'''\t\tintensity\t\t''')
                    _v = VFFSL(SL,"child.intensity",True) # u'$child.intensity' on line 39, col 14
                    if _v is not None: write(_filter(_v, rawExpr=u'$child.intensity')) # from line 39, col 14.
                    write(u''';
''')
                if not ('zero' in '$child.btype'): # generated from line 41, col 1
                    write(u'''\t\tvalue\t\t\t''')
                    _v = VFFSL(SL,"child.value",True) # u'$child.value' on line 42, col 11
                    if _v is not None: write(_filter(_v, rawExpr=u'$child.value')) # from line 42, col 11.
                    write(u''';
''')
                write(u'''\t}
''')
        write(u'''}


// ************************************************************************* //
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_scalarInitialCondition= 'respond'

## END CLASS DEFINITION

if not hasattr(scalarInitialCondition, '_initCheetahAttributes'):
    templateAPIClass = getattr(scalarInitialCondition, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(scalarInitialCondition)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=scalarInitialCondition()).run()


