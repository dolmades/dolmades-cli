# "The Goglizer" - Dolmades v1.0 

## Introduction

Dolmades are intended as a mean to ease packaging, installation, usage and distribution of windows programs in Linux environments to the utmost extent. The current version is a prototype in python. 

This release focuses on basic features and GOG support. As of now a collection of a few command line tools represent the prototypical implementation of the underlying concepts:

* dolmades - to maintain your installed windows application
* goglizer - prepares win-only GOG games to be cooked; GOG account required
* cook - cooks a dolmade given a Dolmadefile and its ingredients

Right after cooking the windows application will be available as clickable shortcut on your desktop.
A global configuration file called `config.py` provides important settings to all three scripts.

Once the prototype is feature-complete I want to work on an enhanced followup version based on Qt combining a remote repository service. The primary goal will be to create a powerful GUI to setup, maintain and run Windows software under Linux.

### Requirements

* x86-64 linux
* Python 2.7
* curl
* tar with support of `-delay-directory-restore` (see https://github.com/indigo-dc/udocker/pull/137)

### Acknowledgements

Dolmades make heavy use of the following underlying technologies:

 * **Docker + DockerHub:** for the dolmades base images
 * **udocker + proot:** for user-level containerization
 * **wine + winetricks:** for running windows application in Linux
 * **lgogdownloader:** for GOG support

### Features

* **GOG gaming support:** generate template recipes for your personal GOG collection and installation is a breeze
* **Ease-of-use:** supports major linux distros and require no special permissions
* **Compatibility:** recipes create functional dolmades across various distros and system hardware
* **Mobility:** cooked dolmades are designed to be portable across various distros and system hardware
* **Safety&Security:** dolmades are isolated from each other and from the host system by default

* **Users**
  * **Creation:** cook your application using recipes and install a desktop symlink
  * **Target launcher:** displays a selection of all installed applications and you choose which one to run
  * **Shares:** bind selected paths from the host system to windows drives inside a dolmade
  * **Import&Export:** allows sharing of cooked dolmades - EXPERIMENTAL - requires user names to remain identical!
  
* **Developers:** 
  * **Create recipes:** use the existing Dolmadefiles as template for your own win-only apps
  * **Debug mode:** examine problems, add fixes and instantly rebuild the application
  * **Selectable base:** choose between between several wine versions


The focus in the v1.x release cycle will be put on support for gaming, the standardization of the `Dolmadefile` specification used to create recipes, the protoypical implementation of the basic concepts and the completion of major unresolved issues.

### Planned for the next release

* Improved Import&Export to work across changing user names
* Recipe specification: Gather feedback. Complete syntax. Standardize it.
* Lots of refactoring / bug fixing

## Basics

Dolmades makes use of several concepts which will be briefly explained here:

* **Dolmades:** Win apps which behave like containers. They can be created, deleted, executed and migrated.
* **Recipes:** Also Dolmadefiles; specification files which define the building process of a dolmade.
* **Ingredients:** Recipes require certain ingredients which can be ISO files, installers, images ...
* **Binds:** Dolmades are isolated by default but can access files or directories on the host system using shared binds 

### Setup

Either download the release tar ball
```
wget https://github.com/dolmades/dolmades-cli/archive/v1.0.tar.gz
tar -xzf v1.0.tar.gz
cd dolmades-cli-1.0/
```
or simply clone the latest master using git:
```
git clone https://github.com/dolmades/dolmades-cli.git
cd dolmades-cli
```

### Cooking a dolmade

Cooking describes the process of building a dolmade from a recipe and the required ingredients.
To cook a dolmade use the very simple example:

```
./cook Dolmadefile
```

At first the required ingredients will be downloaded. Then, the dolmade is being created and the installer is being run.
Click straight through the installation process. This will install the free game Broken Sword 2.5 on your desktop. It can be started by double clicking the desktop icon:

<p align="center">
  <img src="docs/shots/firstuse_0.png?raw=true" alt="screen shot 0"/>
</p>

or from terminal:
```
./dolmades launch Broken_Sword
```

Select `Windowed Mode` in the launcher and click "Ok":

<p align="center">
  <img src="docs/shots/firstuse_1.png?raw=true" alt="screen shot 1"/>
</p>

This will launch the game:

<p align="center">
  <img src="docs/shots/firstuse_2.png?raw=true" alt="screen shot 2"/>
</p>

A system tray icon indicates the running dolmade. On left click you can access the run log, on right click you can forcibly terminate the running dolmade in case the app hangs itself. 

More recipes for dolmades can be downloaded [here](https://github.com/dolmadefiles)

### Generating a GOG dolmade

For this to work you need to be registered at [GOG](https://gog.com). They offer some items for free so you can test `goglizer` without purchasing a game. This is how to cook your favourite GOG win-only game using the script `goglizer`:
```
./goglizer -u
```
The `-u` parameter tells `goglizer` to retrieve the dolmades runtime container and your personal game list.
At first, you will be asked to authorize using your GOG account. Since two-factor-authentication is mandatory you will need to check your email and enter the code that GOG sends to you. This needs to be done only once. 
After that, the authorization credentials are being stored in your home directory for subsequent use.
Finally a list of your games is being shown:

```
Found dolmade repo under /home/stefan/.dolmades/repo
Pulling dolmades runtime container...
da4bf27d-3bf2-3436-916a-e1bc83098523
done
Fetching detailed info about games from GOG...
Retrieving detailed linux game list...
Getting game names (1/1) 48 / 48
Getting game info 26 / 26
Retrieving detailed linux/windows game list...
Getting game names (1/1) 48 / 48
Getting game info 48 / 48
Retrieving detailed windows game list...
Getting game names (1/1) 48 / 48
Getting game info 48 / 48
done!
Windows games available on this account which have no linux installer available
broken_sword_3__the_sleeping_dragon
...
```

Note, that only games are being listed that have no corresponding linux installer. If you want linux games to be listed as well you need to use the `-l` parameter:

```
./goglizer -l
Found dolmade repo under /home/stefan/.dolmades/repo
Windows games available on this account (bold: no linux installer available)
akalabeth_world_of_doom
beneath_a_steel_sky
broken_sword_2__the_smoking_mirror
broken_sword_3__the_sleeping_dragon
...
```

Now choose a game of your liking and instruct `goglizer` to download the ingredients and create a corresponding dolmade file using the `-d` parameter:
```
./goglizer -d=broken_sword_3__the_sleeping_dragon
```
This will download its ingredients and prepare a Dolmadefile for installation. Now the dolmade can be installed:
```
./cook "broken_sword_3__the_sleeping_dragon:en:1.0.dolmade"
```
After successful completion you will find a clickable icon on your desktop :)

## Fixing issues

As of now for many games the installation procedure fails or the installed game won't work properly.
The goal of dolmades is to make it easy to find and apply fixes to the generated Dolmadefile in such cases. 
Let's generate the dolmadefile:
```
./goglizer -d=edna_harvey_the_breakout
```
Then, we try to cook it:
```
./cook edna_harvey_the_breakout:en.dolmade
```
The java installation will fail and leave a broken dolmade.
First, we need to figure out interactively what needs to be done:
```
./dolmades debug edna_harvey_the_breakout:en.dolmade

# THIS IS THE REQUIRED FIX: set windows version to WinXP
winetricks winxp

# rerun installer and ensure that it works now
/install/setup_edna_and_harvey_the_breakout_2.1.0.5.exe

# test cooked dolmade, start in windowed mode
targetSelector
```

The previous changes are now applied permanently to the dolmade but will get lost if it will be recooked.
That is why, secondly, we need to update the corresponing `dolmadefile`.
Edit `edna_harvey_the_breakout:en.dolmade` and add the following section right before the `RunUser` command which launches the installer using `wine`:
```
RunUser
 winetricks winxp

```

Finally, the dolmade can be cooked once more:
```
./cook edna_harvey_the_breakout:en.dolmade
```

This erases the previous dolmade and applies the fix permanently.

## Managing dolmades

Your dolmades are managed by `dolmades`

## Initialization

Initialization does two things:
* if it doesn't exist yet: initializing the dolmades directory under `DOLMADES_PATH`
* downloading the docker `runtime` container with the matching version and (re)create it

```
./dolmades init
```

### Listing
Lists the locally available dolmades:
```
./dolmades list
```

### Removal

Removes the given dolmade and frees up the allocated space:
```
./dolmades del name-of-dolmade
```
You can pass multiple dolmade names or sha256 container ids.

### Execution

Executes the `/.dolmades/start.sh` script which either runs the executable defined via `SetTarget` in the `dolmadefile`
or the target selector script which lets you choose between all installed targets.
```
./dolmades launch name-of-dolmade
```
### Debugging

It is possible to launch a bash inside the container. 
The installation directory will be available under `/install` and installed windows applications under `/wineprefix`.
Furthermore, the home directory of the calling user is available:
```
./dolmades debug name-of-dolmade
ls -lad $HOME /wineprefix /install
```
In rare cases you might to run as fake root, e.g. to install a missing package:
```
./dolmades root-debug runtime
apt-get update && apt-get -y install vim
```

If `name-of-dolmade` is given as argument the changes are being applied permanently.
If `name-of-base` is given as argument a temporary dolmade is being created and destroyed after the shell is being closed. `name-of-base` is used as template and currently can be one of the following:
* `runtime` - used internally by `dolmades`, `cook` and `goglizer`
* `base` - Ubuntu 16.04 LTS prepared for the installation of wine
* `winestable` - `base` with wine stable added and preconfigured
* `winedevel`- `base` with wine testing added and preconfigured

### Binding

It is possible to make files or directories of the host file system accessible from within the container by defining so-called binds. These will apply just when a dolmade is being executed but not when it is being debugged.

```
./dolmades binds name-of-dolmade
# listing the currently configured binds
```

```
./dolmades bind name-of-dolmade bind1 bind2 ...
```

A bind is defined as follows: `/dolmadedir/dolmadefile:/hostdir/hostfile` or `/dolmadedir/:/hostdir/`

*Notes* 
* This will create an empty file/directory in the dolmade if those do not exist already.
* The created files/directories in the dolmade persist even after the corresponding binds have been removed.
* As of now there is no possibility to bind raw devices such as `/dev/cdrom` to a wine drive!
* In wine the C and the Z drive are predefined. Utilize `/wineprefix/drive_x:/my/hostdir/` to bind to drive X.

### Migration (experimental)

It is possible to export and import a readily installed dolmade. 

```
./dolmades export Broken_Sword Broken_Sword.dme
```

```
./dolmades import Broken_Sword
```

The final goal is to be able to export the dolmade on some linux system running under some hardware and import it on another linux system running another hardware. Currently, this feature is experimental, and will only work if the user name remains the same. Also, things can stop working if the hardware changes, e.g. sound stops working, but can be fixed easily by running `winecfg` in debug mode.

### Serving

Last but not least the dolmade can be served on the desktop
```
./dolmades serve name-of-dolmade
```
This will create a clickable short cut on the desktop which will launch the corresponding dolmade. It can be safely deleted and recreated any time.

## Advanced

### Base Images
`dolmades` pulls its base images from DockerHub. The Dockerfiles specifying the build are available at https://github.com/dolmades-docker. As of now three images are available:

* winestable - current wine stable version
* winedevel - current wine development version
* winestaging - current wine staging version: development version + custom patches

The images for releases will be tagged accordingly and not being rebuilt in future. 
Images with the `latest` tag will be used for development and occasionally being rebuilt. 
This is what all images have in common:

* Ubuntu LTS 16.04 64-bit base with wine PPA
* Wine installation under `/wineprefix` with 32-bit prefix
* targetLauncher GUI script under `/usr/local/bin`
* `wget curl less vim` for convenience 

### Help

All available tools give help output:
```
./dolmades help
./dolmades help bind
./cook
./goglizer -h
```

### Configuration

Dolmades ships preconfigured but you may modify some settings to your liking in file `config.py`:

* `VERSION = "1.0"` - this is the utilized version of dolmades. It serves also as tag to be used for base docker images and it has to match the `VERSION` setting in the Dolmadefile. It is set to `latest` in branches and omitted in the recipes, it will be just set for releases.

* `DOLMADES_PATH = HOME + '/.dolmades'` - this is the base path where dolmades stores its runtime, icons and GOG games lists. Note: this affects which host directories you can bind. A bind is never allowed to contain `DOLMADES_PATH` since it would be a security issue!

* `REPO_PATH = DOLMADES_PATH + "/repo"` - this is the base path where dolmades stores its base images and dolmades plus their meta data. Note: this affects which host directories you can bind. A bind is never allowed to contain `REPO_PATH` since it would be a security issue!

All other settings are advised to be kept!

## Dolmadefile Syntax

A Dolmadefile is a specification which allows the guided build of the respective dolmade.
Dolmadefiles are for dolmades what Dockerfiles are for Docker except that most dolmades are not built fully automated and hence require interaction if a graphical installer is being used. 

The structure of a `Dolmadefile` is:
```
# Arbitrary comment...
COMMAND1
  ARGUMENTS
  FURTHER ARGUMENTS
  ...
  
COMMAND2
  ARGUMENTS
  ...
```
### Commands

```
DOLMADE
 Name_Of_The_Dolmade
```
This command is mandatory. It defines the name of the dolmade used internally by `dolmades`. Whitespaces are not allowed. 
This name is going to be used in the desktop symlink title with `_` characters converted into blanks.

```
VERSION
 1.0
```
This command is optional. It defines the tag of the base image pulled by the recipe, and has to match with the version reported by `cook`. Advised to be omitted in development, such that no version checking takes place, and the `latest` base image is being used.

```
BASE
 dolmades/winestable
```

This command is mandatory. It defines the DockerHub repository to be used. The tag of the image used is defined by `VERSION`.

```
DESCRIPTION
 A description of the contents of this dolmade
```

This command is optional. This description is stored inside the container and it is not being used yet.

```
INGREDIENT
 sha256
 filename
 description
 http://remote1
 ftp://remote2
 file://local3
 gog://remoteid
 ...
```
This command is repeatable and optional. For each ingredient used within the recipe one entry is needed.
The ingredient will be fetched from one of the locations defined and made available inside the container under `filename`.

```
RUNUSER
 cmd1 &&
 cmd2 &&
 ...  &&
 cmdN
``` 
This command is repeatable and optional. This command will be launched as the calling user in a bash environment inside the dolmade. [config.py:INST_PATH](https://github.com/dolmades/dolmades-cli/blob/d64513966aa3ba5b84dc22143ea527bde806683b/config.py#L80) will be the target directory.
You can cascade multiple commands by `&&` and they will be executed subsequently. The first failing command however will terminate the execution.

```
RUNROOT
 cmd1 &&
 cmd2 &&
 ...  &&
 cmdN
```

This command is repeatable and optional. This command will be launched as fake root in a bash environment inside the dolmade. [config.py:INST_PATH](https://github.com/dolmades/dolmades-cli/blob/d64513966aa3ba5b84dc22143ea527bde806683b/config.py#L80) will be the target directory.
You can cascade multiple commands by `&&` and they will be executed subsequently. The first failing command however will termine the execution. Usually `RUNUSER` should suffice but if you need to install some packages using `apt` `RUNROOT` will be required.

```
SETTARGET
 targetCall
``` 

This command is optional. If omitted the dolmade will launch using the target launcher and allow the user to select one of all installed targets i.e. lnk-files created during the installation. Sometimes it is desirable to launch a specific executable and then this option can be used to set the exe-binary.

```
SETTARGETARGS
 targetArgs
```

This command is optional. Sometimes if `SETTARGET` is used it is still neccessary to specify also some arguments. This can be done using this command.

```
ICON
 iconFileName
```

This command is optional. It specifies the icon file to be used for the desktop symbol and the target launcher.
If the icon filename is relative `/install` will be prepended. If the command is omitted it defaults to the dolmade icon.

**FINAL NOTES**

* There has to be an empty line in between subsequent commands
* Comments can be added as lines starting with `#`. Comments cannot be appended to existing command lines.
* The order of the commands has to be obeyed until parsing has been refactored. This is planned for the next release.
* The `INGREDIENT` - and maybe some other commands - are likely to undergo slight changes until the next release

## FAQ

 * Which distros have been tested? See [this issue](https://github.com/dolmades/dolmades-cli/issues/26)
 * Will dolmades focus on a particular distribution? I develop under Linux Mint, so Ubuntu and Debian-based distros might be most compatible
 * Will dolmade likely become a Linux distribution? No. I plan to support major distributions though.
 
 * requirements, limits, caveats...

## Future
Dolmades currently is a prototypical implementation done in python. 
Once it is feature-complete I want to work on an enhanced followup version based on Qt combining a remote repository service. The primary goal will be to create a powerful GUI to setup, maintain and run Windows software under Linux.

I figure some exciting use cases which would become addressable as well, e.g.

 * Automated deployment of windows software and complex development environments on large pools of computers
 * Cloud-based GUI applications based on Linux and VNC
 * Enhanced debugging and development for wine development
 * Fully automated dolmade cooking using Xvfb
 * Functional archival of legacy software
 * Support for complex Linux software setups

## Troubleshooting

* `udocker` requires Python 2.7 and will hopefully receive Python 3 support: https://github.com/indigo-dc/udocker/issues/77
* `dolmades` will be written to support Python 2.7 and bearing in mind Python 3 compatibility for later when udocker starts supporting it, too.
* 64bit linux kernel is needed due to the docker base images being built with x86-64 architecture. Technically it is possible to rebuild them using a 32bit linux kernel
* wine does not work well with pure x86-64 software which is why the installed windows software actually has to support 32-bit windows
* do not report issues to wine directly when `winetricks` has been used in the recipe, report them here instead!
* sometimes `udocker` fails to pull some layers from the docker registry (timeouts). Simply repeating the commands should help.
* GOG installer errors: many GOG games display error messages at the end of the installation process. I suspect some unsupported  facl commands are the source. The installed games seem to work anyways!

Last but not least: if you are in trouble check out the issues and open a new one if applicable.
