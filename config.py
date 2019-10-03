import sys
import os
import subprocess
import getpass
import shlex

from prettyprint import printitb
from platform import architecture
from prettyprint import printx

# Python version major.minor
PY_VER = "%d.%d" % (sys.version_info[0], sys.version_info[1])

VERSION = "1.2.0"

def MAJOR_VERSION():
    return '.'.join(VERSION.split('.')[0:2])

META_DIR = ".dolmades"
INST_DIR = "install"
INGR_DIR = "ingredients"

SELF_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
HOME = os.path.expanduser('~')
USER = getpass.getuser()

DOLMADES_PATH = HOME + '/.dolmades-' + MAJOR_VERSION()
INST_PATH = DOLMADES_PATH + "/" + INST_DIR
INGREDIENTS_PATH = DOLMADES_PATH + "/" + INGR_DIR

UDOCKER = SELF_PATH+"/udocker"
UDOCKERCMD_VERBOSE = UDOCKER
UDOCKERCMD_QUIET = UDOCKER+" --quiet"

UDOCKER_ENGINE="auto" # valid options: auto/S1/P1/P2
UDOCKER_ENGINE_PREFERENCE=['S1','P1','P2']

os.environ["UDOCKER_DIR"]=DOLMADES_PATH
# This is set for caching winetricks ingredients
os.environ["XDG_CACHE_HOME"]=INGREDIENTS_PATH
os.environ["BASH_ENV"]="/.dolmades/start.env"

if architecture()[0]=="32bit":
    RUNTIME_IMAGE="dolmades/runtime_i386"
    DOLMA_SUFFIX="_i386"
else:
    RUNTIME_IMAGE="dolmades/runtime"
    DOLMA_SUFFIX=""


def SETUP(dolmaname, mode=None):
    enginePreference=UDOCKER_ENGINE_PREFERENCE
    if (mode == None):
        mode = UDOCKER_ENGINE
    try:
        if (mode=="auto"):
            print("Trying to setup the best container engine...")
            for engine in enginePreference:
                cmdline=UDOCKERCMD_QUIET+" setup --execmode="+engine+" "+dolmaname
                print(cmdline)
                subprocess.call(cmdline, shell=True, close_fds=True)
                cmdline=UDOCKERCMD_QUIET+" run --user=$(whoami) "+dolmaname+" sleep 0"
                print(cmdline)
                subprocess.call(cmdline, shell=True, close_fds=True)
                safe_cmd=shlex.split(cmdline)
                proc=subprocess.Popen(safe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = proc.communicate()
                if (proc.returncode==0):
                   mode=engine
                   print("Success using "+mode)
                   return
            raise Exception("None of the available container engines is usable")
        if mode not in enginePreference:
            raise Exception("Unsupported container engine: " + mode)
        else:
            cmdline=UDOCKERCMD_QUIET+" setup --execmode="+mode+" "+dolmaname
            print(cmdline)
            subprocess.call(cmdline, shell=True, close_fds=True)
    except Exception as error:
        printx(error)

def INIT(force):
    printitb("Initializing dolmades under "+DOLMADES_PATH+"...")

    if not os.path.exists(DOLMADES_PATH):
        cmd = UDOCKER+" install "
        print(cmd)
        subprocess.call(cmd, shell=True, close_fds=True)
        untouched = False

    if (not os.path.exists(INST_PATH)):
        os.mkdir(INST_PATH, 0755)

    printitb("Storing dolmades python runscripts...")
    cmd = "tar --exclude-vcs -czpf "+DOLMADES_PATH+"/dolmades-bin.tgz -C "+SELF_PATH+" dolmades udocker cook goglizer config.py prettyprint.py box"
    subprocess.call(cmd, shell=True, close_fds=True)

    force_runtime_rebuild=False
    cmd = UDOCKERCMD_QUIET+" inspect dolmades-runtime"
    try:
        outp = subprocess.check_output(cmd, shell=True, close_fds=True, stderr=subprocess.STDOUT)
        if (outp != ""):
            printitb("Dolmades Runtime found!")
    except:
        force_runtime_rebuild=True

    if force_runtime_rebuild or force:
        printitb("Rebuilding dolmades runtime...")
        cmd = UDOCKERCMD_QUIET+" pull "+RUNTIME_IMAGE+":"+MAJOR_VERSION()
        print(cmd)
        printitb("Pulling dolmades runtime container...")
        subprocess.call(cmd, shell=True, close_fds=True)

        cmd = UDOCKERCMD_QUIET+" inspect dolmades-runtime"
        try:
            outp = subprocess.check_output(cmd, shell=True, close_fds=True, stderr=subprocess.STDOUT)
            if (outp != ""):
                cmd = UDOCKERCMD_QUIET+" rm dolmades-runtime"
                print(cmd)
                subprocess.call(cmd, shell=True, close_fds=True)
        except:
            pass

        cmd = UDOCKERCMD_QUIET+" create --name=dolmades-runtime "+RUNTIME_IMAGE+":"+MAJOR_VERSION()
        print(cmd)
        subprocess.call(cmd, shell=True, close_fds=True)

        SETUP("dolmades-runtime")

    if (not os.path.exists(DOLMADES_PATH+"/containers/dolmades-runtime/ROOT/"+META_DIR)):
        os.mkdir(DOLMADES_PATH+"/containers/dolmades-runtime/ROOT/"+META_DIR, 0755)

    if (not os.path.exists(INGREDIENTS_PATH)):
        os.mkdir(INGREDIENTS_PATH, 0755)

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

# TODO check if dirs exist and create them if neccessary!
