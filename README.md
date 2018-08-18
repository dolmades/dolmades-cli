# dolmades-cli

## Introduction

Dolmades are intended as a tool to ease installation of windows programs to the utmost extent.
This collection of command line tools is the first implementation of the concept behind dolmades.
Right now there are two python scripts

* goglizer - prepares win-only GOG games to be cooked (GOG account required)
* cook - cooks a dolmade given a Dolmadefile (specification) and its ingredients (files)

Right after cooking the windows application will be available as clickable icon on your desktop.

## Requirements

* Python 2.7 or 3.5
* udocker
* tar version ???

## Basic Use

To cook a dolmade use the very simple example:

```
./cook Dolmadefile
```
This will install the free game Broken Sword 2.5 on your desktop.

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

Note, that only games are being listed that have no corresponding linux installer. If you want those to be listed as well you need to give the `-l` parameter, too:

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
./goglizer -d=broken_sword_3__the_sleeping_dragon

echo FIXME explain how to fix target and installation in the dolmade file...

echo now cook the dolmade
./cook broken_sword_3__the_sleeping_dragon.dolmade
```
