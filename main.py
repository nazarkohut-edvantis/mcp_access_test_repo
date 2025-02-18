import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class BaseVisualizer:
    """
    Base class for visualization.
    """
    def __init__(self, data):
        """
        Initialize with dataset.
        :param data: Data to be visualized (can be a Pandas DataFrame, list, etc.)
        """
        self.data = data

    def plot(self):
        """
        Base method to plot, should be overridden by child classes.
        """
        raise NotImplementedError("Subclasses should implement this method.")


class HistogramVisualizer(BaseVisualizer):
    """
    Visualization for histograms.
    """
    def __init__(self, data, bins=10):
        super().__init__(data)
        self.bins = bins

    def plot(self):
        """
        Creates and displays a histogram for the provided data.
        """
        plt.figure(figsize=(10, 6))
        plt.hist(self.data, bins=self.bins, color='blue', alpha=0.7)
        plt.title("Histogram Visualization")
        plt.xlabel("Data Values")
        plt.ylabel("Frequency")
        plt.show()


if __name__ == "__main__":
    # Generate example data
    np.random.seed(42)
    data = pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': np.random.rand(100)
    })

    # Instantiate and plot visualizations
    hist_viz = HistogramVisualizer(data['A'])
    hist_viz.plot()
