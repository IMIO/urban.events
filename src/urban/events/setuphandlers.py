# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from urban.events.utils import import_all_config


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "urban.events:uninstall",
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.

    import_all_config(
        "./profiles/config",
        "portal_urban",
        "urbaneventtypes",
    )


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
