# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from Products.CMFPlone.utils import get_installer
from plone import api
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from urban.events import testing  # noqa: E501

import unittest


class TestSetup(unittest.TestCase):
    """Test that urban.events is properly installed."""

    layer = testing.URBAN_EVENTS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if urban.events is installed."""
        self.assertTrue(self.installer.is_product_installed("urban.events"))

    def test_browserlayer(self):
        """Test that IUrbanEventsLayer is registered."""
        from urban.events.interfaces import IUrbanEventsLayer
        from plone.browserlayer import utils

        self.assertIn(IUrbanEventsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = testing.URBAN_EVENTS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("urban.events")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if urban.events is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("urban.events"))

    def test_browserlayer_removed(self):
        """Test that IUrbanEventsLayer is removed."""
        from urban.events.interfaces import IUrbanEventsLayer
        from plone.browserlayer import utils

        self.assertNotIn(IUrbanEventsLayer, utils.registered_layers())
