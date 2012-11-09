from Products.CMFCore.permissions import setDefaultRoles


setDefaultRoles('Contextimage: Edit page context image',
                ('Manager', 'Site Administrator'))

setDefaultRoles('Contextimage: Edit header context image',
                ('Manager', 'Site Administrator'))

setDefaultRoles('Contextimage: Edit viewlet context image',
                ('Manager', 'Site Administrator'))

setDefaultRoles('Contextimage: Edit logo context image',
                ('Manager', 'Site Administrator'))

setDefaultRoles('Contextimage: Edit context footer',
                ('Manager', 'Site Administrator'))
