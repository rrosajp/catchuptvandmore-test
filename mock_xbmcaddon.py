# -*- coding: utf-8 -*-

# The unicode_literals import only has
# an effect on Python 2.
# It makes string literals as unicode like in Python 3
from __future__ import unicode_literals


import sys
import mock
import common
import config

ADDONS_SETTINGS = {
    'plugin.video.catchuptvandmore': config.ADDON_FAKE_SETTINGS,
    'script.module.codequick': config.CODEQUICK_FAKE_SETTINGS
}

ADDONS_LABELS = {
    'plugin.video.catchuptvandmore': config.ADDON_FAKE_LABELS,
    'script.module.codequick': config.CODEQUICK_FAKE_LABELS
}

ADDONS_NAME = {
    'plugin.video.catchuptvandmore': 'Catch-up TV & More',
    'script.module.codequick': 'CodeQuick'
}

ADDONS_PATHS = {
    'plugin.video.catchuptvandmore': config.ADDON_PATH,
    'script.module.codequick': common.CODEQUICK_ADDON_PATH
}

ADDONS_FANARTS = {
    'plugin.video.catchuptvandmore': common.ADDON_FANART_PATHFILE,
    'script.module.codequick': common.CODEQUICK_FANART_PATHFILE
}

ADDONS_ICONS = {
    'plugin.video.catchuptvandmore': common.ADDON_ICON_PATHFILE,
    'script.module.codequick': common.CODEQUICK_ICON_PATHFILE
}


class FakeAddon(object):
    def __init__(self, id='plugin.video.catchuptvandmore'):
        self._id = id
        self._settings = ADDONS_SETTINGS[self._id]
        self._labels = ADDONS_LABELS[self._id]
        self._name = ADDONS_NAME[self._id]
        self._path = ADDONS_PATHS[self._id]
        self._fanart = ADDONS_FANARTS[self._id]
        self._icon = ADDONS_ICONS[self._id]

    def getAddonInfo(self, info_id):
        result = ''
        if info_id == 'id':
            result = self._id
        elif info_id == 'name':
            result = self._name
        elif info_id == 'path':
            result = self._path
        elif info_id == 'fanart':
            result = self._fanart
        elif info_id == 'icon':
            result = self._icon
        elif info_id == 'profile':
            result = common.CONFIG_PATH
        else:
            raise Exception(
                'Need to complete getAddonInfo mock for info_id: ' + info_id)

        if config.ENABLE_MOCK_XBMCADDON_LOG:
            print('[FakeAddon] getAddonInfo of "' + info_id + '" --> "' + result + '"')
        return result

    def getSetting(self, setting_id):
        if config.ENABLE_MOCK_XBMCADDON_LOG:
            print('[FakeAddon] getSetting of "' + setting_id + '" --> "' + self._settings.get(setting_id, '') + '"')
        return self._settings.get(setting_id, '')

    def setSetting(self, _id, value):
        if config.ENABLE_MOCK_XBMCADDON_LOG:
            print('[FakeAddon] setSetting of "' + _id + '" --> "' + value + '"')
        self._settings[_id] = value

    def getLocalizedString(self, id_):
        if config.ENABLE_MOCK_XBMCADDON_LOG:
            print('[FakeAddon] getLocalizedString of ' + str(id_) + ' --> "' + self._labels.get(id_, str(id_)) + '"')
        return self._labels.get(id_, str(id_))



mock_xbmcaddon = mock.MagicMock()

mock_xbmcaddon.Addon.side_effect = FakeAddon

# Say to Python that the xbmcaddon module is mock_xbmcaddon
sys.modules['xbmcaddon'] = mock_xbmcaddon
