# Vienna Fountains
## What it does
This CLI tool downloads the current dataset from our governments open data site of where Water Fountains are located and stores it in a json using the requests library. Once provided with latitude and longitude it will calculate the haversine for each fountain in the dataset related to the location and print the 5 nearest ones to you.

## Installation
Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).
```bash
git clone https://github.com/<your-username>/vienna-fountains.git
cd vienna-fountains
uv sync
```

`uv sync` installs the dependencies listed in `pyproject.toml`.
## Usage
Fetch/update the fountain dataset (writes `fountains.json`):
```bash
uv run fetch.py
```

Find the 5 nearest fountains to a location:
```bash
uv run main.py --lat --lon
```
Example:
- uv run main.py --lat 48.2 --lon 16.3

Example output
[(Fountain(7036342, 48.19980533, 16.30413646, 4, Trinkbrunnen), 0.30733767706838966), (Fountain(7037214, 48.1973046, 16.30299824, 7, Auslaufbrunnen), 0.37310978412154244), (Fountain(7037934, 48.20257335, 16.29577575, 18, Trinkhydrant mit Tränke), 0.4241373629427147), (Fountain(7036795, 48.19660037, 16.30319849, 11, Sprühnebeldusche), 0.4462058918529787), (Fountain(7037846, 48.20386536, 16.3020514, 18, Trinkhydrant mit Tränke), 0.45590521622546903)]

## TODO:
Type filtering, more intuitive commands, mayhaps even loopup or gui wrapper

## Done already
Haversine, Proper EPSG:4326 and UTF8 encoding

## Limitations
Does not currently use a path algorithm, fountains might be switched off in winter. 
## Data source and licence

Fountain locations come from the City of Vienna's open data offering, published by
Magistratsabteilung 31 – Wiener Wasser and catalogued on
[data.gv.at](https://www.data.gv.at/katalog/datasets/2ed52078-7e55-40ea-8036-0d89118a06f4).

The data is retrieved from the city's WFS endpoint as GeoJSON:

    https://data.wien.gv.at/daten/geo?service=WFS&request=GetFeature
      &version=1.1.0&typeName=ogdwien:TRINKBRUNNENOGD
      &srsName=EPSG:4326&outputFormat=json

Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.de).

> Datenquelle: Stadt Wien – https://data.wien.gv.at

**A note on the schema:** the published metadata documents a `TYP_NUM` / `TYP_TXT`
field pair for the fountain category. The live WFS response no longer returns these —
the equivalent fields are now `BASIS_TYP` and `BASIS_TYP_TXT`. This project reads the
current field names.