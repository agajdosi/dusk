# How to

Open CV is installed on the Raspberry PI 4 with 4GB RAM.
Dusk script is located at `/home/pi/dusk`.
It is a git repository, so in case of any trouble, new fixed versions can be downloaded via git (more in `update code` section).

Due to the end of available webcams Dusk right now operates on video files.
Please add videos named 1.m4v and 2.m4v into into the directory where main.py script is located.

// Dusk contains 4 camera sources predefined, you can switch between them by pressing key 1, 2, 3 or 4.
// But the default no. 1 is the best...

## Basic usage
1. place videos 1.m4v

1. open terminal
2. `cd dusk`
3. `source bin/activate`
4. `python3 main.py -o True`

## Update code
1. close running dusk script
2. open terminal
3. `cd dusk`
4. `git pull`
5. code is updated now, now you can start the script (steps in basic usage)
