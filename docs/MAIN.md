* [ ] Introduction
* [ ] Features
* [ ] Basics
  * [ ] Usage
  * [ ] Development
  * [ ] Versioning
  * [ ] Base Images
  * [ ] External Binds
  * [ ] Future: next version, C++ rewrite, registry support...
  * [ ] Acknowledgement
* [ ] Tools
  * [x] `dolmades`
  * [ ] `goglizer`
  * [ ] `cook`
  * [ ] `config.py`
  * [ ] goglizer / cook / dolmades should receive proper help texts (with param `-h`)
* [ ] `Dolmadefile` 1.0 Syntax - mark which command is mandatory and which one is optional
* [ ] FAQ: supported distros, requirements, limits, caveats, ...
* [ ] HOWTOS
  * [ ] Cook a dolmade recipe
  * [ ] Create a dolmade recipe
  * [ ] Migrate a dolmade
  * [ ] Copy-Protected CD/DVD Game: Describe how we can install Harry Potter 1 and Harry Potter 2 from copy protected CD media
   * [ ] Contribution
* [X] Roadmap

___

# Dolmades 1.0 "the goglizer"

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
* tar with support of `-delay-directory-restore` (see https://github.com/indigo-dc/udocker/pull/137)

Notes
* `udocker` requires Python 2.7 and will hopefully receive Python 3 support: https://github.com/indigo-dc/udocker/issues/77
* `dolmades` will be written to support Python 2.7 and bearing in mind Python 3 compatibility for later when udocker starts supporting it, too.
* 64bit linux kernel is needed due to the docker base images being built with x86-64 architecture. Technically it is possible to rebuild them using a 32bit linux kernel
* wine does not work well with pure x86-64 software which is why the installed windows software actually has to support 32bit windows

## Technical Base

Dolmades make heavy use of the following underlying technologies:

 * Docker: for the wine base images
 * udocker + proot: for user-level containerization
 * wine

## Features

* GOG games support: generate a template for games in your personal GOG collection and install it within minutes
* sandboxing: dolmades are isolated between each other and from the host system
* compatibility: recipes are designed to create functional dolmades across various systems (hardware, distros)
* mobility: dolmades are designed to be portable across various system (hardware, distros)

* for users
  * creation: cook your application using recipes and install a desktop symlink
  * target launcher: lists all installed applications and select which one to run
  * shares: bind selected paths from the host system to windows drives
  * import/export functionality (EXPERIMENTAL, requires user names to remain identical)
  
* for developers: 
  * create recipes: use the existing Dolmadefiles as template for your own win-only apps
  * debug mode: examine problems, add fixes and rebuild the application
  * selectable base: choose between between several wine versions (currently stable, devel, staging)

## Features of the next release

* Improve import/export to work across changing user names
* Recipe specification: complete syntax
* Lots of refactoring / bug fixing

## Basics

## Tools

## Dolmadefile Syntax

## FAQ

## HOWTOs

## Roadmap
