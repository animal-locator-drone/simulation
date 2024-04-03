# simulation

Any scripts for documentation related to running simulations such as colosseum, airsim, gazebo, PX4 SITL/HITL

## How to setup and run Colosseum with PX4 SITL + QGroundControl

1. Colosseum is very lacking in official documentation but thankfully the setup process is pretty straight forward and even easier than the original AirSim

### Setup the operating system

1. You must run Colosseum/PX4/QGC on Ubuntu 20.04 LTS, other versions and OSes won't work quite as well.
2. You can get 20.04 here <https://releases.ubuntu.com/focal/>
3. Write it to a USB and boot from it and run through the install process.
4. You can run it in a virtual machine if you know how to get GPU passthrough to work.

### Install Visual Studio Code

1. Unreal Engine 5 requires you to have VSCode in order to open Colosseum files.
2. Head to the <https://code.visualstudio.com/Download> page and download the "deb" installer
3. Double click the .deb file once it is downloaded and be patient as it opens the installer software.
4. Click install and enter your password.
5. Alternatively you can use the command line
6. `sudo dpkg -i name_of_file.deb`

### Setup Nvidia graphics drivers if you have an nvidia GPU

1. In many cases you won't start out with the correct graphics drivers.
2. To know if you have the right drivers open a terminal and type
   1. `nvidia-smi`
      1. Output should be similar to Appendix A 1
      2. Most notably you will see the correct version of nvidia driver and cuda displayed and the model of your GP
3. If you do not have the drivers here is how you can install them
   1. `sudo apt install nvidia-driver-535-open`
      1. This driver is the best currently and should work for most modern nvidia GPUs
      2. If you run into any issues consider installing again but omit the `-open` at the end.
4. reboot and confirm that the install worked by running `nvidia-smi` again.

### Install Unreal Engine 5

