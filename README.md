<p align="center">
  <img src="https://dolmades.org/files/dolmade_xxl.png" width="140" alt="screen shot asd lifeforce"/>
</p>

# Dolmades v1.1 - "From Blue to Green"

## Introduction

Dolmades are intended as a mean to ease packaging, installation, usage and distribution of Windows applications in Linux environments to the utmost extent. 

### Features

The focus of the v1.x release cycle will be put on support for gaming, the standardization of the recipe specification used to create dolmades, ingredients handling, the protoypical implementation of the basic concepts and the completion of major unresolved issues.

* **Usage**
  * **Creation:** cook your application using recipes and create a desktop symlink and menu entry
  * **Target launcher:** displays a selection of all installed applications and you choose which one to run
  * **Shares:** bind selected paths from the host system to internal windows drives
  * **Import&Export:** share your cooked dolmades as standalone executables or import them elsewhere
  
* **Development:** 
  * **Create recipes:** use the existing recipes as template for your own win-only apps
  * **Debug mode:** examine problems, add fixes and instantly rebuild the application
  * **Selectable base:** choose between between several wine versions
  * **GOG gaming support:** generate template recipes for your personal GOG collection

Dolmades offer the following features over existing alternatives:
* **Ease of use:** supports major linux distros and requires no special permissions
* **Compatibility:** recipes create functional dolmades across various distros and system hardware
* **Mobility:** cooked dolmades are designed to be executable across various distros and system hardware
* **Safety&Security:** dolmades are isolated from each other and from the host system by default

## Prototypical Implementation 
The current implementation is a prototype in Python and focuses on basic features and GOG support. 

As of now a collection of a few command line scripts represent the prototypical implementation of the underlying concepts:

* `dolmades` - to maintain your installed windows applications
* `cook` - cooks a dolmade given a recipe and its ingredients
* `box` - creates a standalone installer from a cooked dolmade
* `goglizer` - creates template recipes for win-only GOG games; GOG account required
* `config.py` - a configuration file providing important settings

## Long-term Goal
Once the prototype is feature-complete I want to work on an enhanced version based on Qt and a remote repository service where user can store their dolmades, ingredients and recipes.

### Requirements

* x86 Linux (32 or 64 bit) with X.Org and xdg-compliant desktop environment
* Python 2.7
* tar+gzip+curl

### Acknowledgements

Dolmades make use of the following underlying technologies:

 * **Docker + DockerHub:** for the dolmades base images
 * **udocker + proot:** for user-level containerization
 * **wine:** for running windows application in Linux
 * **winetricks:** for installing most common ingredients
 * **lgogdownloader:** for GOG support
 * **makeself:** for creating standalone installers

### Changelog

v1.1 "From Blue To Green" - *TBD*

* Support creation of self-installable dolmades
* Import&Export working reliably now even when user name changes
* Support for 32 bit kernels
* Improved recipe specification
* Improved ingredients handling
* Lots of refactoring / bug fixing
* Beautification (concept, textual output, code)
* Improved documentation
* Updated base images to Wine 4

v1.0 "The Goglizer" - *2018-11-27*
* Initial release


## Basics

Dolmades makes use of several concepts which will be briefly explained here:

* **Dolmades:** Win apps which behave like containers. They can be created, deleted, executed and migrated.
* **Recipes:** Specification files similar to Dockerfiles which define the building process of a dolmade.
* **Ingredients:** Recipes require certain ingredients which can be ISO files, installers, media files ...
* **Binds:** Files contained in dolmades are isolated by default but access to files or directories on the host system can be configured using shared binds 

### Setup

Either download the release tar ball
```
curl -L -o dolmades.tgz https://github.com/dolmades/dolmades-cli/archive/v1.1.tar.gz
tar -xzf dolmades.tgz
cd dolmades-cli-1.1/
```
or simply clone it using git:
```
git clone -b "v1.1" --single-branch --depth 1 https://github.com/dolmades/dolmades-cli.git
cd dolmades-cli
```

### Cooking a dolmade

Cooking describes the process of building a dolmade from a recipe given its required ingredients.
To cook a dolmade use the very simple example:

