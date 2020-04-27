# LSL for Neuromore Studio
Connecting Muse headband to Neuromore Studio

The script redirects LSL stream to OSC, which Neuromore Studio takes as its input. 
The script connects Muse headband, but in theory it can work with other devices as long as the data from them goes thought LSL stream.
Below is the instruction for Windows 10. For the other platforms the steps are similar, except no need for running BlueMuse, becasue muse-lsl can be used instead (https://github.com/alexandrebarachant/muse-lsl)

### Prerequisites

1. Python 3 (tested with 3.7 version) with <i>pylsl</i> and <i>python-osc</i> packages installed</br>
    `pip install pylsl`</br>
    `pip install python-osc`</br>    
2. BlueMuse https://github.com/kowalej/BlueMuse (tested with 2.0.0.0 version)
3. Neuromore Studio https://github.com/neuromore/studio (tested with 1.4.4 version)

### Running the script

1. Connect the Muse headband to BlueMuse
1. Run  `python stream_data.py`
1. Open Neuromore Studio and configure OSC Server (`Edit -> Settings`) to listen on input port 4545, address 0.0.0.0 (if everything runs on a local machine)
1. In the Studio create a Classifier and create 4 (or 5 for aux channel) OSC Input nodes
![Screenshot](screenshot.png)
1. Configure each node to listen to one of the OSC addresses (`/muse/tp9`, `muse/af7` etc.) and set the sampling rate to 256
1. To see the raw data: `View -> Add -> Signal View`


The Script should work for Muse 2 as well, alternative solution https://github.com/naxocaballero/muse2-neuromore
