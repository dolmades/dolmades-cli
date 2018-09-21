# dolmades-cli

## Introduction

Dolmades are intended as a mean to ease installation and distribution of windows programs in Linux environments to the utmost extent. This collection of command line tools represent the first implementation of the underlying concept.
As of now there are two python scripts

* dolmades - to maintain your installed windows application
* goglizer - prepares win-only GOG games to be cooked (GOG account required)
* cook - cooks a dolmade given a Dolmadefile (specification) and its ingredients (files)

Right after cooking the windows application will be available as clickable icon on your desktop.

## Requirements

* Python 2.7 or 3.5

## Basic Use

To cook a dolmade use the very simple example:

```
./cook Dolmadefile
```
Click straight through the installation process. This will install the free game Broken Sword 2.5 on your desktop.

## Usage with GOG account

Here we gonna cook your favourite GOG win-only game using the script `goglizer`.
At first, you will be asked to authorize using your GOG account.
```
./goglizer -u
```
The `-u` parameter tells `goglizer` to retrieve the dolmades runtime container and your personal game list.
The authorization credentials are being stored in the dolmade runtime container for subsequent usage.
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

Now choose a game of your liking and tell `goglizer` to download the ingredients and create a dolmade file using the `-d` parameter.
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

First we need to figure out interactively what needs to be done:
```
./dolmades debug edna_harvey_the_breakout:en.dolmade

# set windows version to WinXP
winetricks winxp
# rerun and check that it works now
/install/setup_edna_and_harvey_the_breakout_2.1.0.5.exe
# test cooked dolmade
targetSelector
```
In rare cases you might need to install a missing package. You can do this if you run as fake root:
```
./udocker root-debug Broken_Sword_3:_The_Sleeping_Dragon
apt-get update && apt-get -y install vim
```

## Management

```
dolmade rm
```