```
./cook recipes/ASD_LifeForce.dolmade
```

This will install the winning demo of Assembly 2007 by Andromeda Software Development.
At first the required ingredients will be downloaded and verified by its checksum. 
Next, the dolmade is created and the installation as defined in the recipe is being performed.
Finally, you can run the installed dolmade:
```
./dolmades launch LifeForce_ASD
```

<p align="center">
  <img src="shots/firstuse_asd_lifeforce.png?raw=true" alt="screen shot asd lifeforce"/>
</p>

The dolmade can now be uninstalled again:
```
./dolmades del LifeForce_ASD
```

Now a second example: the free (as in beer) adventure game "Broken Sword":

```
./cook recipes/Broken_Sword.dolmade --serve
```

This will create the dolmade and add menu entries and a desktop symbol.

```
./cook launch Broken_Sword
```

<p align="center">
  <img src="shots/firstuse_0.png?raw=true" alt="screen shot 0"/>
</p>

A launcher will appear and offer you multiple choices created by the installer.
Select `Windowed Mode` and click "Ok":

<p align="center">
  <img src="shots/firstuse_1.png?raw=true" alt="screen shot 1"/>
</p>

The game will be started. You should be hearing sound unless wine detects the wrong alsa device is which still may happen on some hardware.

<p align="center">
  <img src="shots/firstuse_2.png?raw=true" alt="screen shot 2"/>
</p>

A system tray icon indicates the running dolmade. On left click you can access the run log, on right click you can forcibly terminate the running dolmade in case it hangs. 
The dolmade can be removed via the corresponding menu entry.

