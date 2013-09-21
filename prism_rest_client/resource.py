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

import types

class BaseResource(object):
    def __init__(self, uri, cache, data, metadata):
        self._uri = uri
        self._cache = cache
        self._data = data
        self._metadata = metadata


class Resource(BaseResource):
    def __init__(self, uri, cache, data, metadata, parent=None):
        BaseResource.__init__(self, uri, cache, data, metadata)
        self._parent = parent
        self._dirty = False

    def __getattr__(self, name):
        try:
            val = self._data.get(name)
        except KeyError:
            raise AttributeError, "'%r' has no attribute '%s'" % (self, name)
        obj = self._getObj(name, val)
        if obj is not None:
            return obj
        else:
            return val

    def __setattr__(self, name, value):
        if name.startswith('_'):
            object.__setattr__(self, name, value)
            return

        if name in self._data:
            val = self._data.get(name)
            if not self._setObj(val, name, value):
                self._dirty = True
                self._data[name] = value
        else:
            self._dirty = True

            if isinstance(value, list) and len(value) == 0:
                value = self.__class__(self._uri, self._cache, )

            self._data[name] = value

    def _getObj(self, name, val):
        if isinstance(val, types.StringTypes) and val.startswith('http://'):
            return self._cache.get(val)

        if isinstance(val, dict):
            if 'id' in val:
                return self._cache.get(val['id'])

            valId = id(val)
            if valId not in self._local_cache:
                self._local_cache[valId] = self.__class__(self._uri,
                        self._cache, data=val, metadata=self._metadata,
                        parent=self)
            return self._local_cache.get(valId)

    def _setObj(self, val, name, value):
        return False

    def persist(self):
        pass

    def delete(self):
        self._cache.delete(self._uri)

    def refresh(self, force=False):
        if not self._dirty or force:
            self._dirty = False
            self._local_cache = {}

            resource = self._cache.get(self._uri, cache=False)
            self._data = resource._data
            self._metadata = resource._metadata
