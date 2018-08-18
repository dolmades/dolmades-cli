# dolmades-cli

## Introduction

Dolmades are intended as a tool to ease installation of windows programs to the utmost extent.
This collection of command line tools is the first implementation of the concept behind dolmades.
Right now there are two python scripts

* goglizer - prepares win-only GOG games to be cooked (GOG account required)
* cook - cooks a dolmade given a Dolmadefile (specification) and its ingredients (files)

Right after cooking the windows application will be available as icon on your desktop.

## Requirements

* Python 2.7 or 3.5
* udocker
* tar version ???

## Usage

To cook a dolmade use the very simple example:

```bash
./cook Dolmadefile
```
This will install the free game Broken Sword 2.5 on your desktop.

To cook your favourite GOG win-only game:

```bash
echo you will be asked to authorize your GOG account (only once)
echo check your email and enter the code
echo this will retrieve your personal games and list them
./goglizer -u

echo now choose a game, download its ingredients and prepare a Dolmadefile for installation
./goglizer -d=broken_sword_3__the_sleeping_dragon

echo FIXME explain how to fix target and installation in the dolmade file...

echo now cook the dolmade
./cook broken_sword_3__the_sleeping_dragon.dolmade
```
