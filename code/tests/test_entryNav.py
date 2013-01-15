import unittest
from doctest import DocFileSuite, ELLIPSIS

#import zope.component.testing
import zope.app.testing.setup 
#from zope.annotation.attribute import AttributeAnnotations
from zope.app.folder import rootFolder

from sgs.entry.interfaces import IEntryNav
from sgs.entry.entry import EntryNav
from sgs.entry.entry import Entry

def setupEntryStructure():
    """ Set up a reasonably complex folder structure

     ____________ rootFolder ________________________
    /                                                \
 folder1 _______________________________	   folder2
   |				        \             |     
 folder1_1 ________________	      folder1_2    folder2_1
   |           \           \             |            |
 folder1_1_1 folder1_1_2 folder1_1_3  folder1_2_1  folder2_1_1
    """
    root = rootFolder()
    entry = root[u'entry1'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Pictorial')
    IEntryNav(entry).setEntryMenuOrder(2)
    entry = root[u'entry1'][u'entry1_1'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Menschen')
    IEntryNav(entry).setEntryMenuOrder(12)
    entry = root[u'entry1'][u'entry1_1'][u'entry1_1_1'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Frauen')
    IEntryNav(entry).setEntryMenuOrder(113)
    entry = root[u'entry1'][u'entry1_1'][u'entry1_1_2'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Gruppen')
    IEntryNav(entry).setEntryMenuOrder(111)
    entry = root[u'entry1'][u'entry1_1'][u'entry1_1_3'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Ausrutschen')
    IEntryNav(entry).setEntryMenuOrder(112)
    entry = root[u'entry1'][u'entry1_2'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Verkehr')
    IEntryNav(entry).setEntryMenuOrder(11)
    entry = root[u'entry1'][u'entry1_2'][u'entry1_2_1'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Pferd')
    entry = root[u'entry2'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Sozial')
    IEntryNav(entry).setEntryMenuOrder(1)
    entry = root[u'entry2'][u'entry2_1'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Hilfestellungen')
    IEntryNav(entry).setEntryMenuOrder(21)
    entry = root[u'entry2'][u'entry2_1'][u'entry2_1_1'] = Entry()
    IEntryNav(entry).setEntryMenuName(u'Offiziell')
    IEntryNav(entry).setEntryMenuOrder(22)
    return root


def setUp(test):
    zope.app.testing.setup.placefulSetUp(site=True)
    zope.component.provideAdapter(EntryNav)
    
def tearDown(self):
    zope.app.testing.setup.placefulTearDown()

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('entry.txt',
                     package='sgs.entry',
                     setUp=setUp,
                     tearDown=tearDown,
                     optionflags=ELLIPSIS,
                     globs={'testEntryStructure': setupEntryStructure}),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
