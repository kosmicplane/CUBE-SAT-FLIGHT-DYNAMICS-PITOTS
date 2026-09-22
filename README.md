# CubeSat-Class Atmospheric Probe — Flight Dynamics & Multi-Pitot Wind Estimation

<p align="center">
  <strong>Atmospheric descent · multi-Pitot sensing · IMU/GPS processing · reference-frame transformations · wind-tunnel calibration · post-flight reconstruction</strong>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/cad.webp" width="31%" alt="Probe CAD">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/frame.webp" width="31%" alt="Probe structure">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/avionics.webp" width="31%" alt="Probe avionics">
</p>

This repository contains flight-dynamics and sensing code developed for a **CubeSat-class atmospheric probe** used to study descent behavior and reconstruct atmospheric-flow information from onboard measurements.

The project combines:

- atmospheric-property estimation;
- inertial and GPS-derived motion information;
- a multi-Pitot sensing arrangement;
- body-to-Earth frame transformations;
- wind-vector reconstruction;
- wind-tunnel data collection and calibration;
- post-flight processing and trajectory analysis.

The emphasis is on connecting a physical sensing system to a reproducible computational model rather than treating CFD, wind-tunnel tests, and flight data as separate activities.

---

## Measurement model

### Pitot-derived speed

For each pressure measurement (Delta p_i), the code uses the incompressible dynamic-pressure relation

[
V_i=sqrt{rac{2|Delta p_i|}{ho}},
]

where (ho) is the local air density.

The current implementation forms two differential components from opposing Pitot measurements:

[
V_x^b = V_1-V_3,
qquad
V_y^b = V_2-V_4.
]

The body-frame estimate is therefore represented as

[
mathbf{V}_{pitot}^{,b}
=
egin{bmatrix}
V_x^b\
V_y^b\
0
end{bmatrix}.
]

A rotation matrix built from the measured attitude maps the vector into the Earth frame:

[
mathbf{V}_{pitot}^{,e}
=
C_e^b(phi,	heta,psi),
mathbf{V}_{pitot}^{,b}.
]

The repository implements these operations in [PitotProcess.py](simulacion/functions/PitotProcess.py), [Ce_b.py](simulacion/functions/Ce_b.py), and [Cb_e.py](simulacion/functions/Cb_e.py).

---

## Wind-vector reconstruction

The project combines motion information with the Pitot-derived airflow estimate. In the current processing path,

[
mathbf{V}_{wind}^{,NED}
=
mathbf{V}_{pitot}^{,e}
-
mathbf{V}_{IMU}^{,e}.
]

A second utility supports weighted combination of GPS- and IMU-derived velocity estimates:

[
mathbf{V}_{state}
=
rac{
w_{GPS}mathbf{V}_{GPS}
+
w_{IMU}mathbf{V}_{IMU}
}{
w_{GPS}+w_{IMU}
}.
]

The wind estimate then follows from the selected sensor combination.

See [V_Wind.py](simulacion/functions/V_Wind.py).

---

## Atmospheric properties

Air density and static pressure are estimated using an ISA-style atmosphere model in [ISA.py](simulacion/functions/ISA.py).

The density calculation follows

[
ho=rac{p}{RT},
]

with R the specific gas constant for air and temperature converted to Kelvin.

Because Pitot-derived velocity scales as (1/sqrt{ho}), the atmospheric-property model directly affects the reconstructed flow magnitude.

---

## IMU velocity integration

The processing utilities also include numerical integration of measured linear acceleration:

[
mathbf{v}(t)
=
mathbf{v}(t_0)
+
int_{t_0}^{t}
mathbf{a}(	au),d	au.
]

[calcVelocity.py](simulacion/functions/calcVelocity.py) applies this operation component-wise to the IMU acceleration channels.

This is useful for short-window reconstruction and comparison, but inertial integration is drift-sensitive; calibration and cross-checking against external measurements remain important.

---

## Experimental workflow

~~~mermaid
flowchart LR
    A[Probe geometry] --> B[CFD / sensor placement]
    B --> C[Multi-Pitot installation]
    C --> D[Wind-tunnel calibration]
    D --> E[Flight instrumentation]
    E --> F[IMU + GPS + pressure data]
    F --> G[Frame transformation]
    G --> H[Wind-vector reconstruction]
    H --> I[Post-flight trajectory and model comparison]
~~~

<p align="center">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/windtunnel.webp" width="47%" alt="Wind-tunnel testing">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/wind-results.webp" width="47%" alt="Wind-tunnel results">
</p>

The repository includes wind-tunnel datasets and notebooks under [Tests/](Tests/) as well as flight and simulation processing material under [simulacion/](simulacion/).

---

## Physical integration and recovery

<p align="center">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/tower.webp" width="31%" alt="Probe integration">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/model.webp" width="31%" alt="Probe model">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/recovery.webp" width="31%" alt="Recovered probe">
</p>

These images document the progression from probe modeling and sensor integration to physical mission hardware and recovery.

---

## Repository structure

~~~text
Tests/
├── functions_testing.ipynb
├── tunnel_sampling.ipynb
├── test_tunnel_code.py
└── prueba_tunel_*.xlsx

simulacion/
├── main.ipynb
├── proccesor.ipynb
├── datos_vuelo_200_filas.csv
├── Prueba_recolectada.txt
├── map.html
└── functions/
    ├── PitotProcess.py
    ├── V_Wind.py
    ├── ISA.py
    ├── calcVelocity.py
    ├── Ce_b.py / Cb_e.py
    └── filtering / integration utilities
~~~

---

## Scientific scope

This repository should be interpreted as a research and engineering implementation of the probe's **measurement and reconstruction pipeline**. Individual equations encode simplified sensor and atmospheric models and therefore depend on calibration quality, pressure interpretation, frame definitions, and the assumptions of the selected atmospheric and flow regimes.

The validation hierarchy is:

~~~text
analytical relation
→ numerical processing
→ wind-tunnel calibration
→ integrated sensor testing
→ flight-data reconstruction
~~~

That hierarchy is preserved so that computational results are not presented as stronger evidence than the physical tests that support them.
