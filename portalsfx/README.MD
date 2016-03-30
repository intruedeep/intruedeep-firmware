These are just simple scripts to execute to play Portal turret sounds.

Ideally, in order, they would be played:
1) deployS.py: Upon turning on the turret
2) searchS.py: Upon starting a target finding execution
3) activeS.py: Upon successfully finding a target
4) firingS.py: UNLIKE THE OTHER FILES, this is a loop that should be played while the turret is firing. Currently, it is a while(1) loop

The non-firingS.py files are one-time executes.
