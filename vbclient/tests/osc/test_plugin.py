#   Copyright 2016 Huawei, Inc. All rights reserved.
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
import argparse

import mock
from osc_lib.tests import fakes

from vbclient.osc import plugin
from vbclient.tests import base


class TestCloudEyePlugin(base.BaseTestCase):
    @mock.patch('vbclient.v2.client.Client')
    def test_make_client_with_session(self, client):
        instance = mock.Mock()
        instance._api_version = {plugin.API_NAME: plugin.DEFAULT_API_VERSION}
        instance.session = mock.Mock()
        instance._cli_options = mock.Mock()
        instance._cli_options.config = mock.Mock()
        instance._cli_options.config.get.return_value = (
            "http://volume-backup.endpoint"
        )
        instance.region_name = fakes.REGION_NAME
        instance.interface = fakes.INTERFACE
        plugin.make_client(instance)

        client.assert_called_once_with(
            instance.session,
            "http://volume-backup.endpoint",
            region_name=fakes.REGION_NAME,
            interface=fakes.INTERFACE,
        )

    def test_plugin_parser(self):
        parser = argparse.ArgumentParser(description='TestUnit')
        plugin.build_option_parser(parser)

        parsed = parser.parse_args(['--os-vb-api-version',
                                    '1',
                                    '--os-vb-endpoint-override',
                                    'http://volume-backup.endpoint'])
        self.assertEqual(parsed.os_vb_api_version, "1")
        self.assertEqual(parsed.os_vb_endpoint_override,
                         'http://volume-backup.endpoint')
