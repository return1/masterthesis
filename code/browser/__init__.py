from operator import itemgetter

from zope.traversing.api import getParents
from zope.traversing.interfaces import IPhysicallyLocatable
from zope.publisher.browser import BrowserView
from zope.traversing.browser import absoluteURL

from sgs.entry.interfaces import IEntryNav

class EntryNavigation(BrowserView):

    def __call__(self):
        root = IPhysicallyLocatable(self.context).getNearestSite()
        parents = getParents(self.context)

        # remove all parents below the first found site
        while parents[-1] != root:
            parents.pop()

        parents.pop() #remove Site from parents
        parents.reverse()

        parentSiblings = [ sorted( [
            {'name':IEntryNav(sibling).getEntryMenuName(),
             'order':IEntryNav(sibling).getEntryMenuOrder(),
             'url':absoluteURL(sibling, self.request),
             'active':((sibling in parents) and 'parent') or False}
            for sibling in IEntryNav(item).getSiblings() ] ,
                                key=itemgetter('order')) for item in parents ]

        mySiblings = sorted( [
            {'name':IEntryNav(sibling).getEntryMenuName(),
             'order':IEntryNav(sibling).getEntryMenuOrder(),
             'url':absoluteURL(sibling, self.request),
             'active':((sibling == self.context) and 'self') or False} \
            for sibling in IEntryNav(self.context).getSiblings() ] ,
                             key=itemgetter('order')) 

        
        children = sorted( [
            {'name':IEntryNav(child).getEntryMenuName(),
             'order':IEntryNav(child).getEntryMenuOrder(),
             'url':absoluteURL(child, self.request) }
            for child in IEntryNav(self.context).getChildren() ],
                           key=itemgetter('order'))
        
        parentSiblings.append(mySiblings)
        
        if len(children):
            parentSiblings.append(children)

        return parentSiblings
