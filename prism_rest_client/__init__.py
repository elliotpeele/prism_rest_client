#
# Copyright (c) Elliot Peele <elliot@bentlogic.net>
#
# This program is distributed under the terms of the MIT License as found
# in a file called LICENSE. If it is not present, the license
# is always available at http://www.opensource.org/licenses/mit-license.php.
#
# This program is distributed in the hope that it will be useful, but
# without any warrenty; without even the implied warranty of merchantability
# or fitness for a particular purpose. See the MIT License for full details.
#

"""
RESTful client library, meant to be used with REST APIs generated by prism_rest
and possibly others.
"""

from .client import Client
from .cache import InstanceCache

def open(uri, headers=None, verify=False):
    return InstanceCache(Client(headers=headers, verify=verify)).get(uri)