More recipes for dolmades can be downloaded [here](https://github.com/dolmadefiles)

### Generating a GOG dolmade

For this to work you'll need to be registered at [GOG](https://gog.com). They offer some items for free so you can test `goglizer` without purchasing a game. If you have not done so already obtain the free item "Flight of the Amazon Queen" and verify that it is shown in your personal game collection. Retrieve a list of your games using the script `goglizer`:
```
./goglizer -u
```
The `-u` parameter tells `goglizer` to retrieve the dolmades runtime container and your personal game list.
At first, you will be asked to authorize using your GOG account. Since two-factor-authentication is mandatory you will need to check your email and enter the code that GOG has sent to you. This needs to be done only once since the authorization credentials are being stored in your home directory for subsequent use.
Finally, a list of your games is displayed:

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
flight_of_the_amazon_queen
...
```

Note, that only games are listed that have no linux installer. If you want linux games to be listed as well you need to use the `-l` parameter:

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

Now choose a game of your liking and instruct `goglizer` to download the ingredients and create a corresponding recipe template using the `-d` parameter:
```
./goglizer -d=flight_of_the_amazon_queen
```
Now the dolmade can be installed:
```
./cook "flight_of_the_amazon_queen:en:1.1.dolmade" --serve
```
After successful completion you will find a clickable icon on your desktop and a menu entry :)
You can skip the `goglizer` run completely by using the recipe under `recipes/flight_of_the_amazon_queen:en:1.1.dolmade`.

## Fixing issues

As of now for one out of two games the installation procedure fails or the installed game won't work properly.
If that happens dolmades makes it easy to find and apply fixes to the generated Dolmadefile.
Let's give an real example:
```
./goglizer -d=edna_harvey_the_breakout
```
We try to cook it:
```
./cook edna_harvey_the_breakout:en.dolmade
```
The java installation will fail and leave a broken dolmade.
First, we need to figure out interactively what needs to be done:
```
./dolmades debug edna_harvey_the_breakout:en.dolmade

> # THIS IS THE REQUIRED FIX: set windows version to WinXP
> winetricks winxp

> # rerun installer and ensure that it works now
> /install/setup_edna_and_harvey_the_breakout_2.1.0.5.exe

# test cooked dolmade, start in windowed mode
targetSelector
```

The previous changes are now applied permanently to the dolmade but will get lost if it will be recooked.
That is why we ought to update the corresponing recipe to include that fix.
Edit `edna_harvey_the_breakout:en.dolmade` and add the following section right before the `RunUser` command which launches the installer using `wine`:
```
RunUser
 winetricks winxp

```

Finally, the dolmade can be cooked once more:
```
./cook edna_harvey_the_breakout:en.dolmade
```

This erases the previous dolmade and helps keeping recipe and cooked dolmade in sync with each other.

## Installable Dolmades
Once a dolmade has been cooked and thoroughly tested it is possible to convert it into a standalone installer:

```
./box LifeForce_ASD
```
This will package all dependencies and create an offline installer script based on `makeself` which installs on various Linux systems without special privileges.
The approximate size overhead produced by the Ubuntu Base Image and the wineprefix will be 800M.

Users who download this file can select it in the "Downloads" folder, and open up a terminal via right click.
The installer can then be run like this:
```
sh LifeForce_ASD.dme.sh
```
grant executable permissions via right click.
Depending on the desktop environment it may be possible to execute the script when double clicked if executable permissions have been granted beforehand via right click.
Unfortunately many desktop environments do not allow this. The method via terminal is more reliable.

*Note: as of now self-installable Dolmades will require Python 2.7 on the host system. A future release will probably get rid of this requirement.*

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

Removes the given dolmade (data, menu entries and desktop symbols) and frees up the allocated space:
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
In rare cases you might want to run as fake root, e.g. to install a missing package:
```
./dolmades root-debug runtime
apt-get update && apt-get -y install vim
```

If `name-of-dolmade` is given as argument the changes are being applied permanently.
If `name-of-base` is given as argument a temporary dolmade is being created and destroyed after the shell is being closed. `name-of-base` is used as template and currently can be one of the following:
* `runtime` - used internally by `dolmades`, `cook` and `goglizer`
* `base` - Ubuntu 18.04 LTS prepared for the installation of wine
* `winestable` - `base` with wine stable added and preconfigured
* `winedevel`- `base` with wine testing added and preconfigured

### Binding

It is possible to make files or directories of the host file system accessible from within the container by defining so-called binds. These will apply just when a dolmade is being launched but not when it is being debugged.

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

### Migration

It is possible to export and import a readily installed dolmade. 

```
./dolmades export Broken_Sword Broken_Sword.dme
```

```
./dolmades import Broken_Sword
```

The final goal is to be able to export the dolmade on some linux system running under some hardware and import it on another linux system running another hardware. Since the user name will likely change all users home directories are shared and being symlinked to `root`. Also, things can stop working if the hardware changes, e.g. sound stops working, but can be fixed easily by running `winecfg` in debug mode.

### Menu entries and desktop symbols

Last but not least the dolmade can be served on the desktop
```
./dolmades serve name-of-dolmade
```
This will create a clickable icon on the desktop and a sub-menu entry which will launch the corresponding dolmade. In addition a menu entry for uninstallation is created.
It is possible to remove the menu entries and the desktop symbol again without uninstalling the dolmade:
```
./dolmades clearaway name-of-dolmade
```

## Advanced

### Base Images
`dolmades` pulls its base images from DockerHub. The Dockerfiles specifying the build are available at https://github.com/dolmades-docker. As of now four images are available:

* winestable - current wine stable version
* winestable_i386 - current wine stable version (32 bit)
* winestaging - current wine staging version: development version + custom patches
* winestaging_i386 - current wine staging version: development version + custom patches (32  bit)

The images for releases will be tagged accordingly and not being rebuilt in future. 
Images with the `latest` tag are occasionally being rebuild, may break and are therefore reserved for internal development.
This is what all images have in common:

* Ubuntu LTS 18.04 base with wine PPA
* Wine installation under `/wineprefix` with 32-bit prefix
* `yad` for graphical installation/uninstallation
* `targetLauncher` GUI script under `/usr/local/bin`
* `wget curl less vim` for convenience 

It is possible to create custom docker images on DockerHub as base for recipes which e.g. offer legacy wine, gallium9, pba or Proton support.

### Help

All available tools give help output:
```
./dolmades help
./dolmades help bind
./cook
./box
./goglizer -h
```

### Configuration

Dolmades ships preconfigured but you may modify some settings to your liking in file `config.py`:

* `VERSION = "1.1"` - this is the utilized version of dolmades. It serves also as tag to be used for base docker images and it has to match the `VERSION` setting in the Dolmadefile. It is set to `latest` in branches and omitted in the recipes, it will be just set for releases.

* `DOLMADES_PATH = HOME + '/.dolmades'` - this is the base path where dolmades stores its runtime, base images, dolmades, meta data, icons and GOG games lists. Note: this affects which host directories you can bind. A bind is never allowed to contain `DOLMADES_PATH` since it would be a security issue!

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
 1.1
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
You can cascade multiple commands by `&&` and they will be executed subsequently. The first failing command, however, will terminate the execution. If all commands succeed a final `wineserver --wait` ensures the proper termination of all wine processes.

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
TARGET
 targetCall
``` 

This command is optional. If omitted the dolmade will launch using the target launcher and allow the user to select one of all installed targets i.e. lnk-files created during the installation. Sometimes it is desirable to launch a specific executable and then this option can be used to set the exe-binary.

```
TARGETARGS
 targetArgs
```

This command is optional. Sometimes if `TARGET` is used it is neccessary to also specify arguments. This can be done using this command.

```
TARGETENV
 targetEnv
```

This command is optional. Sometimes it is necessary to set some environment variables for an executable.
For instance it is possible to force [DLL overrides](recipes/ASD_LifeForce.dolmade) or specific language settings.

```
TARGETPROLOGUE
 targetPrologue
```

This command is optional. Sometimes it is necessary to call `wine` using a preceding command e.g. `taskset -c 0 wine` in order to limit the execution to a single CPU. This can help fix race conditions.

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
 * Will dolmades focus on a particular distribution? I develop under Linux Mint, so Ubuntu and Debian-based distros might be most compatible. I plan to keep compatibility to major distributions though.
 * Why does the syntax for the recipes change? As of now the syntax may change for **every** version. This does not matter since dolmades recipes will work when the `VERSION` of the recipe matches the `dolmades` run script. Exported dolmades will contain all scripts necessary to rebuild and rerun the dolmade.
 * Will the syntax for the recipes be fixed anytime? Probably. But not in the prototypical implementation phase. 
 * Will dolmades support ever MacOSX or Windows? Maybe. But not for the foreseeable future.
 * Is it enough to lookup ingredients by SHA256? TODO

## Future

Dolmades currently is a prototypical implementation done in python. 
Once it is feature-complete I want to work on an enhanced version based on Qt combining a remote repository service. The primary goal will be to create a powerful GUI to setup, maintain and run Windows software under Linux.

I figure some exciting use cases which would become addressable as well, e.g.

 * Automated deployment of windows software and complex development environments on large pools of computers
 * Cloud-based GUI applications based on Linux and VNC
 * Enhanced debugging and development for wine development
 * Fully automated dolmade cooking using Xvfb / AutoHotKey
 * Functional archival of legacy software
 * Support for complex Linux software setups

## Troubleshooting

* `udocker` requires Python 2.7 and will hopefully receive Python 3 support: https://github.com/indigo-dc/udocker/issues/77
* `udocker` requires tar with support of `-delay-directory-restore` (see https://github.com/indigo-dc/udocker/pull/137) which every recent distro should provide
* `dolmades` will be written to support Python 2.7 and bearing in mind Python 3 compatibility for later when udocker starts supporting it, too.
* wine does not work well with pure x86-64 software which is why the installed windows software actually has to support 32-bit windows
* do not report issues to wine directly when `winetricks` has been used in the recipe
* sometimes `udocker` fails to pull some layers from the docker registry (timeouts) - simply repeating the commands should help.
* GOG installer errors: many GOG games display error messages at the end of the installation process. I suspect some failing installer script commands are the source. The installed games seem to work anyways! According to [this post](https://wp.xin.at/archives/tag/out-of-global-vars-range) these messages even occur on Windows machines!

Last but not least: if you are in trouble, check out the issues and open a new one if applicable.
