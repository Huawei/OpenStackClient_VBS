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
from osc_lib import utils

from vbclient.common import display
from vbclient.common import resource


class Job(resource.Resource, display.Display):
    """Volume Backup Job resource instance"""

    # {
    #     "status": "SUCCESS",
    #     "entities": {
    #         "bks_create_volume_name": "autobk_volume",
    #         "backup_id": "ba5401a2-7cd2-4c01-8c0d-c936ab412d6d",
    #         "volume_id": "7e5fdc5a-5e36-4b22-8bcc-7f17037290cc",
    #         "snapshot_id": "a77a96bf-dd18-40bf-a446-fdcefc1719ec"
    #     },
    #     "job_id": "4010b39b5281d3590152874bfa3b1604",
    #     "job_type": "bksCreateBackup",
    #     "begin_time": "2016-01-28T16:14:09.466Z",
    #     "end_time": "2016-01-28T16:25:27.690Z",
    #     "error_code": null,
    #     "fail_reason": null
    # }
    show_column_names = [
        "Id",
        "Type",
        "Begin Time",
        "End Time",
        "entities",
        "Status",
    ]

    column_2_property = {
        "Id": "job_id",
        "Type": "job_type",
    }

    formatter = {
        "entities": utils.format_dict
    }

    def get_show_column_names(self):
        column_names = self.show_column_names[:]
        if "fail_reason" in self.original and self.fail_reason:
            column_names.insert(5, "Fail Reason")
        if "error_code" in self.original and self.error_code:
            column_names.insert(5, "Error Code")
        return column_names

