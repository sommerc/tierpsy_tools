## TierPsy Tools

### Installation

You need to install [uv]()

#### Get callibrated speeds from TierPsy Results
Requirements:

1. Movie `MOVIE.AVI` used for callibration
2. TierPsy Results, i. e. a `Results` folder containing hdf5 files for the `MOVIE.AVI`

Usage:

```bash
uvx --from https://github.com/sommerc/tierpsy_tools.git get_speed MOVIE.AVI
```