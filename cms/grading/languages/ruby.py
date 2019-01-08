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

"""Ruby programming language definition."""

from cms.grading import Language


__all__ = ["Ruby"]


class Ruby(Language):
    """This defines the Ruby programming language, interpreted with the
    standard Ruby interpreter available in the system.

    """

    @property
    def name(self):
        """See Language.name."""
        return "Ruby"

    @property
    def source_extensions(self):
        """See Language.source_extensions."""
        return [".rb"]

    def get_compilation_commands(self,
                                 source_filenames, executable_filename,
                                 for_evaluation=True):
        """See Language.get_compilation_commands."""
        return [["/bin/cp", source_filenames[0], executable_filename]]

    def get_evaluation_commands(
            self, executable_filename, main=None, args=None):
        """See Language.get_evaluation_commands."""
        args = args if args is not None else []
        return [["/usr/bin/ruby", executable_filename] + args]
