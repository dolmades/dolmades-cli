# Dolmades 1.0 "the goglizer"

## Introduction

Dolmades are intended as a mean to ease packaging, installation and distribution of windows programs in Linux environments to the utmost extent. This release focuses on basic features and GOG support. As of now a collection of a few command line tools represent the prototypical implementation of the underlying concepts:

* dolmades - to maintain your installed windows application
* goglizer - prepares win-only GOG games to be cooked; GOG account required
* cook - cooks a dolmade given a Dolmadefile and its ingredients

Right after cooking the windows application will be available as clickable shortcut on your desktop.
A global configuration file called `config.py` provides important settings to all three scripts.

### Requirements

As of now 
* x86-64 linuxes only
* Python 2.7
* curl
* tar with support of `-delay-directory-restore` (see https://github.com/indigo-dc/udocker/pull/137)

Notes
* `udocker` requires Python 2.7 and will hopefully receive Python 3 support: https://github.com/indigo-dc/udocker/issues/77
* `dolmades` will be written to support Python 2.7 and bearing in mind Python 3 compatibility for later when udocker starts supporting it, too.
* 64bit linux kernel is needed due to the docker base images being built with x86-64 architecture. Technically it is possible to rebuild them using a 32bit linux kernel
* wine does not work well with pure x86-64 software which is why the installed windows software actually has to support 32bit windows

### Technical Base

Dolmades make heavy use of the following underlying technologies:

 * Docker+DockerHub: for the dolmades base images
 * udocker + proot: for user-level containerization
 * wine + winetricks: for running windows application in Linux

### Features

* **GOG games support:** generate template recipes for your personal GOG collection and installation is a breeze
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

## Basics

Dolmades makes use of several concepts which will be briefly explained here:

* **Dolmades:** Win apps which behave like containers. They can be created, deleted, executed and migrated.
* **Recipes:** Specification files which define the building process of a dolmade.
* **Ingredients:** Recipes require certain ingredients which can be ISO files, installers, images ...
* **Binds:** Dolmades are isolated by default but can access files or directories on the host system using shared binds 

### Usage

#### Setup

Either download the release tar ball under https://github.com/dolmades/dolmades-cli/releases or
simply clone the repository using git:

```
cd $HOME
git clone --branch the_goglizer https://github.com/dolmades/dolmades-cli.git
cd dolmades-cli
git checkout tags/1.0 -b the_goglizer
```

#### Cooking a dolmade

Cooking describes the process of building a dolmade from a recipe and the required ingredients.
To cook a dolmade use the very simple example:

```
./cook Dolmadefile
```

At first the required ingredients will be downloaded. Then, the dolmade is being created and the installer is being run.
Click straight through the installation process. This will install the free game Broken Sword 2.5 on your desktop. It can be started by double clicking the desktop icon:

![](shots/firstuse_0.png?raw=true)

or from terminal:
```
./dolmades launch Broken_Sword
```

Select `Windowed Mode` in the launcher and click "Ok":

![](shots/firstuse_1.png?raw=true)

This will launch the game:

![](shots/firstuse_2.png?raw=true)

A system tray icon indicates the running dolmade. On left click you can access the run log, on right click you can forcibly terminate the running dolmade in case the app hangs itself. 

#### Generating a dolmade recipe using a GOG account

Here we gonna cook your favourite GOG win-only game using the script `goglizer`.
At first, you will be asked to authorize using your GOG account:
```
./goglizer -u
```
The `-u` parameter tells `goglizer` to retrieve the dolmades runtime container and your personal game list.
The authorization credentials are being stored in your home directory for subsequent use.
After success a list of your games is being shown:

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
./cook broken_sword_3__the_sleeping_dragon.dolmade
```
After successful completion you will find a clickable icon on your desktop :)


### Development
### Versioning
### Base Images
### External Binds

## Tools

### `dolmades`
### `goglizer`
### `cook`
### `config.py`

## `Dolmadefile` Syntax
...`Dolmadefile` 1.0 Syntax - mark which command is mandatory and which one is optional

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

## Acknowledgement
