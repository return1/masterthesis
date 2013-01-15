from zope.interface import Interface
from zope.app.file.interfaces import IImage
from zope.app.container.interfaces import IContainer
from zope.app.container.constraints import contains
from zope.schema import Text, TextLine, Date


class IEntry(IImage):
    """ Interface for Entry  """

    description = Text(title=u"Image Description", required=False)

    dateTaken = Date(title=u"Date when picture was taken", required=True)
    placeTaken = TextLine(title=u"Place where picture was taken",
                          required=True)

    contributor = TextLine(title=u"email of contributor", required=True)


class IEntryContainer(IContainer):
    """ Container Interface for an Entry """
    contains(IEntry)

class IEntryNav(Interface):
    """used as Adapter for menu creation
    """

    def setEntryMenuName(menuname):
        """ set the navigation menu name  """

    def getEntryMenuName():
        """ get the navigation menu name """

    def getEntryMenuNameFirstLetter():
        """ get the navigation menu name first letter """

    def getEntryMenuOrder():
        """ get the navigation menu order """

    def setEntryMenuOrder(order):
        """ set the navigation menu order """
                        
    def getChildren():
        """ get all IEntry children from this location """

    def getSiblings():
        """ get all IEntry Siblings from this location
            (self is included)
        """
        
