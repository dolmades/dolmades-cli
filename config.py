import sys
import os
import subprocess

# Python version major.minor
PY_VER = "%d.%d" % (sys.version_info[0], sys.version_info[1])

VERSION = "1.0"
META_DIR = ".dolmades"
INST_DIR = "install"

SELF_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
HOME = os.path.expanduser('~')

DOLMADES_PATH = HOME + '/.dolmades'
REPO_PATH = DOLMADES_PATH + "/repo"

try:
    DESK_PATH = subprocess.check_output(['xdg-user-dir', 'DESKTOP']).strip()
except:
    DESK_PATH = HOME + "/Desktop"

try:
    DL_PATH = subprocess.check_output(['xdg-user-dir', 'DOWNLOAD']).strip()
except:
    DL_PATH = HOME + "/Downloads"

try:
    DOC_PATH = subprocess.check_output(['xdg-user-dir', 'DOCUMENTS']).strip()
except:
    DOC_PATH = HOME + "/Documents"

INST_PATH = DOLMADES_PATH + "/" + INST_DIR

# TODO check if dirs exist and create them if neccessary!
