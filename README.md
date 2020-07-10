Berserker's Multiworld
======================

A Multiworld implementation for the Legend of Zelda: A Link to the Past Randomizer  
For setup and instructions there's a [Wiki](https://github.com/Berserker66/MultiWorld-Utilities/wiki)  
Downloads can be found at [Releases](https://github.com/Berserker66/MultiWorld-Utilities/releases), including compiled windows binaries.  

Additions/Changes compared to Bonta's V31
-----------------

Project
 * Available in precompiled form and guided setup for Windows 64Bit on [Releases](https://github.com/Berserker66/MultiWorld-Utilities/releases) page.
 * Compatible with Python 3.7 and 3.8. Forward Checks for Python 4.0 are done.
 * Update modules if they are too old, preventing a crash when trying to connect among potential other issues
 * Autoinstall missing modules
 * Allow newer versions of modules than specified, as they will *usually* not break compatibility
 * Uses "V32" MSU
 * Has support for binary patching to allow legal distribution of multiworld rom files
 * Various performance improvements (over 100% faster in most cases)
 * Various fixes
 * Overworld Glitches Logic
 * Newer Entrance Randomizer Logic, allowing more potential item and boss locations
 * completely redesigned command interface, with `!help` and `/help`
 * New Goal: local triforce hunt - limits triforce pieces to your own world so it is your own goal to accomplish
 
MultiMystery.py
 * Allows you to generate a Multiworld with individual player mystery weights. Since weights can also be set to 100%, this also allows for individual settings for each player in a regular multiworld.
Basis is a .yaml file that sets these weights. You can find an [easy.yaml](https://github.com/Berserker66/MultiWorld-Utilities/blob/master/easy.yaml) in this project folder to get started.
 * Additional instructions are at the start of the file. Open with a text editor.
 * Configuration options in the host.yaml file.
 * Allows a new Mode called "Meta-Mystery", allowing certain mystery settings to apply to all players.
   * For example, everyone gets the same but random goal.
 
 MultiServer.py
  * Supports automatic port-forwarding, can be enabled in host.yaml
  * improved `!players` command, mentioning how many players are currently connected of how many expected and who's missing
  * /forfeit Playername now works when the player is not currently connected
  * Added `/hint` and `!hint`, configuration in host.yaml and description in help
  * various commands, like /send and /hint use "fuzzy text matching", no longer requiring you to enter a location, player name or item name perfectly
  * Some item groups also exist, so `/hint Bottles` lists all bottle varieties

Mystery.py
 * Defaults to generating a non-race ROM (Bonta's only makes race ROMs at this time)
If a race ROM is desired, pass --create-race as argument to it
 * When an error is generated due to a broken .yaml file, it now mentions in the error trace which file, line and character is the culprit
 * Option for progressive items, allowing you to turn them off (see easy.yaml for more info)
 * Rom-Option for extendedmsu (see easy.yaml for more info)
 * Option for "timer"
 * Option for "dungeon_counters", allowing you to configure the dungeon item counter
 * Option for "glitch_boots", allowing to run glitched modes without automatic boots
 * Supports new Meta-Mystery mode. Read [meta.yaml](https://github.com/Berserker66/MultiWorld-Utilities/blob/master/meta.yaml) for details.
 * Added `dungeonssimple` and `dungeonsfull` ER modes
 * Option for local items
 * Option for linked options
 * Added 'l' to dungeon_items to have a local-world keysanity
 
MultiClient.py
 * Has a Webbrowser based UI now
 * Awaits a QUsb2Snes connection when started, latching on when available
 * completely redesigned command interface, with `!help` and `/help`
 * Running it with a patch file will patch out the multiworld rom and then automatically connect to the host that created the multiworld
 * Cheating is now controlled by the server and can be disabled through host.yaml
 * Automatically starts QUsb2Snes, if it isn't running
 * Better reconnect to both snes and server
