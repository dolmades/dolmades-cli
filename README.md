# dolmades-cli

## Introduction

Dolmades are intended as a mean to ease packaging, installation and distribution of windows programs in Linux environments to the utmost extent. This collection of command line tools represent the prototypical implementation of the underlying concepts.
As of now there are three python scripts:

* dolmades - to maintain your installed windows application
* goglizer - prepares win-only GOG games to be cooked; GOG account required
* cook - cooks a dolmade given a Dolmadefile and its ingredients

Right after cooking the windows application will be available as clickable shortcut on your desktop.
A global configuration file called `config.py` provides important settings to all three scripts.

## Requirements

As of now 
* x86-64 linuxes only
* Python 2.7
* curl
* tar (udocker requires some recent version, I can't find the issue pointing out which one it is)

Notes
* `udocker` requires Python 2.7 and will hopefully receive Python 3 support: https://github.com/indigo-dc/udocker/issues/77
* `dolmades` will be written to support Python 2.7 and bearing in mind Python 3 compatibility for later when udocker starts supporting it, too.
* 64bit linux kernel is needed due to the docker base images being built with x86-64 architecture. Technically it is possible to rebuild them using a 32bit linux kernel
* wine does not work well with pure x86-64 software which is why the installed windows software actually has to support 32bit windowses

## First use

To cook a dolmade use the very simple example:

```
./cook Dolmadefile
```
Click straight through the installation process. This will install the free game Broken Sword 2.5 on your desktop.
It can be started by double clicking the desktop icon or from terminal:
```
./dolmades launch Broken_Sword
```

## Usage with GOG account

Here we gonna cook your favourite GOG win-only game using the script `goglizer`.
At first, you will be asked to authorize using your GOG account.
```
./goglizer -u
```
The `-u` parameter tells `goglizer` to retrieve the dolmades runtime container and your personal game list.
The authorization credentials are being stored in your home directory for subsequent use.
After success a list of your games is being shown. 

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

Note, that only games are being listed that have no corresponding linux installer. If you want those to be listed as well you need to use the `-l` parameter:

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

Now choose a game of your liking and instruct `goglizer` to download the ingredients and create a corresponding dolmade file using the `-d` parameter.
```
./goglizer -d=broken_sword_3__the_sleeping_dragon
```
download its ingredients and prepare a Dolmadefile for installation
```
./goglizer -d=broken_sword_3__the_sleeping_dragon
```

Now install the dolmade
```
./cook broken_sword_3__the_sleeping_dragon.dolmade
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

# set windows version to WinXP
winetricks winxp
# rerun installer and ensure that it works now
/install/setup_edna_and_harvey_the_breakout_2.1.0.5.exe
# test cooked dolmade
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

This erases the previous dolmade and applies the fix permanently. Now add and commit your `dolmadefile` to your personal github repository.

## Managing dolmades

Your dolmades are managed by `dolmades`

## Initialization

Initialization does two things:
* if it doesn't exist yet: initializing the dolmades directory under `$HOME/.dolmades`
* downloading the docker runtime container with the matching version and (re)create it

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
### Debug

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

### Binds

It is possible to make files or directories of the host file system accessible from within the container by defining so-called binds. These will apply just when a dolmade is being executed but not when it is being debugged.

```
./dolmades binds name-of-dolmade
# listing the currently configured binds
```

```
./dolmades bind name-of-dolmade bind1 bind2 ...
```

A bind is defined as follows: `/hostdir/hostfile:/dolmadedir/dolmadefile` or `/hostdir/:/dolmadedir/`
Note, that a bind requires files/directories to exist on the host and within the dolmade!
