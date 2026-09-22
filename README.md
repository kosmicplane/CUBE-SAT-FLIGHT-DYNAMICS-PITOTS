# CubeSat-Class Atmospheric Probe — Flight Dynamics & Multi-Pitot Wind Estimation

<p align="center">
  <strong>Atmospheric descent · multi-Pitot sensing · IMU/GPS processing · frame transformations · wind-tunnel calibration · post-flight reconstruction</strong>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/cad.webp" width="32%" alt="Probe CAD">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/frame.webp" width="32%" alt="Probe structure">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/avionics.webp" width="32%" alt="Probe avionics">
</p>

This repository contains flight-dynamics and sensing code developed for a **CubeSat-class atmospheric probe** used to study descent behavior and reconstruct atmospheric-flow information from onboard measurements.

The project connects five engineering layers:

1. **descent dynamics and atmospheric properties**;
2. **multi-Pitot airflow sensing**;
3. **IMU/GPS motion information**;
4. **coordinate-frame transformations and wind-vector reconstruction**;
5. **wind-tunnel and flight-data validation**.

The goal is not to treat CFD, tunnel testing, sensing, and post-flight processing as independent activities, but to connect them into one traceable measurement-and-reconstruction workflow.

---

## System workflow

~~~mermaid
flowchart LR
    A[Probe geometry] --> B[CFD / sensor placement]
    B --> C[Multi-Pitot installation]
    C --> D[Wind-tunnel calibration]
    D --> E[Flight instrumentation]
    E --> F[IMU + GPS + pressure data]
    F --> G[Frame transformation]
    G --> H[Wind-vector reconstruction]
    H --> I[Trajectory / model comparison]
~~~

---

## Pitot measurement model

For each differential-pressure measurement \(\Delta p_i\), the implementation uses the incompressible dynamic-pressure relation

$$
V_i
=
\sqrt{
\frac{2\lvert \Delta p_i\rvert}{\rho}
},
$$

where \(\rho\) is local air density.

The current processing path forms opposing-sensor components

$$
V_x^b
=
V_1-V_3,
$$

$$
V_y^b
=
V_2-V_4.
$$

The body-frame airflow estimate is therefore represented as

$$
\mathbf V_{\mathrm{Pitot}}^{\,b}
=
\begin{bmatrix}
V_x^b\\
V_y^b\\
0
\end{bmatrix}.
$$

Using the repository's selected body/Earth frame convention,

$$
\mathbf V_{\mathrm{Pitot}}^{\,e}
=
C_e^b(\phi,\theta,\psi)
\mathbf V_{\mathrm{Pitot}}^{\,b}.
$$

Relevant implementation files include:

- [PitotProcess.py](simulacion/functions/PitotProcess.py)
- [Ce_b.py](simulacion/functions/Ce_b.py)
- [Cb_e.py](simulacion/functions/Cb_e.py)

---

## Atmospheric model

Air density is estimated with an ISA-style atmospheric model.

The density relation is

$$
\rho
=
\frac{p}{RT},
$$

where \(p\) is static pressure, \(R\) the specific gas constant for air, and \(T\) absolute temperature.

Because the Pitot-derived velocity scales as

$$
V\propto \frac{1}{\sqrt{\rho}},
$$

errors in the atmospheric-property estimate propagate directly into the reconstructed airflow magnitude.

See [ISA.py](simulacion/functions/ISA.py).

---

## Wind-vector reconstruction

The processing path combines the airflow estimate with vehicle motion.

A representative Earth/NED-frame relation is

$$
\mathbf V_{\mathrm{wind}}^{\,NED}
=
\mathbf V_{\mathrm{Pitot}}^{\,e}
-
\mathbf V_{\mathrm{vehicle}}^{\,e}.
$$

The repository also includes a weighted combination utility for GPS- and IMU-derived velocity information:

$$
\mathbf V_{\mathrm{state}}
=
\frac{
w_{\mathrm{GPS}}\mathbf V_{\mathrm{GPS}}
+
w_{\mathrm{IMU}}\mathbf V_{\mathrm{IMU}}
}{
w_{\mathrm{GPS}}
+
w_{\mathrm{IMU}}
}.
$$

See [V_Wind.py](simulacion/functions/V_Wind.py).

---

## IMU velocity integration

Short-window inertial reconstruction uses numerical integration of measured acceleration:

$$
\mathbf v(t)
=
\mathbf v(t_0)
+
\int_{t_0}^{t}
\mathbf a(\tau)\,d\tau.
$$

The utility [calcVelocity.py](simulacion/functions/calcVelocity.py) applies this operation component-wise.

This calculation is drift-sensitive. It is useful for short-window reconstruction and comparison, but it should not be interpreted as a drift-free standalone velocity estimator.

---

## Wind-tunnel calibration

<p align="center">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/windtunnel.webp" width="48%" alt="Wind-tunnel testing">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/wind-results.webp" width="48%" alt="Wind-tunnel results">
</p>

The wind-tunnel stage was used to connect sensor placement and pressure measurements with the airflow quantities required by the post-processing model.

Repository evidence includes:

- [functions_testing.ipynb](Tests/functions_testing.ipynb)
- [tunnel_sampling.ipynb](Tests/tunnel_sampling.ipynb)
- [test_tunnel_code.py](Tests/test_tunnel_code.py)
- recorded tunnel datasets under [Tests/](Tests/)

The role of this stage is calibration and characterization; it should not be conflated with full-flight validation.

---

## Flight instrumentation and reconstruction

The flight-processing material includes:

- recorded flight data;
- onboard sensor measurements;
- frame conversions;
- trajectory reconstruction utilities;
- atmospheric-property estimation;
- map/trajectory visualization.

Key files include:

- [main.ipynb](simulacion/main.ipynb)
- [proccesor.ipynb](simulacion/proccesor.ipynb)
- [datos_vuelo_200_filas.csv](simulacion/datos_vuelo_200_filas.csv)
- [Prueba_recolectada.txt](simulacion/Prueba_recolectada.txt)
- [map.html](simulacion/map.html)

---

## Physical mission evidence

<p align="center">
  <a href="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/media/projects/volta-launch.mp4">
    <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/tower.webp" width="760" alt="Atmospheric probe mission integration">
  </a>
</p>

The linked clip provides launch-context footage from the Spaceport America Cup campaign in which the probe payload was integrated.

<p align="center">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/model.webp" width="48%" alt="Probe model">
  <img src="https://raw.githubusercontent.com/kosmicplane/kosmicplane.github.io/main/assets/images/research/udea/recovery.webp" width="48%" alt="Recovered probe">
</p>

These images document physical integration and recovery without repeating the CAD, avionics, or wind-tunnel figures used earlier.

---

## Validation hierarchy

The evidence should be interpreted in the following order:

~~~text
analytical relation
→ numerical processing
→ CFD / sensor-placement study
→ wind-tunnel calibration
→ integrated instrumentation
→ flight-data reconstruction
~~~

Each stage answers a different question. Agreement at one stage should not be presented as validation of a stronger stage that was not tested.

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

This repository is a research and engineering implementation of the probe's **measurement and reconstruction pipeline**.

The mathematical relations depend on:

- differential-pressure calibration;
- air-density estimation;
- frame conventions;
- sensor alignment;
- inertial drift;
- time synchronization;
- the validity of the selected flow assumptions.

For that reason, equations, numerical processing, wind-tunnel data, and flight measurements are kept conceptually distinct throughout the documentation.
