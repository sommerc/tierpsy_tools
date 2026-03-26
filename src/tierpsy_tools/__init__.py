import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import h5py
import matplotlib.pyplot as plt

from rich.prompt import Prompt
import cv2


def get_pixel_size_from_mov(mov_path):
    try:
        vh = cv2.VideoCapture(mov_path)
        _, img = vh.read()
        fig, ax = plt.subplots()

        ax.imshow(img)
        ax.set_title("Click two points corresponding to a known distance")

        # Let the user click two points
        pts = plt.ginput(2, timeout=-1)

        pixel_distance = -1
        if len(pts) == 2:
            (x1, y1), (x2, y2) = pts
            pixel_distance = np.hypot(x2 - x1, y2 - y1)
            print(f"Distance in pixels: {pixel_distance:.2f}")
        return pixel_distance
    except:
        raise
    finally:
        vh.release()


def extract_speed_over_time(file_path, px_size):

    with h5py.File(file_path, "r") as fh:
        features = fh["timeseries_data"][:]

    tab = pd.DataFrame(features)[["worm_index", "timestamp", "speed"]]
    tab["speed_um/frame"] = tab["speed"] * px_size

    out_tab_fn = file_path.parent / (file_path.stem + "_speed_over_time.csv")

    tab.to_csv(out_tab_fn, index=False)
    print(f"Speeds written to '{out_tab_fn}'")


def get_speed() -> None:
    parser = argparse.ArgumentParser("Get tierpsy speed from movie")
    parser.add_argument(
        "input_movies",
        nargs="+",
        type=Path,
        help="Movie for which tierspy 'Results' are available",
    )

    args = parser.parse_args()

    for mov in args.input_movies:
        res_hdf5_fn = mov.parent / "Results" / (mov.stem + "_featuresN.hdf5")
        if not res_hdf5_fn.exists():
            print(
                f"Results file for that movie '{mov.name}' does not exists... skipping"
            )
            continue

        print(
            f"Extracting Speed for {mov.name}",
        )

        px_distance = get_pixel_size_from_mov(mov)
        mu_distance = Prompt.ask("  - Enter the known distance in um", default="11950")
        mu_distance = float(mu_distance)
        px_size = mu_distance / px_distance

        extract_speed_over_time(res_hdf5_fn, px_size)
        print("Done")


if __name__ == "__main__":
    get_speed()
