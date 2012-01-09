from zope.interface import Interface


class IContextImageExtensionLayer(Interface):
    """Browser layer for collective.contextimage
    """


class IPageImageExtensionLayer(IContextImageExtensionLayer): pass


class IHeaderImageExtensionLayer(IContextImageExtensionLayer): pass


class IViewletImageExtensionLayer(IContextImageExtensionLayer): pass