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

# In order to install a Go grader on Ubuntu 18.04, run
# apt install golang-go

"""Go programming language definition."""

from cms.grading import CompiledLanguage


__all__ = ["GoLang"]


class GoLang(CompiledLanguage):
    """This defines the Go Lang Programming language
    """
    
    @property
    def name(self):
        """See Language.name."""
        return "Go"

    @property
    def source_extensions(self):
        """See Language.source_extensions."""
        return [".go"]

    def get_compilation_commands(self,
                                 source_filenames, executable_filename,
                                 for_evaluation=True):
        """See Language.get_compilation_commands."""
        command = ["/usr/bin/go"]
        command += ["build",
                    "-o", executable_filename]
        command += source_filenames
        test = ["/usr/bin/test", "-x", executable_filename]
        return [command, test]
