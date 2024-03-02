# simulation
Any scripts for documentation related to running simulations such as colosseum, airsim, gazebo, PX4 SITL/HITL

## How to setup and run Colosseum with PX4 SITL + QGroundControl

1. Colosseum is very lacking in official documentation but thankfully the setup process is pretty straight forward and even easier than the original AirSim

### Setup the operating system

1. You must run Colosseum/PX4/QGC on Ubuntu 20.04 LTS, other versions and OSes won't work quite as well.
2. You can get 20.04 here https://releases.ubuntu.com/focal/
  1. Write it to a USB and boot from it and run through the install process.
  2. You can run it in a virtual machine if you know how to get GPU passthrough to work.

### Install Visual Studio Code

1. Unreal Engine 5 requires you to have VSCode in order to open Colosseum files.
2. Head to the https://code.visualstudio.com/Download page and download the "deb" installer
3. Double click the .deb file once it is downloaded and be patient as it opens the installer software.
4. Click install and enter your password.
5. Alternatively you can use the command line
6. `sudo dpkg -i name_of_file.deb`

### Setup Nvidia graphics drivers if you have an nvidia GPU

1. In many cases you won't start out with the correct graphics drivers.
2. To know if you have the right drivers open a terminal and type
  1. `nvidia-smi`
  2. Output should be similar to Appendix A 1
  3. Most notably you will see the correct version of nvidia driver and cuda displayed and the model of your GPU
4. If you do not have the drivers here is how you can install them
  1. `sudo apt install nvidia-driver-535-open`
  2. This driver is the best currently and should work for most modern nvidia GPUs
  3. If you run into any issues consider installing again but omit the `-open` at the end.
4. reboot and confirm that the install worked by running `nvidia-smi` again.

### Install Unreal Engine 5

1. Thanks to leaps of improvements the process to install UE5 on linux is far easier than it was for UE4
2. You will need exactly version 5.2.1 of Unreal Engine 5
3. Go to https://www.unrealengine.com/en-US/linux
4. Login with an Epic Games account or make one.
5. You will need to browse older versions of UE5 using `show earlier releases`
6. Look for version 5.2.1 and download it (make sure it's unreal engine and not the "bridge" think.
7. It's a large file so wait some time for it to download.
8. Extract the folder into a directory you wish to store UE5
9. Test it out by running the file at `Linux_Unreal_Engine_5.2.1/Engine/Binaries/Linux/UnrealEditor`
  1. It is recommended to create a symlink to this file on your desktop so its easy to launch it.
  2. `ln -s /home/myusername/Desktop/UnrealEditor /path/to/UnrealEditor`
11. It may take some time to initialize and get ready. Be sure to fully test by creating a basic project.
12. You're done!

### Install ~~AirSim~~ Colosseum

1. Installing Colosseum is fairly straight forward and automated.
2. Create a folder somewhere you'd like to store AirSim and compile it.
3. clone the repo into the folder `git clone https://github.com/CodexLabsLLC/Colosseum.git`
4. cd Into `Colosseum`
5. run `./setup.sh`
6. May take some time to run
7. now once that is done run `./build.sh`
8. May also take some time
9. When that is finished you will have a folder in the main folder `Unreal/Environments/Blocks`
10. This is the folder where the UE5 project is stored keep that in mind.
11. Test out airsim now
12. Launch UnrealEditor
13. Use the file selector to browse for project files and look for the Blocks.uproject file we mentioned.
14. You will be asked if you want to convert the project in place or work on a copy.
15. Select convert-in-place
16. UnrealEngine5 might disappear for a minute or two don't worry this is normal it will be right back.
17. Once the project is loaded you can click play and then click "No" if asked if you want to use the car sim.
18. Should start processing shaders and loading the default drone.
19. In the future you can launch this by just opening UnrealEditor and select it in the previously open projects.



## Appendix A

### 1
```
animallocator@colosseum-1:~/Documents/src/Colosseum/Colosseum/Unreal/Environments/Blocks$ nvidia-smi
Sat Mar  2 09:41:12 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.161.07             Driver Version: 535.161.07   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce GTX 1080        Off | 00000000:00:10.0  On |                  N/A |
|  0%   50C    P5              14W / 180W |   1390MiB /  8192MiB |      2%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A       945      G   /usr/lib/xorg/Xorg                          150MiB |
|    0   N/A  N/A      1237      G   /usr/bin/gnome-shell                         45MiB |
|    0   N/A  N/A      2609      G   /usr/lib/firefox/firefox                    145MiB |
|    0   N/A  N/A     32644    C+G   .../Engine/Binaries/Linux/UnrealEditor     1009MiB |
|    0   N/A  N/A     33691      G   ...sion,SpareRendererForSitePerProcess       31MiB |
+---------------------------------------------------------------------------------------+
```
