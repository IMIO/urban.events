# -*- coding: utf-8 -*-

from urban.events import utils
from plone import api

import logging
import os

logger = logging.getLogger("urban.events: migrations")


def update_talcondition_on_events(context):
    logger.info("starting : Update TAL Condition on new events")
    brains = api.content.find(
        container=api.portal.get(),
        id=[
            "en-attente-de-paiement-de-lamende",
            "intention-de-depot-de-plans-modifies",
        ],
        portal_type=["UrbanEventType", "EventConfig"],
    )
    for brain in brains:
        obj = brain.getObject()
        if obj.TALCondition in (None, u"context/is_CODT2024"):
            obj.TALCondition = u"here/is_CODT2024"
            logger.info("Update {0}".format(obj.absolute_url()))
    logger.info("upgrade done!")


def fix_event_type(context):
    logger.info("starting : Update event type on new events")
    brains = api.content.find(
        container=api.portal.get(),
        id="intention-de-depot-de-plans-modifies",
        portal_type=["EventConfig"],
    )
    for brain in brains:
        obj = brain.getObject()
        if obj.eventType in (None, [], ()):
            obj.eventType = (
                "Products.urban.interfaces.IIntentionToSubmitAmendedPlans",
            )
            logger.info("Update {0}".format(obj.absolute_url()))
    logger.info("upgrade done!")


def install_roaddecree_procedure(context):
    logger.info("starting : Import roaddecree events")
    directory_path = os.path.dirname(os.path.realpath(__file__))
    if "liege" not in utils.get_configs():
        path="./profiles/config/standard/roaddecree/urbantemplates.json"
        utils.import_json_config(
            json_path=os.path.normpath(os.path.join(directory_path, path)),
            context=api.portal.get_tool("portal_urban"),
            handle_existing_content=utils.ExistingContent.UPDATE,
        )

        utils.import_all_config(
            base_json_path="./profiles/config/standard/roaddecree",
            handle_existing_content=utils.ExistingContent.UPDATE,
            blacklist=["urbantemplates.json"],
        )
    logger.info("upgrade done!")


def install_housing_procedure(context):
    logger.info("starting : Import roaddecree events")
    if "liege" in utils.get_configs():
        utils.import_all_config(
            base_json_path="./profiles/config/liege/housing",
            handle_existing_content=utils.ExistingContent.UPDATE,
        )
    else:
        utils.import_all_config(
            base_json_path="./profiles/config/standard/housing",
            handle_existing_content=utils.ExistingContent.UPDATE,
        )
