#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
from vbclient.common.i18n import _


class Backup(object):

    @staticmethod
    def add_volume_arg(parser):
        parser.add_argument(
            "volume",
            metavar="<volume>",
            help=_("Volume to backup (name or ID)")
        )

    @staticmethod
    def add_backup_name_arg(parser):
        parser.add_argument(
            "--name",
            metavar="<name>",
            help=_("Name of the backup")
        )

    @staticmethod
    def add_backup_desc_arg(parser):
        parser.add_argument(
            "--description",
            required=False,
            metavar="<description>",
            help=_("Description of the backup")
        )