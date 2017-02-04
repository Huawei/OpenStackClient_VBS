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
from osc_lib.tests import utils

from vbclient.tests import fakes


class BaseTestCase(utils.TestCommand):
    """Base Test case class for all unit tests."""
    pass


class CloudEyeV1BaseTestCase(BaseTestCase):
    """Base test case class for Cloud Eye V1 management API."""

    def __init__(self, *args, **kwargs):
        super(CloudEyeV1BaseTestCase, self).__init__(*args, **kwargs)
        self.cmd = None

    def setUp(self):
        super(CloudEyeV1BaseTestCase, self).setUp()
        fake_cloudeye_client = fakes.FakeCloudEyeV1Client()
        self.app.client_manager.cloudeye = fake_cloudeye_client
