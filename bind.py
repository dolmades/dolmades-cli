#!/usr/bin/env python2

import subprocess
import os

from prettyprint import printx

try:
    BIND_DOWNLOAD  = '/wineprefix/drive_k/:'+subprocess.check_output(['xdg-user-dir', 'DOWNLOAD']).strip()+'/'
    BIND_DOCUMENT  = '/wineprefix/drive_d/:'+subprocess.check_output(['xdg-user-dir', 'DOCUMENTS']).strip()+'/'
    BIND_PICTURES  = '/wineprefix/drive_p/:'+subprocess.check_output(['xdg-user-dir', 'PICTURES']).strip()+'/'
    BIND_MUSIC     = '/wineprefix/drive_m/:'+subprocess.check_output(['xdg-user-dir', 'MUSIC']).strip()+'/'
    BIND_VIDEOS    = '/wineprefix/drive_v/:'+subprocess.check_output(['xdg-user-dir', 'VIDEOS']).strip()+'/'
    BIND_HOME      = '/wineprefix/drive_h/:'+os.getenv("HOME")+'/'
except:
    printx("ERROR: no xdg compliance given, binds in recipes probably broken!")

BIND_COM1   = "/dev/ttyS0:/dev/ttyS0"
BIND_COM2   = "/dev/ttyS1:/dev/ttyS1"
BIND_CDROM  = "/dev/sr0:/dev/sr0"
BIND_FLOPPY = "/dev/fd0:/dev/fd0"
