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

"""Kotlin programming language definition."""

from cms.grading import Language


__all__ = ["Kotlin"]


class Kotlin(Language):
    """This defines the Kotlin programming language.
   
    Kotlin compiles to a Java jar file.
    """

    @property
    def name(self):
        """See Language.name."""
        return "Kotlin"

    @property
    def source_extensions(self):
        """See Language.source_extensions."""
        return [".kt"]

    def get_compilation_commands(self,
                                 source_filenames, executable_filename,
                                 for_evaluation=True):
        """See Language.get_compilation_commands."""
        return [["/snap/kotlin/current/bin/kotlinc", source_filenames[0], "-include-runtime", "-d", "%s.jar" % executable_filename], ["/bin/mv", "%s.jar" % executable_filename, executable_filename]]

    def get_evaluation_commands(
            self, executable_filename, main=None, args=None):
        """See Language.get_evaluation_commands."""
        args = args if args is not None else []
        return [["/bin/mv", executable_filename, "%s.jar" % executable_filename], ["/usr/bin/java", "-jar", "%s.jar" % executable_filename] + args]
