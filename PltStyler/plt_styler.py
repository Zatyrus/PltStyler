## Dependiencies
import json
import os
import matplotlib.pyplot as plt
from typing import Dict, Any, NoReturn, Union


class PltStyler:
    stylesheet: Dict[str, Any]
    available_stylesheets: list
    verbose: bool

    def __init__(
        self, stylesheet: Union[str, Dict[str, Any]] = None, verbose: bool = False
    ) -> "PltStyler":
        # set verbosity level for debug output
        self.verbose = verbose

        # check available stylesheets in the stylesheets directory
        self.available_stylesheets = self.check_available_stylesheets()

        # check if the provided stylesheet is a string (path to JSON file) or a dictionary, and load it accordingly
        if isinstance(stylesheet, str):
            if stylesheet in self.available_stylesheets:
                # Load the predefined stylesheet
                with open(
                    os.path.join(
                        os.path.dirname(__file__), "stylesheets", f"{stylesheet}.json"
                    ),
                    "r",
                ) as f:
                    self.stylesheet = json.load(f)
            else:
                # Load the custom stylesheet from the provided path
                with open(stylesheet, "r") as f:
                    self.stylesheet = json.load(f)

            if self.verbose:
                print(f"Stylesheet provided as a string, loaded from {stylesheet}.")

        elif isinstance(stylesheet, dict):
            self.stylesheet = stylesheet
            if self.verbose:
                print("Stylesheet provided as a dictionary, using provided settings.")

        else:
            self.stylesheet = {
                "style": "default",
                "font": {"family": "DejaVu Sans", "weight": "bold", "size": 12},
            }

            if self.verbose:
                print("No stylesheet provided, using default settings.")

    # %% Colorbar styling method
    def make_color_axis(
        self, data: Any, cmap: str = "viridis", normalize: bool = True
    ) -> plt.Axes:
        norm = plt.Normalize(vmin=data.min(), vmax=data.max()) if normalize else None
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        return sm

    def make_colorbar(
        self,
        data: Any,
        cmap: str = "viridis",
        label: str = "Colorbar",
        fontsize: int = 12,
        fontweight: str = "bold",
    ) -> None:
        cbar = plt.colorbar(self.make_color_axis(data, cmap=cmap))
        cbar.set_label(label, fontsize=fontsize, fontweight=fontweight)
        return cbar

    # %% Default parameters for different plot types
    def get_default_parameters(self, plot_type: str) -> Dict[str, Any]:
        default_parameters_dir = os.path.join(
            os.path.dirname(__file__), "default_parameters"
        )
        default_parameters_path = os.path.join(
            default_parameters_dir, f"{plot_type}.json"
        )

        if os.path.exists(default_parameters_path):
            with open(default_parameters_path, "r") as f:
                default_parameters = json.load(f)
            return default_parameters
        else:
            raise ValueError(
                f"No default parameters found for plot type '{plot_type}'."
            )

    # %% Stylesheet management methods
    def reset_style(self) -> NoReturn:
        plt.style.use("default")

    def reset_font(self) -> NoReturn:
        plt.rc("font", family="DejaVu Sans", weight="bold", size=12)

    def check_available_stylesheets(self) -> list:
        stylesheets_dir = os.path.join(os.path.dirname(__file__), "stylesheets")
        available_stylesheets = [
            f[:-5] for f in os.listdir(stylesheets_dir) if f.endswith(".json")
        ]
        return available_stylesheets

    def check_available_default_parameters(self) -> list:
        default_parameters_dir = os.path.join(
            os.path.dirname(__file__), "default_parameters"
        )
        available_default_parameters = [
            f[:-5] for f in os.listdir(default_parameters_dir) if f.endswith(".json")
        ]
        return available_default_parameters

    def reset_stylesheet(self) -> NoReturn:
        # load the default stylesheet from the stylesheets directory
        with open(
            os.path.join(os.path.dirname(__file__), "stylesheets/matplotlib.json"),
            "r",
        ) as f:
            self.stylesheet = json.load(f)

        # enforce the default stylesheet
        plt.style.use(self.stylesheet["style"])
        plt.rc("font", **self.stylesheet["font"])

    # %% Methods to set and apply stylesheets and fonts
    def set_font(
        self, family: str = "DejaVu Sans", weight: str = "bold", size: int = 12
    ) -> "PltStyler":
        self.stylesheet["font"]["family"] = family
        self.stylesheet["font"]["weight"] = weight
        self.stylesheet["font"]["size"] = size

        return self

    def set_style(self, style: str) -> "PltStyler":
        self.stylesheet["style"] = style

        return self

    def set_stylesheet(self, stylesheet: Union[str, Dict[str, Any]]) -> "PltStyler":
        # check if the provided stylesheet is a string (path to JSON file) or a dictionary, and load it accordingly
        if isinstance(stylesheet, str):
            if stylesheet in self.available_stylesheets:
                # Load the predefined stylesheet
                with open(
                    os.path.join(
                        os.path.dirname(__file__), "stylesheets", f"{stylesheet}.json"
                    ),
                    "r",
                ) as f:
                    self.stylesheet = json.load(f)
            else:
                # Load the custom stylesheet from the provided path
                with open(stylesheet, "r") as f:
                    self.stylesheet = json.load(f)

            if self.verbose:
                print(f"Stylesheet provided as a string, loaded from {stylesheet}.")

        elif isinstance(stylesheet, dict):
            self.stylesheet = stylesheet
            if self.verbose:
                print("Stylesheet provided as a dictionary, using provided settings.")

        else:
            raise ValueError(
                "Stylesheet must be either a string (path to JSON file) or a dictionary."
            )

        return self

    def apply_style(self) -> NoReturn:
        plt.style.use(self.stylesheet["style"])

    def apply_font(self) -> NoReturn:
        plt.rc("font", **self.stylesheet["font"])

    def apply_stylesheet(self) -> NoReturn:
        # reset to default to avoid compounding styles when calling this method multiple times
        self.reset_style()
        self.reset_font()

        # enforce the stylesheet
        plt.style.use(self.stylesheet["style"])
        plt.rc("font", **self.stylesheet["font"])
