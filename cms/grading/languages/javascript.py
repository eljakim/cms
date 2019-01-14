#!/usr/bin/env python3

# Contest Management System - http://cms-dev.github.io/
# Copyright © 2019 Eljakim Schrijvers <eljakim@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Javascript programming language definition."""

# In order to setup JavaScript on Ubuntu 18.04 run
# apt install nodejs

from cms.grading import Language


__all__ = ["JavaScript"]


class JavaScript(Language):
    """This defines the Javascript programming language, interpreted with the
    standard Javascript interpreter available in the system.

    """

    @property
    def name(self):
        """See Language.name."""
        return "JavaScript"

    @property
    def source_extensions(self):
        """See Language.source_extensions."""
        return [".js"]

    def get_compilation_commands(self,
                                 source_filenames, executable_filename,
                                 for_evaluation=True):
        """See Language.get_compilation_commands."""
        return [["/bin/cp", source_filenames[0], executable_filename]]

    def get_evaluation_commands(
            self, executable_filename, main=None, args=None):
        """See Language.get_evaluation_commands."""
        args = args if args is not None else []
        return [["/usr/bin/node", executable_filename] + args]
