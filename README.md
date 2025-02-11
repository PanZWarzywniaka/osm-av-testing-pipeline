# OpenStreetMap AV testing pipeline

## Introduction

This is a fork of [sbst-tool-competition-av](https://github.com/se2p/tool-competition-av) which provide a pipeline for executing generated tests on [BeamNG.tech](https://beamng.tech/) simulator.

As a part of my dissertation project at [TUOS](https://www.sheffield.ac.uk/) under the supervision of [Phil McMinn](https://mcminn.io/) I expand this pipeline to use OpenSteetMap ([OSM](https://www.openstreetmap.org/)) to test cars on real world roads.

I additionally I want to add extra dimension (elevation) to the test cases, to test e.g. riding down hill.

## Technologies
- Python 3.7
- BeamNG.tech simulator with beamngpy library
- OSMPythonTools 

## Todo list

- [X] Test OSM API to retrieve road data
- [ ] Process OSM road data to generate test supplied to BeamNG
- [ ] Add another dimention to test generating