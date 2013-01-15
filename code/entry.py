from zope.interface import implements
from zope.component import adapts
from zope.app.container.btree import BTreeContainer
from zope.app.file.image import Image
from zope.size.interfaces import ISized
from zope.size import byteDisplay
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.annotation import IAnnotations
from zope.app.i18n import ZopeMessageFactory as _

from interfaces import *

class Entry(BTreeContainer, Image):
    implements(IEntry, IEntryContainer, IAttributeAnnotatable)

    __name__ = __parent__ = None

    description = u""
    
    dateTaken = None
    placeTaken = u""
     
    contributor = u""


EntryNavAnnotations_KEY = "sgs.entrynav"

class EntryNav(object):
    implements(IEntryNav)
    adapts(IEntry)

    def __init__(self, context):
        self.context = self.__parent__  = context # see PvWh book site 269
        annotations = IAnnotations(context)
        mapping = annotations.get(EntryNavAnnotations_KEY)
        if mapping is None:
            mapping = annotations[EntryNavAnnotations_KEY] = {'name': '',
                                                              'order': 0}
        self.mapping = mapping

    def setEntryMenuName(self, menuname):
        self.mapping['name'] = menuname

    def getEntryMenuName(self):
        return self.mapping['name']

    def getEntryMenuNameFirstLetter(self):
        if len(self.mapping['name']):
            return self.mapping['name'][0]

    def setEntryMenuOrder(self, order):
        self.mapping['order'] = order

    def getEntryMenuOrder(self):
        return self.mapping['order']

    def getChildren(self):
        return self.context.values() 

    def getSiblings(self):
        siblings = []
        for sibling in self.context.__parent__.values():
            if IEntry.providedBy(sibling):
                siblings.append(sibling)
        return siblings


            
class EntrySized(object):
    implements(ISized)
    adapts(IEntry)

    def __init__(self, container):
        self._container = container

    def sizeForSorting(self):
        """See `ISized`"""
        return ('item', len(self._container)) 
        #return ('byte', self._container.getSize()) 

    def sizeForDisplay(self):
        """See `ISized`"""
        bytes = self._container.getSize()
        byte_size = byteDisplay(bytes)

        num_items = len(self._container)

        mapping = byte_size.mapping
        if mapping is None:
            mapping = {}
        mapping.update({'items': str(num_items)})

        if num_items == 1:
            return _("${items} item / " + byte_size , mapping=mapping)
        else:
            return _("${items} items / " + byte_size , mapping=mapping)
