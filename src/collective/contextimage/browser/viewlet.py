# -*- coding: utf-8 -*-
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Acquisition import aq_inner, aq_parent


class ContextImageViewlet(ViewletBase):
    
    @property
    def image(self):
        obj = aq_inner(self.context)
        image = None
        default = '<img src="%s/viewlet_context_image_default.png" ' + \
                  'alt="Context specific Image" />'
        default = default % self.context.absolute_url()
        while not IPloneSiteRoot.providedBy(obj):
            try:
                field = obj.getField('viewlet_context_image')
            except AttributeError, e:
                return default
            if field is None:
                obj = aq_parent(aq_inner(obj))
                continue
            image = field.get(obj)
            if not image:
                obj = aq_parent(aq_inner(obj))
            else:
                break
        if not image:
            return default
        try:
            return image.tag()
        except Exception, e:
            print e
            return default


CSS_TEMPLATE = """
#portal-header {
    background: url('%s') no-repeat 0px 0px !important;
}
"""

DEFAULT_IMAGE = '++resource++collective.contextimage.images/default.png'

class HeaderImageViewlet(ViewletBase):
    
    @property
    def imageurl(self):
        obj = aq_inner(self.context)
        image = ''
        while not IPloneSiteRoot.providedBy(obj):
            field = obj.getField('viewlet_context_image')
            if field is None:
                obj = aq_parent(aq_inner(obj))
                continue
            image = field.get(obj)
            if not image:
                obj = aq_parent(aq_inner(obj))
            else:
                break
        if not image:
            return '%s/%s' % (self.context.absolute_url(), DEFAULT_IMAGE)
        return image.absolute_url()
    
    @property
    def css(self):
        try:
            return CSS_TEMPLATE % self.imageurl
        except Exception, e:
            print e
            return u''