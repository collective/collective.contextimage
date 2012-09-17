from zope.interface import implements
from zope.component import adapts
from zope.i18nmessageid import MessageFactory
from archetypes.schemaextender.interfaces import (
    IOrderableSchemaExtender,
    IBrowserLayerAwareExtender,
)
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.utils import OrderedDict
from Products.Archetypes.public import (
    ImageField,
    ImageWidget,
    TextField,
    RichWidget,
)
from collective.contextimage.interfaces import (
    IPageImageExtensionLayer,
    IHeaderImageExtensionLayer,
    IViewletImageExtensionLayer,
    ILogoImageExtensionLayer,
    IFooterExtensionLayer,
    IPageImageExtensible,
    IHeaderImageExtensible,
    IViewletImageExtensible,
    ILogoImageExtensible,
    IFooterExtensible,
)

_ = MessageFactory('collective.contextimage')


class XImageField(ExtensionField, ImageField):
    pass


class XTextField(ExtensionField, TextField):
    pass


class ExtenderBase(object):
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    
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


class PageContextImageExtender(ExtenderBase):
    """Schema extender for context specific images displayed as background
    image of portal.
    """
    adapts(IPageImageExtensible)
    layer = IPageImageExtensionLayer

    fields = [
        XImageField(
            name='page_context_image',
            schemata='settings',
            widget=ImageWidget(
                label=_(u'label_page_context_image', u'Page Background Image'),
            )
        ),
    ]


class HeaderContextImageExtender(ExtenderBase):
    """Schema extender for context specific images displayed as background
    image of portal header.
    """
    adapts(IHeaderImageExtensible)
    layer = IHeaderImageExtensionLayer

    fields = [
        XImageField(
            name='header_context_image',
            schemata='settings',
            widget=ImageWidget(
                label=_(u'label_header_context_image',
                        u'Header Background Image'),
            )
        ),
    ]


class ViewletContextImageExtender(ExtenderBase):
    """Schema extender for context specific images displayed as viewlet.
    """
    adapts(IViewletImageExtensible)
    layer = IViewletImageExtensionLayer

    fields = [
        XImageField(
            name='viewlet_context_image',
            schemata='settings',
            widget=ImageWidget(
                label=_(u'label_viewlet_context_image', u'Viewlet Image'),
            )
        ),
    ]


class LogoContextImageExtender(ExtenderBase):
    """Schema extender for context specific images displayed as logo.
    """
    adapts(ILogoImageExtensible)
    layer = ILogoImageExtensionLayer

    fields = [
        XImageField(
            name='logo_context_image',
            schemata='settings',
            widget=ImageWidget(
                label=_(u'label_viewlet_logo_image', u'Logo Image'),
            )
        ),
    ]


class ContextFooterExtender(ExtenderBase):
    """Schema extender for context specific footer.
    """
    adapts(IFooterExtensible)
    layer = IFooterExtensionLayer

    fields = [
        XTextField(
            name='context_footer',
            default_output_type='text/html',
            schemata='settings',
            widget=RichWidget(
                label=_(u'label_viewlet_footer', u'Footer'),
            )
        ),
    ]
