from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
from j5basic import ImportModuleDef

def test_importmoduledef():
    module = {}
    ImportModuleDef.import_def_from('j5basic', module)
    assert 'ImportModuleDef' in module
    assert module['ImportModuleDef'] == ImportModuleDef
