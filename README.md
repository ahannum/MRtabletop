# Tabletop MRI

## Introduction

This repository serves as the main hub for all code & resources related to the tabletop MRI systems at Stanford University.

To get started, these videos and files can serve as basic orientation to the systems.
* https://www.youtube.com/watch?v=-oz5ecPS6VQ&t=561s
* https://www.youtube.com/watch?v=9qmofVIGHZ4&t=3s
* https://www.sciencedirect.com/science/article/pii/S1090780719302642?via%3Dihub
* https://zeugmatographix.org/ocra/


## System Status

### Ocra1

March 9: updated to latest release of Relax 2.0 software

### Ocra2

February 28: gradient channels y and z2 not working
- As evidenced by shim calibration returning flat lines for these channels
-	TODO Alex & Ariel: bring ocra2 to Thomas at Q-Bio end of March to investigate

### Ocra3

February 28: Relax 2.0 software version predates latest release


## Bugs

Shim calibration prone to freezing
-	This has only been observed on ocra2, so may be related to shim channels malfunctioning

Certain button clicks will crash the Relax 2.0 program
-	appears to be sequence-dependent; full extent of issue is unknown, but certainly includes some 2D imaging sequences
-	Commenting lines of code with parameter ”frameon=” resolves the issue
-	TODO identify the specific button/sequence combinations that trigger these errors

Reducing FOV does not shorten scan time as expected (fewer phase encode lines)
-	Observed by Daniel
-	Alex suspects this is more of a suboptimal UI design than a bug: the “Resolution” field does not set pixel size directly, but rather the number of pixels (the image matrix size). Hence changes to the field of view result in inversely proportional changes to the pixel size in order to preserve the matrix size.

Unexpected bimodal signal observed in FID spectrum
-	Observed by Mark using multi-component phantom
-	TODO further investigation is needed comparing FID vs spin echo for single- and multi-component phantoms and recording the parameters used
-	TODO check whether poor shim could explain


## Feature Requests

Correct typos and misleading labels in Parameters menu
- Generell -> General
- Resolution -> Pixel Count or Image Matrix Size

Synchronization of code between tabletop systems
- Current status quo results in bug fixes not always distributed to other systems

Visualize pulse sequences to help with debugging and learning

Force quit a scan without killing the server

Automatic pre-scan
- Run center frequency calibration prior to a scan
- Create option in main menu to toggle this feature on/off
- Consider adding other abbreviated calibration routines e.g. shimming

Improve shim calibration
- Further automation to reduce manual effort
- Improve algorithm to achieve lower B0 inhomogeneity (currently 20-40ppm)
  - We may find that hardware is the limiting factor here

Facilitate pulse sequence development & deployment through Pulseq integration 

Web app to allow remote access bypassing Stanford network

Automate phantom loading/unloading for remote use with multiple phantoms


## Roadmap

1. Test latest release of firmware and software (March 8). Revise Bugs and Feature Requests accordingly.
2. Communicate with Marcus and Thomas about residual issues pertaining to the software and hardware. 
3. Decide on software platform moving forward.
4. Tend to bugs and feature requests.
