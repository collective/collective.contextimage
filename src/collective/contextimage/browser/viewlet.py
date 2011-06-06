from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Acquisition import aq_inner, aq_parent


class ContextImageViewlet(ViewletBase):
    
    @property
    def image(self):
        obj = aq_inner(self.context)
        image = None
        default = '%s/vielwet_context_image_default.png' \
            % self.context.absolute_url()
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
            return default
        try:
            return image.tag()
        except Exception, e:
            print e
            return default