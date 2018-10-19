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

UDOCKER = SELF_PATH+"/udocker"
UDOCKERCMD_VERBOSE = UDOCKER+" --repo="+REPO_PATH
UDOCKERCMD_QUIET = UDOCKER+" --quiet --repo="+REPO_PATH

def INIT():
    print("Preparing directories...")

    untouched = True
    if not os.path.exists(DOLMADES_PATH):
        os.mkdir(DOLMADES_PATH, 0755)
        untouched = False
    try:
        if (os.path.exists(REPO_PATH)):
            os.rmdir(REPO_PATH)
            untouched = False
    except:
        pass

    if not os.path.exists(REPO_PATH):
        cmd = UDOCKER+ " mkrepo "+REPO_PATH
        print(cmd)
        subprocess.call(cmd, shell=True, close_fds=True)
        untouched = False

    if (not os.path.exists(INST_PATH)):
        os.mkdir(self.INST_PATH, 0755)
        untouched = False
    if (untouched):
        print("found dolmade repo under " + REPO_PATH)
    else:
        print("initialized dolmade repo under " + REPO_PATH)

    print("Preparing runtime...")
    cmd = UDOCKERCMD_QUIET+" pull dolmades/runtime:"+VERSION
    print(cmd)
    print("Pulling dolmades runtime container...")
    subprocess.call(cmd, shell=True, close_fds=True)

    cmd = UDOCKERCMD_QUIET+" rm dolmades-runtime"
    print(cmd)
    subprocess.call(cmd, shell=True, close_fds=True)

    cmd = UDOCKERCMD_QUIET+" create --name=dolmades-runtime dolmades/runtime:"+VERSION
    print(cmd)
    subprocess.call(cmd, shell=True, close_fds=True)
    print("done")

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
