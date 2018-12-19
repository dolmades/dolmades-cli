# Internals of a dolmade container

A dolmade contains an ubuntu base system with wine.
The file structure is currently standardized as follows:

* `/wineprefix` - where all wine and win application data is being stored
* `/data` - where user data is being stored
* `/.dolmades` - where all dolmade meta data is being stored

`/wineprefix/drive_c/users/root` holds the user profile. All unix user names are being symlinked to this directory. 
This is done automatically (see `/.dolmades/start.env`) whenever a bash is invoked inside the container via `dolmades`.

# Cooking procedure

The single steps performed during cooking are as follows:
* Parsing of the recipe
 * If recipe defines `VERSION`: version of `cook` has to match. Also, `VERSION` is used as tag for the docker images.
* Preparing the ingredients
 * Downloading/copying to the installation folder using one of the following protocols: `file ftp http https gog`
 * Validating checksums
* Preparing the base image
 * Pulling the base image from DockerHub which takes considerable time at the initial pull
* Creating a dolmade with the given name (will overwrite an existing dolmade with that name)
 * Initializing the wine prefix
 * Performing all run steps in the given order
 * Deposit meta data i.e. application icon, name, description, recipe, utilized dolmade version
 * Creating desktop symbol unless requested otherwise
