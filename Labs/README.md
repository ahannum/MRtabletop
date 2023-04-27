# Lab Course Materials

The master documents for all tabletop MRI course materials reside in a live latex project on Overleaf (link below). Different compiled versions of this project may be pushed here for a given course offering. Please edit the Overleaf project directly to make any changes that should be applied universally, i.e. to all future course offerings.

https://www.overleaf.com/5917285931djystdhvctnk

## Ideas

Below is a running list of ideas for new lab exercises.

- Image contrast
  - compare T1 contrast for saturation recovery vs inversion recovery
    - measure CNR
  - elicit T2* effects by adjusting parameters of SE and GRE sequences
    - comment on signal envelope
    - if dominant inhomogeneity is linear, then expect signal envelope to be sinc-like for uniform rectangular object (p.129 [1])


- RF Excitation
  - estimate RF pulse from FT of slice profile at small flip angle
  - make plots like Fig 6.11 [1]
    - test importance of assumptions about no relaxation and small tip angle by extending pulse duration and increasing flip angle
  - applied study of Practical Considerations on p.117 [1]
    - fix slice gradient and pulse duration and see how slice definition gets worse with reduced B1 bandwidth (because you’re truncating the sinc ie worse time bandwidth); begin by consideromg how to make a super thin slice
  - double RF amplitude and halve the pulse duration, or vice-versa; compare the resulting plots
    - ideally they would look the same, based on excitation kspace theory. Why might this not hold true? Relaxation, for one.
  - Ernst Angle


- Encoding
  - observe effect of off-resonance with different sampling schemes
    - problem 5.5 a&b [1]
    - figure 7.2 adjust gradient strength to scale the displacement with a 2DFT sequence
      - Discuss implications of imaging at different field strengths, different gradient specs (e.g. high field scanners require stronger gradient systems to overcome the same ppm)
  - adjust sequence timing to get fat and water in phase or out of phase when you sample the k-space origin - so you get water plus fat contrast or water minus fat contrast (p.134 [1])
  - reproduce aliasing artifacts on p.88 (figures 5.18, 5.19) [1]
  - play with arguments on p.87 and p.90 about cycles of phase across the object - how to measure this? [1]

- Imaging Tradeoffs: SNR, resolution, FOV
  - p.163 example [1]
    - change the sampling rate, but keep sampling time the same
    - observe FOV changes but SNR is preserved
  - p.164-5 & figure 7.19 [1]
    - compare SNR of two images with same readout duration, sampling rate (and number of samples), anti-aliasing filter bandwidth but 2x readout gradient
    - try for different objects
    - compare SNR between the three cases: low-res, high-res, and synthesized low-res
      - comment on agreement with SNR ~ dx * dx * dz and SNR ~ sqrt(N_ave)
    - see if you can break the p.165 “rule of thumb” by repeating the experiment with a much larger voxel size
      - where is the breaking point? can you explain this by looking at the k-space roll-off?
- Spectroscopic Phantoms
  - Water and Ethanol

[1] Nishimura, Dwight G. Principles of Magnetic Resonance Imaging, Lulu.com, 2010.
