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

Dolmades are intended as a mean to ease packaging, installation and distribution of windows programs in Linux environments to the utmost extent. This release focuses on basic features and GOG support. As of now a collection of a few command line tools represent the prototypical implementation of the underlying concepts:

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

 * Docker+DockerHub: for the dolmades base images
 * udocker + proot: for user-level containerization
 * wine + winetricks: for running windows application in Linux

## Features

* **GOG games support:** generate template recipes for your personal GOG collection and installation is a breeze
* **Ease-of-use:** supports any linux distro and require no special permissions
* **Compatibility:** recipes create functional dolmades across various distros and system hardware
* **Mobility:** designed to be portable across various distros and system hardware
* **Safety&Security:** dolmades are isolated from each other and from the host system by default

* **Users**
  * **Creation:** cook your application using recipes and install a desktop symlink
  * **Target launcher:** displays a selection of all installed applications and you choose which one to run
  * **Shares:** bind selected paths from the host system to windows drives inside a dolmade
  * **Import&Export:** EXPERIMENTAL - allows sharing cooked dolmades and requires user names to remain identical!
  
* **Developers:** 
  * **Create recipes:** use the existing Dolmadefiles as template for your own win-only apps
  * **Debug mode:** examine problems, add fixes and instantly rebuild the application
  * **Selectable base:** choose between between several wine versions

## Features of the next release

* Improved Import&Export to work across changing user names
* Recipe specification: Gather feedback. Complete syntax. Standardize it.
* Lots of refactoring / bug fixing

## Basics

## Tools

## Dolmadefile Syntax

## FAQ

## HOWTOs

## Roadmap
