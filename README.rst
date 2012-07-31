collective.contextimage
=======================

Provide extension fields for context specific images. This images can be used
as layout elements. If the current context does not provide an image it is 
aquired from its parents. 

It is useful i.e.
 
- if you like to have a different logo or header background on different sections 
  of your site,
- if you want to set a background image for your content,
- if you want to place an image in context somehwere in the page using a 
  viewlet.

Separate schema extenders are provided with corresponsing renderers bound to 
browserlayers loaded by different profiles. This way its possible to enable
only one of the several features:

*Viewlet context image*
    An image which gets rendered by a viewlet as ``img`` tag. Profile is
    ``profile-collective.contextimage:viewlet``.

*Header context image*
    An image which gets rendered as portal header background. Profile is
    ``profile-collective.contextimage:header``.

*Page context image*
    An image which gets rendered as page background. Profile is
    ``profile-collective.contextimage:page``.

*Logo context image*
    An image which gets rendered as portal logo. This is a drop in replacement
    for the logo viewlet with fallback to default logo). Profile is
    ``profile-collective.contextimage:logo``.


Installation
============

Just depend in your buildout on the egg ``collective.conteximage``. ZCML is
loaded automagically with z3c.autoinclude.

Install it as an addon in Plone control-panel or portal_setup.

This package is written for Plone 4.1 or later.

Each of this features can be activated by importing the refering GenericSetup
profile.

If i.e. page background and header image support desired, add
following to integration GS profile metadata.xml::

    <?xml version="1.0"?>
    <metadata>
      <version>1</version>
      <dependencies>
        <dependency>profile-collective.contextimage:page</dependency>
        <dependency>profile-collective.contextimage:header</dependency>
      </dependencies> 
    </metadata>


Source Code and Contributions
=============================

If you want to help with the development (improvement, update, bug-fixing, ...)
of ``collective.contextimage`` this is a great idea!

The code is located in the
`github collective <https://github.com/collective/collective.contextimage>`_.

You can clone it or `get access to the github-collective
<http://collective.github.com/>`_ and work directly on the project.

Maintainer is Robert Niederreiter and the BlueDynamics Alliance developer team.
We appreciate any contribution and if a release is needed to be done on pypi,
please just contact one of us
`dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_

Contributors
============

- Robert Niederreiter <rnix@squarewave.at>

- Jens W. Klein <jens@bluedynamics.com>

