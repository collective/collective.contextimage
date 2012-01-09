collective.contextimage
=======================

Provide extension fields for context specific images. This images can be used
as layout elements.

Currently, three separate schema extenders are provided with corresponsing
renderers:

*Viewlet context image*
    An image which gets rendered by a viewlet as ``img`` tag.

*Header context image*
    An image which gets rendered as portal header background.

*Page context image*
    An image which gets rendered as page background.


Each of this extenders can be activated by importing the refering GenericSetup
profile. If i.e. page background and header image support desired, add
following to integration GS profil metadata.xml::

    <?xml version="1.0"?>
    <metadata>
      <version>1</version>
      <dependencies>
        <dependency>profile-collective.contextimage:default</dependency>
        <dependency>profile-collective.contextimage:page</dependency>
        <dependency>profile-collective.contextimage:header</dependency>
      </dependencies> 
    </metadata>


Changes
=======

0.4
---

- separate context images for portal background, header background and viewlet.
  [rnix]

0.3
---

- add viewlet for using context image as header background
  [rnix]

0.2
---

- typos
  [rnix]

0.1
---

- initial
  [rnix]