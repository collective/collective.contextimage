from zope.interface import implements
from zope.component import adapts
from archetypes.schemaextender.interfaces import (
    IOrderableSchemaExtender,
    IBrowserLayerAwareExtender,
)
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.utils import OrderedDict
from Products.Archetypes.public import (
    ImageField,
)
from Products.Archetypes.interfaces import IBaseObject
from collective.contextimage.interfaces import IContextImageExtensionLayer


class XImageField(ExtensionField, ImageField): pass


class ViewletContextImageExtender(object):
    """Schema extender for context specific images displayed in a viewlet.
    """
    
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    adapts(IBaseObject)
    
    layer = IContextImageExtensionLayer

    fields = [
        XImageField(
            name='viewlet_context_image',
            schemata='Context Image',
        ),
    ]
    
    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
    
    def getOrder(self, original):
        neworder = OrderedDict()
        keys = original.keys()
        last = keys.pop()
        keys.insert(1, last)
        for schemata in keys:
            neworder[schemata] = original[schemata]
        return neworder