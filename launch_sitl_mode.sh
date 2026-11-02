#!/bin/bash

# Open three terminals with different commands

# Command for terminal 1
command1="~/Desktop/UnrealEditor  /home/animallocator/Documents/src/colosseum/Colosseum/Unreal/Environments/Blocks/Blocks.uproject -norelativemousemode"

# Command for terminal 2
command2="cd ~/Documents/src/PX4/PX4-Autopilot && make px4_sitl_default none_iris"

# Command for terminal 3
command3="~/Downloads/QGroundControl.AppImage"

# Open terminal 1
# gnome-terminal -- bash -c "$command1"

# Open terminal 2
gnome-terminal -- bash -c "$command2"

# Open terminal 3
gnome-terminal -- bash -c "$command3"
