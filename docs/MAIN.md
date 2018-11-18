# Dolmades 1.0 "the goglizer"

## Introduction

Dolmades are intended as a mean to ease packaging, installation and distribution of windows programs in Linux environments to the utmost extent. This release focuses on basic features and GOG support. As of now a collection of a few command line tools represent the prototypical implementation of the underlying concepts:

* dolmades - to maintain your installed windows application
* goglizer - prepares win-only GOG games to be cooked; GOG account required
* cook - cooks a dolmade given a Dolmadefile and its ingredients

Right after cooking the windows application will be available as clickable shortcut on your desktop.
A global configuration file called `config.py` provides important settings to all three scripts.

### Requirements

As of now:
* x86-64 linux
* Python 2.7
* curl
* tar with support of `-delay-directory-restore` (see https://github.com/indigo-dc/udocker/pull/137)

### Technical Base

Dolmades make heavy use of the following underlying technologies:

 * Docker + DockerHub: for the dolmades base images
 * udocker + proot: for user-level containerization
 * wine + winetricks: for running windows application in Linux
 * lgogdownloader: for GOG support

### Features

The focus in the 1.x release cycle will be put on support for gaming, the standardization of the `Dolmadefile` specification used to create recipes, the protoypical implementation of the basic concepts and the completion of major unresolved issues.

* **GOG gaming support:** generate template recipes for your personal GOG collection and installation is a breeze
* **Ease-of-use:** supports major linux distros and require no special permissions
* **Compatibility:** recipes create functional dolmades across various distros and system hardware
* **Mobility:** cooked dolmades are designed to be portable across various distros and system hardware
* **Safety&Security:** dolmades are isolated from each other and from the host system by default

* **Users**
  * **Creation:** cook your application using recipes and install a desktop symlink
  * **Target launcher:** displays a selection of all installed applications and you choose which one to run
  * **Shares:** bind selected paths from the host system to windows drives inside a dolmade
  * **Import&Export:** allows sharing cooked dolmades - EXPERIMENTAL - requires user names to remain identical!
  
* **Developers:** 
  * **Create recipes:** use the existing Dolmadefiles as template for your own win-only apps
  * **Debug mode:** examine problems, add fixes and instantly rebuild the application
  * **Selectable base:** choose between between several wine versions

### Planned for the next release

* Improved Import&Export to work across changing user names
* Recipe specification: Gather feedback. Complete syntax. Standardize it.
* Lots of refactoring / bug fixing

## Basic Usage

Dolmades makes use of several concepts which will be briefly explained here:

* **Dolmades:** Win apps which behave like containers. They can be created, deleted, executed and migrated.
* **Recipes:** Also Dolmadefiles; specification files which define the building process of a dolmade.
* **Ingredients:** Recipes require certain ingredients which can be ISO files, installers, images ...
* **Binds:** Dolmades are isolated by default but can access files or directories on the host system using shared binds 

### Setup

Either download the release tar ball under https://github.com/dolmades/dolmades-cli/releases or
simply clone the repository using git:

```
cd $HOME
git clone --branch the_goglizer https://github.com/dolmades/dolmades-cli.git
cd dolmades-cli
git checkout tags/1.0 -b the_goglizer
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
  <img src="shots/firstuse_0.png?raw=true" alt="screen shot 0"/>
</p>

or from terminal:
```
./dolmades launch Broken_Sword
```

Select `Windowed Mode` in the launcher and click "Ok":

<p align="center">
  <img src="shots/firstuse_1.png?raw=true" alt="screen shot 1"/>
</p>

This will launch the game:

<p align="center">
  <img src="shots/firstuse_2.png?raw=true" alt="screen shot 2"/>
</p>

A system tray icon indicates the running dolmade. On left click you can access the run log, on right click you can forcibly terminate the running dolmade in case the app hangs itself. 

### Generating a dolmade recipe using a GOG account

Here we gonna cook your favourite GOG win-only game using the script `goglizer`:
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

## Advanced Usage

### Development
### Versioning
### Base Images
### External Binds

## Tools

### dolmades
### goglizer
### cook
### config.py

## Dolmadefile Syntax

A Dolmadefile is a recipe or specification which allows the guided build of the respective dolmade.
Dolmadefiles are for dolmades what Dockerfiles are for Docker except that most dolmades are not built fully automated and hence require interaction e.g. when a graphical installer is used. 

The structure of a `Dolmadefile` is:
```
COMMAND
  ARGUMENTS
  FURTHER ARGUMENTS
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
WRITEMORE
 

**NOTES**

* Comments can be added as lines starting with `#`. Comments cannot be appended to existing command lines.
* The order of the commands has to be obeyed until parsing has been refactored. This is planned for the next release.
* The `INGREDIENT` - and maybe some other commands - are likely to undergo slight changes until the next release


## FAQ
...supported distros, requirements, limits, caveats, ...

## HOWTO
### Recipe creation HOWTO
### Migration HOWTO
### Copy-Protected CD/DVD Game HOWTO
...describe how we can install Harry Potter 1 and Harry Potter 2 from copy protected CD media
### Contribution HOWTO
   
## Roadmap

## Future
...next version, C++ rewrite, registry support...

## Troubleshooting
* `udocker` requires Python 2.7 and will hopefully receive Python 3 support: https://github.com/indigo-dc/udocker/issues/77
* `dolmades` will be written to support Python 2.7 and bearing in mind Python 3 compatibility for later when udocker starts supporting it, too.
* 64bit linux kernel is needed due to the docker base images being built with x86-64 architecture. Technically it is possible to rebuild them using a 32bit linux kernel
* wine does not work well with pure x86-64 software which is why the installed windows software actually has to support 32bit windows
* do not report issues to wine directly when `winetricks` has been used in the recipe, report them here instead!

## Acknowledgement
