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
import mock
import six
from osc_lib import utils

from vbclient.osc.v1 import job

from vbclient.tests import base
from vbclient.v1 import job_mgr
from vbclient.v1 import resource


@mock.patch.object(job_mgr.JobManager, "_get")
class TestShowJob(base.VolumeBackupBaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestShowJob, self).__init__(*args, **kwargs)
        self.job = {
            "status": "SUCCESS",
            "entities": {
                "bks_create_volume_name": "autobk_volume",
                "backup_id": "ba5401a2-7cd2-4c01-8c0d-c936ab412d6d",
                "volume_id": "7e5fdc5a-5e36-4b22-8bcc-7f17037290cc",
                "snapshot_id": "a77a96bf-dd18-40bf-a446-fdcefc1719ec"
            },
            "job_id": "4010b39b5281d3590152874bfa3b1604",
            "job_type": "bksCreateBackup",
            "begin_time": "2016-01-28T16:14:09.466Z",
            "end_time": "2016-01-28T16:25:27.690Z",
            "error_code": None,
            "fail_reason": None
        }

    def setUp(self):
        super(TestShowJob, self).setUp()
        self.cmd = job.ShowJob(self.app, None)

    def test_create_volume_backup(self, mocked_get):
        args = [
            "job-id-1",
        ]
        verify_args = [
            ("job_id", "job-id-1"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        mocked_get.return_value = resource.Job(
            mock.Mock(), self.job, "request-id"
        )
        columns, data = self.cmd.take_action(parsed_args)

        self.assertEqual(columns, [
            "Id",
            "Type",
            "Begin Time",
            "End Time",
            "Entities",
            "Status",
        ])

        # ????
        entities = "backup_id='c6be4287-6707-4f5b-84ef-07013851b60d', " \
            "bks_create_volume_name='autobk_volume', " \
            "snapshot_id='34f14aeb-cede-4e1b-8d9f-14a2c43bae9f', " \
            "volume_id='a5109cba-1b1f-4d40-b3a9-753bc808b66a' "


        print tuple([
            "4010b39b5281d3590152874bfa3b1604",
            "bksCreateBackup",
            "2016-01-28T16:14:09.466Z",
            "2016-01-28T16:25:27.690Z",
            entities,
            "SUCCESS",
        ])

        print entities
        self.assertEqual(tuple(data), tuple([
            "4010b39b5281d3590152874bfa3b1604",
            "bksCreateBackup",
            "2016-01-28T16:14:09.466Z",
            "2016-01-28T16:25:27.690Z",
            entities,
            "SUCCESS",
        ]))
