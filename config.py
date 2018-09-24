import sys
import os

VERSION = "1.0"
META_DIR = ".dolmades"
INST_DIR = "install"
# Python version major.minor
PY_VER = "%d.%d" % (sys.version_info[0], sys.version_info[1])
SELF_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))

DOLMADES_PATH = os.path.expanduser('~')+'/.dolmades'
REPO_PATH = DOLMADES_PATH + "/repo"
INST_PATH = DOLMADES_PATH + "/" + INST_DIR
