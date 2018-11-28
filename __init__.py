# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

from wakeonlan import send_magic_packet

__author__ = 'RobBren'

LOGGER = getLogger(__name__)


class WakeOnLanSkill(MycroftSkill):
    def __init__(self):
        super(WakeOnLanSkill, self).__init__(name="WakeOnLanSkill")

    #@intent_handler(IntentBuilder("").require("Wake").require("Device"))
    @intent_handler(IntentBuilder("").require("Wake")) #.require("Device"))
    def handle_wake(self, message):

         #handle having a device name
         #device = message.data.get("Device")

         address = self.settings.get("address")

         #handle if device is not set
         #if not url_rs

         #handle invalid address

         send_magic_packet(address)

def create_skill():
    return WakeOnLanSkill()
