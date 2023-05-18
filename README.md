# SingularityNET service for Spotify Basic Pitch

This is a wrapper around [Basic Pitch](https://basicpitch.spotify.com/)
for the SingularityNET Market Place.

Basic Pitch is an audio-to-MIDI converter built by
[Spotify](https://www.spotify.com).

## Prerequisites

1. Install Basic Pitch.  Follow the instructions
   [here](https://github.com/spotify/basic-pitch#installation), or
   simply type in terminal

```
pip install basic-pitch
```

### Installing

* Clone the git repository:

```
git clone https://github.com/singnet/basic-pitch-service.git
cd basic-pitch-service
```

* Install the dependencies and compile the protobuf file:

```
pip install -r requirements.txt
sh buildproto.sh
```

### Running

#### Standalone

* Run the example service directly (without `SNET Daemon`):

```
python run_basic_pitch_service.py --no-daemon
```

* To test it run the script:

```
python test_basic_pitch_service.py
```
