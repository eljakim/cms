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

# In order to install a Visual Basic grader on Ubuntu 18.04, run
# apt install mono-vbnc

"""Visual Basic programming language definition."""

from cms.grading import Language


__all__ = ["VisualBasic"]


class VisualBasic(Language):
    """This defines the Visual Basic programming language, interpreted by
    first compiling to mono using vbnc, and then running with the mono interpreter.
    """

    @property
    def name(self):
        """See Language.name."""
        return "Visual Basic"

    @property
    def source_extensions(self):
        """See Language.source_extensions."""
        return [".vb"]

    def get_compilation_commands(self,
                                 source_filenames, executable_filename,
                                 for_evaluation=True):
        """See Language.get_compilation_commands."""
        return [["/usr/bin/vbnc", "-out:%s" % executable_filename, source_filenames[0]]]

    def get_evaluation_commands(
            self, executable_filename, main=None, args=None):
        """See Language.get_evaluation_commands."""
        args = args if args is not None else []
        return [["/usr/bin/mono", executable_filename] + args]
