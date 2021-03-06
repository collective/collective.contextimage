# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.layout.viewlets.common import LogoViewlet
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.navigation.root import getNavigationRoot
import logging

logger = logging.getLogger('collective.contextimage')


class ContextField(object):
    """Abstract Base for context field acquiring.
    """
    field_name = None

    def acquire_field(self):
        obj = aq_inner(self.context)
        field = None
        while not IPloneSiteRoot.providedBy(obj):
            try:
                field = obj.getField(self.field_name)
            except AttributeError:
                return
            if field is None:
                obj = aq_parent(aq_inner(obj))
                continue
            field = field.get(obj)
            if not field:
                obj = aq_parent(aq_inner(obj))
            else:
                break
        return field


class ContextImageBase(ContextField):
    """Abstract Base for Context Images.
    """
    default_imageurl = None

    @property
    def imageurl(self):
        image = self.acquire_field()
        if not image:
            return self.default_imageurl
        return image.absolute_url()


class ImageViewlet(ContextImageBase, ViewletBase):
    """Base Viewlet for Context Images.
    """


class CSSViewlet(ImageViewlet):
    default_css_template = None
    media = 'all'

    def resource_url(self, urlpath):
        nav_root = getNavigationRoot(self.context)
        return '{0:s}/{1:s}'.format(nav_root, urlpath)

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

PAGE_DEFAULT_IMAGE = '++resource++collective.contextimage.images/' \
                     'default_page.png'


class PageImageViewlet(CSSViewlet):
    field_name = 'page_context_image'

    @property
    def default_imageurl(self):
        return self.resource_url(PAGE_DEFAULT_IMAGE)

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
    field_name = 'header_context_image'

    @property
    def default_imageurl(self):
        return self.resource_url(HEADER_DEFAULT_IMAGE)

    @property
    def default_css_template(self):
        return HEADER_CSS_TEMPLATE


class ContextImageViewlet(ImageViewlet):

    @property
    def image(self):
        default = '<img src="%s/viewlet_context_image_default.png" ' + \
                  'alt="Context specific Image" />'
        default = default % self.context.absolute_url()
        image = self.acquire_field()
        if not image:
            return default
        try:
            return image.tag()
        except Exception, e:
            logger.error(str(e))
            return default


class ContextLogoViewlet(ContextImageBase, LogoViewlet):
    field_name = 'logo_context_image'

    def update(self):
        super(ContextLogoViewlet, self).update()
        image = self.acquire_field()
        if image:
            logoTitle = self.portal_state.portal_title()
            self.logo_tag = image.tag(title=logoTitle, alt=logoTitle)


class ContextFooterViewlet(ContextField, ViewletBase):
    field_name = 'context_footer'

    @property
    def footer(self):
        context_footer = self.acquire_field()
        if not context_footer:
            return ''
        return context_footer
