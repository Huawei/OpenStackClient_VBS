#   Copyright 2016 Huawei, Inc. All rights reserved.
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
import logging

from osc_lib import utils
from osc_lib.command import command

from vbclient.common.i18n import _
from vbclient.osc.v1 import parser_builder as pb

LOG = logging.getLogger(__name__)


class CreateVolumeBackup(command.Command):
    _description = _("Create new volume backup (HuaWei custom)")

    def get_parser(self, prog_name):
        parser = super(CreateVolumeBackup, self).get_parser(prog_name)
        pb.Backup.add_volume_arg(parser)
        pb.Backup.add_backup_name_arg(parser)
        pb.Backup.add_backup_desc_arg(parser)
        return parser

    def take_action(self, args):
        volume_client = self.app.client_manager.volume
        volume_id = utils.find_resource(volume_client.volumes, args.volume).id
        mgr = self.app.client_manager.volume_backup.backup_mgr
        job = mgr.create(volume_id, name=args.name, description=args.description)
        return 'Request Received, job id: ' + job['job_id']
