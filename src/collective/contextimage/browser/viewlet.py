# -*- coding: utf-8 -*-
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Acquisition import aq_inner, aq_parent

CSS_TEMPLATE = """
#portal-header {
    background: url('%s') no-repeat 0px 0px !important;
}
"""

class ContextImageViewlet(ViewletBase):
    
    @property
    def imageurl(self):
        obj = aq_inner(self.context)
        image = ''
        while not IPloneSiteRoot.providedBy(obj):
            field = obj.getField('contextimage')
            if field is None:
                obj = aq_parent(aq_inner(obj))
                continue
            image = field.get(obj)
            if not image:
                obj = aq_parent(aq_inner(obj))
            else:
                break
        if not image:
            base = u'++resource++.images/%s'
            default = base % u'bannertop_980x108-frontpage.jpg'
            return default # XXX
        return image.absolute_url()
    
    @property
    def css(self):
        try:
            return CSS_TEMPLATE % self.imageurl
        except Exception, e:
            print e
            return ''
