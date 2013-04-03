from zope.interface import implementer
from zope.component import adapter
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


class XImageField(ExtensionField, ImageField): pass
class XTextField(ExtensionField, TextField): pass


@implementer(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
class ExtenderBase(object):
    
    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
    
    def getOrder(self, order):
        return order


@adapter(IPageImageExtensible)
class PageContextImageExtender(ExtenderBase):
    """Schema extender for context specific images displayed as background
    image of portal.
    """
    layer = IPageImageExtensionLayer

    fields = [
        XImageField(
            name='page_context_image',
            schemata='settings',
            widget=ImageWidget(
                label=_(u'label_page_context_image', u'Page Background Image'),
            ),
            write_permission='Contextimage: Edit page context image',
        ),
    ]


@adapter(IHeaderImageExtensible)
class HeaderContextImageExtender(ExtenderBase):
    """Schema extender for context specific images displayed as background
    image of portal header.
    """
    layer = IHeaderImageExtensionLayer

    fields = [
        XImageField(
            name='header_context_image',
            schemata='settings',
            widget=ImageWidget(
                label=_(u'label_header_context_image',
                        u'Header Background Image'),
            ),
            write_permission='Contextimage: Edit header context image',
        ),
    ]


@adapter(IViewletImageExtensible)
class ViewletContextImageExtender(ExtenderBase):
    """Schema extender for context specific images displayed as viewlet.
    """
    layer = IViewletImageExtensionLayer

    fields = [
        XImageField(
            name='viewlet_context_image',
            schemata='settings',
            widget=ImageWidget(
                label=_(u'label_viewlet_context_image', u'Viewlet Image'),
            ),
            write_permission='Contextimage: Edit viewlet context image',
        ),
    ]


@adapter(ILogoImageExtensible)
class LogoContextImageExtender(ExtenderBase):
    """Schema extender for context specific images displayed as logo.
    """
    layer = ILogoImageExtensionLayer

    fields = [
        XImageField(
            name='logo_context_image',
            schemata='settings',
            widget=ImageWidget(
                label=_(u'label_viewlet_logo_image', u'Logo Image'),
            ),
            write_permission='Contextimage: Edit logo context image',
        ),
    ]


@adapter(IFooterExtensible)
class ContextFooterExtender(ExtenderBase):
    """Schema extender for context specific footer.
    """
    layer = IFooterExtensionLayer

    fields = [
        XTextField(
            name='context_footer',
            default_output_type='text/html',
            schemata='settings',
            widget=RichWidget(
                label=_(u'label_viewlet_footer', u'Footer'),
            ),
            write_permission='Contextimage: Edit context footer',
        ),
    ]
