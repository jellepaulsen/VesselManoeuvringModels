# runs.csv — Spaltenbeschreibung

`runs.csv` ist eine Teilmenge der `run_selection.csv` (nur erfolgreich verarbeitete Runs)
erweitert um die Spalte `sailing`. Index-Spalte ist `id`.

---

## Identifikation & Verwaltung

| Spalte | Erklärung |
|--------|-----------|
| `id` | Eindeutige numerische Run-ID (Primärschlüssel) |
| `project_number` | Projektnummer des Modellversuchs |
| `series_number` | Seriennummer innerhalb des Projekts |
| `run_number` | Laufnummer innerhalb eines Tests |
| `test_number` | Testnummer innerhalb einer Serie |
| `model_number` | Bezeichnung des physischen Schiffsmodells (z.B. `M5139-02-A`) |
| `ship_name` | Name des Schiffs / Modells |
| `loading_condition_id` | ID des Beladungszustands (referenziert Beladungstabelle) |
| `ascii_name` | Alternativer ASCII-kompatibler Name des Runs |
| `date` | Datum des Versuchsdurchlaufs (Format: YYYY-MM-DD) |
| `facility` | Prüfanlage / Schlepprinne (z.B. `MDL` = Maritime Dynamics Laboratory, SSPA) |

---

## Versuchsparameter

| Spalte | Erklärung |
|--------|-----------|
| `ship_speed` | Schiffsgeschwindigkeit (normiert, dimensionslos) |
| `comment` | Freitextkommentar zum Run (z.B. `12.0 kn`, `GWA`) |
| `test_type` | Versuchstyp (z.B. `reference speed`, `rodergrundvinkel`, `sailing`, `zig-zag`) |
| `angle1` | Erster Ruderwinkel [°] |
| `angle2` | Zweiter Ruderwinkel [°] (z.B. bei Zickzack-Manövern) |
| `Körfallstyp` | Versuchstyp auf Schwedisch (SSPA-interne Klassifikation) |
| `sailing` | `True` wenn `test_type == 'sailing'` ODER `comment` enthält `'GWA'` (Geographic Wind Angle — Versuch unter Windeinfluss), sonst `False` |

---

## Dateipfade

| Spalte | Erklärung |
|--------|-----------|
| `file_path_ascii` | Pfad zur ASCII-Messdatendatei |
| `file_path_ascii_temp` | Temporärer ASCII-Pfad (Zwischenspeicherung) |
| `file_path_log` | Pfad zur Log-Datei des Versuchs |
| `file_path_hdf5` | Pfad zur HDF5-Messdatendatei (Hauptdatenquelle, auf SSPA-Netzlaufwerk) |

---

## Modellmaßstab & Beladung

| Spalte | Einheit | Erklärung |
|--------|---------|-----------|
| `scale_factor` | — | Maßstabsfaktor Modell → Schiff (z.B. 41.2) |
| `name` | — | Name des Beladungszustands (z.B. `Design`) |

---

## Hydro­statische Schiffsdaten (Modellmaßstab)

| Spalte | Einheit | Erklärung |
|--------|---------|-----------|
| `lcg` | m | Längsschwerpunkt (Longitudinal Centre of Gravity), bezogen auf Lpp/2 |
| `kg` | m | Abstand Kiel–Schwerpunkt (Keel to Centre of Gravity) |
| `gm` | m | Metazentrische Höhe (Transversal) |
| `CW` | — | Wasserlinienfläche-Koeffizient |
| `TF` | m | Tiefgang vorn (Forward Draft) |
| `TA` | m | Tiefgang achtern (Aft Draft) |
| `BWL` | m | Breite an der Konstruktionswasserlinie |
| `KXX` | m | Trägheitsradius um die Längsachse (Roll) |
| `KZZ` | m | Trägheitsradius um die Hochachse (Yaw) |
| `BTT1` | m | Breite (spezifischer Querschnitt, SSPA-intern) |
| `CP` | — | Prismatischer Koeffizient |
| `Volume` | m³ | Verdrängungsvolumen |
| `A0` | m² | Querschnittsfläche des Hauptspants |
| `RH` | m | Hydraulischer Radius |
| `lpp` | m | Länge zwischen den Loten (Length between Perpendiculars) |
| `beam` | m | Größte Schiffsbreite |
| `LOA` | m | Länge über alles (Length Overall) |

---

## Anhänge & Zusatzgeometrie (oft leer)

| Spalte | Erklärung |
|--------|-----------|
| `ABULB` | Querschnittsfläche des Bugwulstes |
| `BKX` | Längsposition der Schlingerkiele |
| `BKL` | Länge der Schlingerkiele |
| `BKB` | Breite der Schlingerkiele |
| `TWIN` | Twin-Screw-Flag (Zwillingsschraubenanordnung) |
| `DCLR` | Propeller-Rumpf-Abstand (Clearance) |
| `VDES` | Design-Geschwindigkeit |
| `RHBL` | Hydraulischer Radius Bilgenkiel |
| `ASKEG` | Querschnittsfläche des Kiels |
| `LSKEG` | Länge des Kiels |
| `XSKEG` | Längsposition des Kiels |
| `HSKEG` | Höhe des Kiels |
| `RSKEG` | Radius des Kiels |
| `PD` | Steigungsverhältnis des Propellers (Pitch/Diameter) |
| `ARH` | Ruderfläche |
| `CFP` | Propellerflächen-Koeffizient |
| `AIX` | Querschnittsfläche (intern) |
| `PDTDES` | Design-Steigungsverhältnis |
| `RTYPE` | Rudertyp |
| `SFP` | Schlupffaktor Propeller |
| `PROT` | Propellerdrehrichtung |
| `D` | Propellerdurchmesser |
| `RR` | Ruderbalance-Verhältnis |
| `XSKEG` | Längsposition des Kiels |
| `NDES` | Design-Drehzahl Propeller |
| `AR` | Ruderfläche (alternativ) |
| `BR` | Ruderbreite |
| `BRA` | Ruderbalance-Fläche |
| `IRUD` | Ruder-ID / Rudertyp-Index |
| `PTYPE` | Propellertyp |
| `XRUD` | Längsposition des Ruders |
| `AI` | Einlaufbereich-Fläche (Intake Area) |

---

## Messpunkt-Koordinaten (Modell)

| Spalte | Einheit | Erklärung |
|--------|---------|-----------|
| `xm` | m | x-Koordinate des Messpunkts im Modell (längs) |
| `ym` | m | y-Koordinate des Messpunkts im Modell (quer) |
| `zm` | m | z-Koordinate des Messpunkts im Modell (vertikal, z.B. `-0.214`) |

---

## Sonstiges

| Spalte | Erklärung |
|--------|-----------|
| `ship_type_id` | Numerische ID des Schiffstyps |
