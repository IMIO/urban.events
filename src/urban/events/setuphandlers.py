# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from plone import api
from zope.interface import implementer
from urban.events.utils import import_all_config

import os


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
    portal_urban = api.portal.get().portal_urban

    configs = os.environ.get("URBAN_EVENTS_CONFIGS", "default,standard")
    configs = configs.split(",")

    config_folder_id = "urbaneventtypes"
    replacements = []
    if config_folder_id not in portal_urban.codt_buildlicence.keys():
        config_folder_id = "eventconfigs"
        replacements = [("urbaneventtypes", config_folder_id)]
    for config in configs:
        import_all_config(
            "./profiles/config/{0}".format(config),
            "portal_urban",
            config_folder_id,
            id_replacements=replacements,
        )


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
