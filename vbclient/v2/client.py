#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

LOGGER = logging.getLogger(__name__)


class Client(object):
    """Client for the HuaWei AutoScaling v2 API."""

    # service name registered in open-stack
    service_name = 'volume_backup'

    def __init__(self, session=None, endpoint=None, **kwargs):
        """Initialize a new client for the VBS v2 API.

        :param keystoneauth1.session.Session session:
            The session to be used for making the HTTP API calls.  If None,
            a default keystoneauth1.session.Session will be created.
        :param string endpoint:
            An optional URL to be used as the base for API requests on this API
        :param kwargs:
            Keyword arguments passed to keystoneauth1.session.Session().
        """

        from vbclient.common import httpclient
        from vbclient.v2 import backup_mgr
        from vbclient.v2 import restore_mgr

        # http_log_debug = utils.get_effective_log_level() <= logging.DEBUG
        default_options = {
            'service_name': self.service_name,
            'client_name': 'Volume Backup Client(HuaWei)',
            'client_version': 'V2',
            'logger': LOGGER,
        }
        kwargs.update(default_options)

        if endpoint:
            endpoint += '/v2/%(project_id)s'
        self.client = httpclient.OpenStackHttpClient(
            session, endpoint, **kwargs
        )
        self.backup_mgr = backup_mgr.VolumeBackupManager(self.client)
        self.restore_mgr = restore_mgr.VolumeBackupRestoreManager(self.client)
