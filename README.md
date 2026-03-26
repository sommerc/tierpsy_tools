## TierPsy Tools

### Installation
---

You need to install [uv](https://docs.astral.sh/uv/getting-started/installation/).

1. Open a terminal
2. Follow instructions to install [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Command Line Tools
---

#### Get callibrated speeds from TierPsy Results

Requirements:

1. Movie `MOVIE.AVI` used for callibration
2. TierPsy Results, i. e. a `Results` folder containing hdf5 files for the `MOVIE.AVI`

Usage:

```bash
uvx --from https://github.com/sommerc/tierpsy_tools.git get_speed MOVIE.AVI
```

1. A Window will pop up showing the first frame of `MOVIE.AVI`.
2. Click on two points in the image of known distance
3. In the terminal, type the known distance in microns

A table will be written containing the worm speeds