from zope.interface import Interface


class IContextImageExtensionLayer(Interface):
    """Browser layer for collective.contextimage
    """


class IPageImageExtensionLayer(IContextImageExtensionLayer): pass
class IHeaderImageExtensionLayer(IContextImageExtensionLayer): pass
class IViewletImageExtensionLayer(IContextImageExtensionLayer): pass
class ILogoImageExtensionLayer(IContextImageExtensionLayer): pass
class IFooterExtensionLayer(IContextImageExtensionLayer): pass


class IContextExtensible(Interface):
    """Marker indicating context being extensible.
    """


class IPageImageExtensible(IContextExtensible): pass
class IHeaderImageExtensible(IContextImageExtensionLayer): pass
class IViewletImageExtensible(IContextImageExtensionLayer): pass
class ILogoImageExtensible(IContextImageExtensionLayer): pass
class IFooterExtensible(IContextImageExtensionLayer): pass
