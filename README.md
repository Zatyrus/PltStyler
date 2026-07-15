# PltStyler
A simple package to provide a collection of stylesheets and default values for Python matplotlib figures. The goal is to make it easy to create visually appealing and consistent plots with minimal effort.

I will add more stylesheets and default values in the future! If you have any suggestions or want to contribute, feel free to open an issue or a pull request.

# Installation
You can install PltStyler using pip:
```bash
pip install PltStyler
```

# Usage
To use PltStyler, simply import the desired stylesheet and apply it to your matplotlib figures. For example:
```python
import matplotlib.pyplot as plt
from PltStyler import PltStyler

# Apply the default stylesheet
PltStyler().apply()

# Apply a predefined stylesheet (e.g., "dark")
PltStyler().set_stylesheet("dark").apply()

# Apply a custom stylesheet - must be json (see below for an example)
PltStyler().set_stylesheet("path/to/stylesheet.json").apply()

# Change the font
PltStyler().set_font(family="Arial", weight="normal").apply()

# Because the PltStyler is a singleton and the methods return the instance itself, you can chain the methods together for conveniently readable code:
PltStyler().set_stylesheet("dark").set_font(family="Arial", weight="normal").apply()

# The PltStyler inclused default parameters for the following plot types:
# - Line plots
# - Scatter plots
# - Box plots
# - Histograms

lineplot_defaults = PltStyler().get_lineplot_defaults()

# Create a sample plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, **lineplot_defaults) # apply lineplot defaults
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```