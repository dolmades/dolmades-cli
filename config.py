import sys
import os
import subprocess

VERSION = "latest"
META_DIR = ".dolmades"
INST_DIR = "install"
# Python version major.minor
PY_VER = "%d.%d" % (sys.version_info[0], sys.version_info[1])
SELF_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))

DOLMADES_PATH = os.path.expanduser('~')+'/.dolmades'
REPO_PATH = DOLMADES_PATH + "/repo"
INST_PATH = DOLMADES_PATH + "/" + INST_DIR

try:
    DESK_PATH = subprocess.check_output(['xdg-user-dir', 'DESKTOP']).strip()
except:
    DESK_PATH = os.path.expanduser("~/Desktop")
