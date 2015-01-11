"""Plot a decision tree for easier (human) verification."""


import matplotlib.pyplot as plt


__author__ = 'l.jones'



# Options for different visual elements
decision_node = dict(boxstyle='sawtooth', fc='0.8')
leaf_node = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='<-')


def plot_node(node_text, center_point, parent_point, node_type):
    """Plot a node of node_type having node_text at center_point from parent_point."""

    # Note that create_plot is the name of a function. Strange...
    create_plot.ax1.annotate(node_text, xy=parent_point, xycoords='axes fraction', xytext=center_point,
                             textcoords='axes fraction', va='center', ha='center', bbox=node_type,
                             arrowprops=arrow_args)


def create_plot():
    """Create a plot of created decision tree."""

    fig = plt.figure(1, facecolor='white')
    fig.clf()
    create_plot.ax1 = plt.subplot(111, frameon=False)
    plot_node('a decision node', (0.5, 0.1), (0.1, 0.5), decision_node)
    plot_node('a leaf node', (0.8, 0.1), (0.3, 0.8), leaf_node)
    plt.show()


if __name__ == '__main__':
    create_plot()