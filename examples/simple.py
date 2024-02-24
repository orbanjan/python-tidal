# -*- coding: utf-8 -*-

# Copyright (C) 2023- The Tidalapi Developers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""simple.py: A simple example script that describes how to get started using tidalapi"""

import tidalapi
from tidalapi import Quality
from pathlib import Path

session_file1 = Path("tidal-session-oauth.json")

session = tidalapi.Session()
# Load session from file; create a new OAuth session if necessary
session.login_session_file(session_file1)

session.audio_quality = Quality.hi_res_lossless.value

album_id = "71096074"
album = session.album(album_id)
tracks = album.tracks()
# list album tracks
print(album.name)
# list album tracks
for track in tracks:
    print("{}: '{}' by '{}'".format(track.id, track.name, track.artist.name))
    print(track.get_url())
