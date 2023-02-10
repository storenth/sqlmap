#!/usr/bin/env python3

"""
Copyright (c) 2006-2023 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.exception import SqlmapUnsupportedFeatureException
from plugins.generic.filesystem import Filesystem as GenericFilesystem

class Filesystem(GenericFilesystem):
    def readFile(self, remoteFile):
        errMsg = "on Microsoft Access it is not possible to read files"
        raise SqlmapUnsupportedFeatureException(errMsg)

    def writeFile(self, localFile, remoteFile, fileType=None, forceCheck=False):
        errMsg = "on Microsoft Access it is not possible to write files"
        raise SqlmapUnsupportedFeatureException(errMsg)
