#!/usr/bin/env python3

"""
Copyright (c) 2006-2023 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.data import logger
from plugins.generic.enumeration import Enumeration as GenericEnumeration

class Enumeration(GenericEnumeration):
    def getRoles(self, *args, **kwargs):
        warnMsg = "on Vertica it is not possible to enumerate the user roles"
        logger.warning(warnMsg)

        return {}
