# MavSDK python test code to run on PX4 SITL sims

## Setup and Run

### Prerequisites

1. Python 3 installed

### Setup

1. cd into this directory
2. Create a virtualenv if you value your sanity
   1. `python3 -m venv .venv`
3. Activate the venv (do this anytime you wanna run the code too)
   1. `source .venv/bin/activate`
4. install dependencies
   1. `pip install -r requirements.txt`

### Running

1. Before starting
   1. see the README of the simulation repo for instructions on how to do this if you do not know how.
   2. Make sure airsim/colosseum is configured for PX4 SITL
   3. launch Airsim/Colosseum, and PX4 SITL, optionally you can launch QGroundControl
   4. make sure you activated the venv as in `Setup 3.1`
   5. ensure that PX4 has connected to AirSim you will see ready text outputted in the px4 terminal
   6. **IMPORTANT** make sure that pymavsdk and AirSim/Colosseum are using different control ports.
      1. eg. pymavsdk uses 14540 and AirSim uses 14550
      2. In the example settings.json below we changed colosseum to use 14550 because pymavsdk defaults to 14540
      3. However you need to pay attention to this because both the settings and the pymavsdk script can be accidentally configured to use the same.
2. in the PX4 command interface
   1. `commander disarm`
      1. This is currently a bug and we need to develop a way to not have to do this manually for smooth scripting.
3. Run the python script
   1. `python testmavsdk.py`

### Common issues

1. You didn't run `commander disarm` in px4
2. You are running the script from another machine
   1. If you need to do this then there is extra networking and reconfiguration necessary for the code.
   2. It is not possible out of the box
3. Your script connect() command and Airsim/Colosseum are using the same port
