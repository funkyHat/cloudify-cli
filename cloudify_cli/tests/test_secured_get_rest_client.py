########
# Copyright (c) 2015 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############

import os
import unittest

from cloudify_cli import utils
from cloudify_cli.constants import CLOUDIFY_USERNAME_ENV
from cloudify_cli.constants import CLOUDIFY_PASSWORD_ENV


class TestGetRestClient(unittest.TestCase):

    def test_get_rest_client(self):
        os.environ[CLOUDIFY_USERNAME_ENV] = 'test_username'
        os.environ[CLOUDIFY_PASSWORD_ENV] = 'test_password'
        self.assertIsNotNone(os.environ[CLOUDIFY_USERNAME_ENV],
                             'expected {0} to be test_username but it is None'
                             .format(CLOUDIFY_USERNAME_ENV))
        print 'os.environ[CLOUDIFY_USERNAME_ENV] = {0}'\
            .format(os.environ[CLOUDIFY_USERNAME_ENV])
        client = utils.get_rest_client(
            manager_ip='localhost', rest_port=80)
        self.assertIsNotNone(client._client.encoded_credentials)
