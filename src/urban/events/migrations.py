# -*- coding: utf-8 -*-

from plone import api

import logging

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
