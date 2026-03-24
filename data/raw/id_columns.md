# {id}.csv — Spaltenbeschreibung (Zeitreihendaten)

Jede Datei `{id}.csv` enthält die Messzeitreihe eines einzelnen Versuchslaufs.
Der Dateiname entspricht der `id` aus `runs.csv` (z.B. `22605.csv`).

## Format

- **Index (Spalte 0):** Zeit in Sekunden (float), wird von `mdl.load_run()` automatisch in `pd.TimedeltaIndex` umgewandelt
- **Trennzeichen:** Komma (`,`)
- **Dezimaltrennzeichen:** Punkt (`.`)

---

## Spalten

### Rumpf / Beschleunigung

| Spalte | Einheit | Erklärung |
|--------|---------|-----------|
| `Hull/Acc/Z3` | m/s² | Vertikale Beschleunigung am Rumpfmesspunkt Z3 |

---

### Propeller

| Spalte | Einheit | Erklärung |
|--------|---------|-----------|
| `Prop/PS/Rpm` | rpm | Drehzahl Propeller Backbord (Port Side) |
| `Prop/PS/Thrust` | N | Schub Propeller Backbord |
| `Prop/PS/Torque` | Nm | Drehmoment Propeller Backbord |
| `Prop/SB/Rpm` | rpm | Drehzahl Propeller Steuerbord (Starboard) |
| `Prop/SB/Thrust` | N | Schub Propeller Steuerbord |
| `Prop/SB/Torque` | Nm | Drehmoment Propeller Steuerbord |

> `thrust = Prop/PS/Thrust + Prop/SB/Thrust` (Gesamtschub, in `mdl.load_test()` berechnet)

---

### Ruder

| Spalte | Einheit | Erklärung |
|--------|---------|-----------|
| `Rudder/Angle` | ° | Aktueller Ruderwinkel (wird zu `delta` umbenannt in `preprocess_run()`) |
| `Rudder/MaxAngle` | ° | Maximaler Ruderwinkel (Begrenzer) |
| `Rudder/Rate` | °/s | Rudergeschwindigkeit (Änderungsrate) |

---

### Bewegung / Lage (Modellkoordinaten)

| Spalte | Einheit | Erklärung |
|--------|---------|-----------|
| `roll` | rad | Rollwinkel (φ) um Längsachse |
| `pitch` | rad | Stampfwinkel (θ) um Querachse |
| `psi` | rad | Kurswinkel (ψ) um Hochachse (Yaw) |
| `x0` | m | Position in x-Richtung (längs, laborgebunden) |
| `y0` | m | Position in y-Richtung (quer, laborgebunden) |
| `z0` | m | Position in z-Richtung (vertikal, laborgebunden) |

---

### Umgebung

| Spalte | Einheit | Erklärung |
|--------|---------|-----------|
| `lab/WaveHeight` | m | Wellenhöhe im Tank (Labormessung) |
| `Wind/GWA` | ° | Geographic Wind Angle — Windrichtung relativ zum Schiff |
| `Wind/Course` | ° | Windkurs (absolut im Labor) |

---

### Windgenerator / Fan (optional, nur bei GWA-Versuchen)

| Spalte | Einheit | Erklärung |
|--------|---------|-----------|
| `Fan/Fore/AngleOrder2` | ° | Sollwinkel des vorderen Windgenerators |
| `Fan/Fore/FxOrder` | N | Sollkraft des vorderen Windgenerators in x-Richtung |
| `Fan/Fore/Rate` | — | Änderungsrate des vorderen Windgenerators |
| `Fan/Aft/Fx` | N | Kraft des hinteren Windgenerators in x-Richtung |

---

## Abgeleitete Größen (nach `preprocess_run()`)

Diese Spalten sind **nicht** in der Rohdatei, sondern werden berechnet:

| Spalte | Erklärung |
|--------|-----------|
| `delta` | Ruderwinkel (umbenannt aus `Rudder/Angle`) |
| `u` | Längsgeschwindigkeit im körperfesten System [m/s] |
| `v` | Quergeschwindigkeit im körperfesten System [m/s] |
| `r` | Gierrate (Yaw Rate) [rad/s] |
| `thrust` | Gesamtschub `Prop/PS/Thrust + Prop/SB/Thrust` [N] |
| `U` | Gesamtgeschwindigkeit `sqrt(u² + v²)` [m/s] |
