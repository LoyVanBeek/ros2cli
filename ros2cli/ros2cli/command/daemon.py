# Copyright 2016-2017 Dirk Thomas
# Copyright 2017 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ros2cli.command import add_subparsers
from ros2cli.command import CommandExtension
from ros2cli.verb import get_verb_extensions


class DaemonCommand(CommandExtension):
    """Various daemon related sub-commands."""

    def add_arguments(self, parser, cli_name):
        self._subparser = parser
        # get verb extensions and let them add their arguments
        verb_extensions = get_verb_extensions('ros2cli.daemon.verb')
        add_subparsers(
            parser, cli_name, '_verb', verb_extensions, required=False)

    def main(self, *, parser, args):
        if not hasattr(args, '_verb'):
            # in case no verb was passed
            self._subparser.print_help()
            return 0

        extension = getattr(args, '_verb')

        # call the verb's main method
        return extension.main(args=args)
