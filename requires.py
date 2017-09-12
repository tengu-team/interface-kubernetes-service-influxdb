#!/usr/bin/env python3
# Copyright (C) 2016  Ghent University
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import yaml

from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class KubernetesServiceRequires(RelationBase):
    scope = scopes.GLOBAL

    @hook('{requires:kubernetes-service-influxdb}-relation-{joined}')
    def joined(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.joined')

    @hook('{requires:kubernetes-service-influxdb}-relation-{changed}')
    def changed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.joined')
        conv.set_state('{relation_name}.available')

    @hook('{requires:kubernetes-service-influxdb}-relation-{departed,broken}')
    def broken(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.joined')
        conv.remove_state('{relation_name}.available')

    def get_service_name(self):
        conv = self.conversation()
        return conv.get_remote('service_name', '')



