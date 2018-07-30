# Copyright 2015 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""remove service related

Revision ID: 2774a42c7163
Revises: 12a57080b278
Create Date: 2015-11-26 15:47:51.161749

"""

# revision identifiers, used by Alembic.
revision = '2774a42c7163'
down_revision = '12a57080b278'

from alembic import op


def upgrade(active_plugins=None, options=None):
    # commands auto generated by Alembic - please adjust! #
    op.drop_table('servicecontexts')
    op.drop_table('deviceservicecontexts')
    op.drop_table('servicedevicebindings')
    op.drop_table('serviceinstances')
    # end Alembic commands #
