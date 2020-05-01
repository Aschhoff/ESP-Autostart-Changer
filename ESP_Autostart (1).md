**Esp Autostart Changer**

On  ESP Boards with micropython the main.py is a autostart file to run your Python program on power on.
Unfortunately uPyCraft is not able to terminate a running program and runs in flashmode.

Esp Autostart Changer is a Python script to terminate the running program on a esp board connected via USB.
Just press Autostart off the main.py on board is disabled and   uPyCraft get access to the board.
Make your changes and then press Autostart on.
The original main.py will be restored.
