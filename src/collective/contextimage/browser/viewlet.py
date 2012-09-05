# -*- coding: utf-8 -*-
import logging
from plone.app.layout.viewlets.common import (
    ViewletBase,
    LogoViewlet,
)
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Acquisition import aq_inner, aq_parent

logger = logging.getLogger('collective.contextimage')


class ContextImageBase(object):
    """Abstract Base for Context Images"""
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


class ContextFooterBase(object):
    """Abstract Base for Context Footer"""
    footer_name = None
    
    def aquire_footer(self):
        obj = aq_inner(self.context)
        context_footer = None
        while not IPloneSiteRoot.providedBy(obj):
            try:
                field = obj.getField(context_footer)
            except AttributeError, e:
                return
            if field is None:
                obj = aq_parent(aq_inner(obj))
                continue
            context_footer = field.get(obj)
            if not context_footer:
                obj = aq_parent(aq_inner(obj))
            else:
                break
        return context_footer

    @property
    def footer(self):
        context_footer = self.aquire_footer()
        if not context_footer:
            return 'nothing'
        return context_footer


class ImageViewlet(ContextImageBase, ViewletBase):
    """Base Viewlet for Context Images"""


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

    @property
    def default_imageurl(self):
        return PAGE_DEFAULT_IMAGE

    @property
    def default_css_template(self):
        return PAGE_CSS_TEMPLATE


HEADER_CSS_TEMPLATE = """
#portal-header {
    background: url('%s') no-repeat 0px 0px !important;
}
"""

HEADER_DEFAULT_IMAGE = '++resource++collective.contextimage.images/default.png'


class HeaderImageViewlet(CSSViewlet):
    image_field_name = 'header_context_image'

    @property
    def default_imageurl(self):
        return HEADER_DEFAULT_IMAGE

    @property
    def default_css_template(self):
        return HEADER_CSS_TEMPLATE


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


class ContextLogoViewlet(ContextImageBase, LogoViewlet):
    image_field_name = 'logo_context_image'

    def update(self):
        super(ContextLogoViewlet, self).update()
        image = self.aquire_context_image()
        if image:
            logoTitle = self.portal_state.portal_title()
            self.logo_tag = image.tag(title=logoTitle, alt=logoTitle)


class ContextFooterViewlet(ContextFooterBase):
    field_name = 'context_footer'
    
    def update(self):
        super(ContextFooterViewlet, self).update()
        context_footer = self.aquire_footer()
        if context_footer:
            return context_footer