# -*- coding: utf-8 -*-
import logging
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Acquisition import aq_inner, aq_parent

logger = logging.getLogger('collective.contextimage')


class ImageViewlet(ViewletBase):
    
    image_field_name = None
    default_imageurl = None
    
    def aquire_context_image(self):
        obj = aq_inner(self.context)
        image = None
        while not IPloneSiteRoot.providedBy(obj):
            try:
                field = obj.getField(self.image_field_name)
            except AttributeError, e:
                return
            if field is None:
                obj = aq_parent(aq_inner(obj))
                continue
            image = field.get(obj)
            if not image:
                obj = aq_parent(aq_inner(obj))
            else:
                break
        return image
    
    @property
    def imageurl(self):
        image = self.aquire_context_image()
        if not image:
            return '%s/%s' % (self.context.absolute_url(),
                              self.default_imageurl)
        return image.absolute_url()


class CSSViewlet(ImageViewlet):
    
    default_css_template = None 
    
    @property
    def css(self):
        try:
            return self.default_css_template % self.imageurl
        except Exception, e:
            logger.error(str(e))
            return u''


PAGE_CSS_TEMPLATE = """
html {
    background:url('%s') no-repeat top center fixed;
    -webkit-background-size:cover;
    -moz-background-size:cover;
    -o-background-size:cover;
    background-size:cover;
}
"""

PAGE_DEFAULT_IMAGE = '++resource++collective.contextimage.images/default_page.png'


class PageImageViewlet(CSSViewlet):
    image_field_name = 'page_context_image'
    default_imageurl = PAGE_DEFAULT_IMAGE
    default_css_template = PAGE_CSS_TEMPLATE


HEADER_CSS_TEMPLATE = """
#portal-header {
    background: url('%s') no-repeat 0px 0px !important;
}
"""

HEADER_DEFAULT_IMAGE = '++resource++collective.contextimage.images/default.png'


class HeaderImageViewlet(CSSViewlet):
    image_field_name = 'header_context_image'
    default_imageurl = HEADER_DEFAULT_IMAGE
    default_css_template = HEADER_CSS_TEMPLATE


class ContextImageViewlet(ImageViewlet):
    
    @property
    def image(self):
        default = '<img src="%s/viewlet_context_image_default.png" ' + \
                  'alt="Context specific Image" />'
        default = default % self.context.absolute_url()
        image = self.aquire_context_image()
        if not image:
            return default
        try:
            return image.tag()
        except Exception, e:
            logger.error(str(e))
            return default