1. Thanks to leaps of improvements the process to install UE5 on linux is far easier than it was for UE4
2. You will need exactly version 5.2.1 of Unreal Engine 5
3. Go to <https://www.unrealengine.com/en-US/linux>
4. Login with an Epic Games account or make one.
5. You will need to browse older versions of UE5 using `show earlier releases`
6. Look for version 5.2.1 and download it (make sure it's unreal engine and not the "bridge" think.
7. It's a large file so wait some time for it to download.
8. Extract the folder into a directory you wish to store UE5
9. Test it out by running the file at `Linux_Unreal_Engine_5.2.1/Engine/Binaries/Linux/UnrealEditor`
   1. It is recommended to create a symlink to this file on your desktop so its easy to launch it.
      1. `ln -s /home/myusername/Desktop/UnrealEditor /path/to/UnrealEditor`
10. It may take some time to initialize and get ready. Be sure to fully test by creating a basic project.
11. You will also want to disable limiting FPS in the background as it will cause airsim to lag when you switch to other windows which is often the case.
   1. Edit >> Editor Preferences >> Performance >> Uncheck "Limit FPS In Background"
13. You're done!

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

### Install and setup PX4 in SITL mode

1. Create a folder where you would like to compile and run PX4 in SITL mode
2. cd into the folder
3. Retrieve the source code for PX4.
   1. In the folder you are working in
      1. `git clone https://github.com/PX4/PX4-Autopilot.git --recursive`
      2. Make sure you add that `--recursive` flag.
         1. This ensures that all the code that PX4 depends on is also cloned.
      3.
   2. (optional but recommended) Switch to a stable release
      1. Start over from step 3.1 but this time don't clone recursively.
      2. `git clone https://github.com/PX4/PX4-Autopilot.git`
      3. `cd PX4-Autopilot`
      4. Go to the releases page and identify the latest stable version number <https://github.com/PX4/PX4-Autopilot/releases>
         1. As of writing this it is `v1.14.0`
      5. `git checkout v1.14.0`
      6. Update submodules
         1. `make submodulesclean`
4. Run the script to install all dependencies
      1. `bash ./PX4-Autopilot/Tools/setup/ubuntu.sh`
      2. This step can have issues. Pay close attention to the output and identify any issues that arise and be sure to resolve them manually before proceeding.
      3. The reason this happens is because we are running on 20.04 an older version of ubuntu.
      4. Some issues can be ignored. I'll list any that I find and fix or ignore in Appendix A 2
5. Build PX4 in SITL mode
   1. `make px4_sitl none_iris`
   2. This will take some time on first run but from now on this is how you launch PX4 SITL
      1. Consider writing a script to automatically do this conveniently
   2. Common issue
      1. `AttributeError: module 'em' has no attribute 'Interpreter'`
         1.  This happened from a recent update. To fix it simply
            1. `pip uninstall em`
            2. `pip install empy==3.3.4`

### Install QGroundControl

1. You can use almost any version of QGC with any version of PX4
2. Weird prerequisite install `libxcb-cursor0`
   1. `sudo apt install  libxcb-cursor0`
3. Download the QGroundControl daily AppImage
   1. <https://docs.qgroundcontrol.com/master/en/qgc-user-guide/releases/daily_builds.html>
   2. Select the Linux build and you will get a .AppImage file
4. Make the AppImage executable
   1. Method 1 from the GUI
      1. Right click the file and click Properties
      2. Go to Permissions tab and select "Allow executing file as a program"
   2. Method 2 command line
      1. `chmod +x QGroundControlFileName.AppImage`
5. Run the AppImage file
   1. Method 1 from gui
      1. Right click and click Run or double click
   2. Method 2 command line
      1. `./QGroundControlFileName.Appimage`
6. You will be able to test it once we get everything else configured but it should launch just fine.

### Configure Colosseum to use PX4 simulation mode.

1. Colosseum needs to be configured to work with PX4
2. Edit your AirSim configuration file (Yeah its still called AirSim)
   1. It is located in `/home/myusername/Documents/AirSim/settings.json`
   2. Use the basic configuration in Appendix A 3 and paste it in the file overwriting existing settings. 
3. For more about how this settings file works see <https://microsoft.github.io/AirSim/settings/>

### Now lets bring it all together

1. Launch PX4
   1. `make px4_sitl none_iris`
2. Launch Colosseum
   1. ./UnrealEditor
   2. Once loaded press play
3. PX4 should detect the simulator and show feedback that it is ready
4. Launch QGroundControl
   1. It should auto connect to PX4
5. Now you can give commands to PX4 in simulation from QGroundControl and you can also write software to interact with PX4
6. Have lots of fun!

## Appendix A

### 1. Running nvidia-smi example when drivers are installed correctly

```bash
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

### 2. Issues that arise when running ubuntu.sh

1. Pandas incompatible library error
   1. Can be safely ignored it seems.
2. Warnings
   1. All warnings can likely be safely ignored they are just warnings after all.
3. `AttributeError: module 'em' has no attribute 'Interpreter'`
   1. This happened from a recent update. To fix it simply
      1. `pip uninstall em`
      2. `pip install empy==3.3.4`

### 3. Colosseum Config file example

```json
{
    "SettingsVersion": 1.2,
    "SimMode": "Multirotor",
    "ClockType": "SteppableClock",
    "Vehicles": {
        "PX4": {
            "VehicleType": "PX4Multirotor",
            "UseSerial": false,
            "LockStep": true,
            "UseTcp": true,
            "TcpPort": 4560,
            "ControlPortLocal": 14550,
            "ControlPortRemote": 14580,
            "Sensors":{
                "Barometer":{
                    "SensorType": 1,
                    "Enabled": true,
                    "PressureFactorSigma": 0.0001825
                }
            },
            "Parameters": {
                "NAV_RCL_ACT": 0,
                "NAV_DLL_ACT": 0,
                "COM_OBL_ACT": 1,
                "LPE_LAT": 47.641468,
                "LPE_LON": -122.140165
            }
        }
    }
}
```

### 4. commandto launch x11vnc on login
```bash
x11vnc -listen 0.0.0.0 -loop -forever -bg -rfbport 5901 -xkb -noxrecord -noxfixes -noxdamage -shared -norc
```

### 5. Systemd unit file for x11vnc on login screen
```bash
[Unit]
Description=Start x11vnc at startup.
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/x11vnc -listen 0.0.0.0 -loop -forever -bg -rfbport 5900 -xkb -noxrecord -noxfixes -noxdamage -shared -norc -auth /run/user/121/gdm/Xauthority

[Install]
WantedBy=multi-user.target
```
