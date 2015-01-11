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


def count_tree_leafs(decision_tree):
    """Count the number of leaf nodes in decision_tree."""

    result = 0
    feature_name = decision_tree.keys()[0]
    children = decision_tree[feature_name]
    for child_feature_name in children:
        if type(children[child_feature_name]).__name__ == 'dict':
            result += count_tree_leafs(children[child_feature_name])
        else:
            result += 1

    return result


def count_tree_depth(decision_tree):
    """Count the depth of decision_tree."""

    result = 0
    feature_name = decision_tree.keys()[0]
    children = decision_tree[feature_name]
    for child_feature_name in children:
        if type(children[child_feature_name]).__name__ == 'dict':
            depth_from_here = (1 + count_tree_depth(children[child_feature_name]))
        else:
            depth_from_here = 1
        if depth_from_here > result:
            result = depth_from_here

    return result


def plot_mid_text(center_point, parent_point, text_string):
    """Plot text_string midway between center_point and parent_point."""

    x_midpoint = (parent_point[0] - center_point[0]) / 2.0 + center_point[0]
    y_midpoint = (parent_point[1] - center_point[1]) / 2.0 + center_point[1]

    create_plot.ax1.text(x_midpoint, y_midpoint, text_string)


def plot_tree(decision_tree, parent_point, node_text):
    """Plot decision_tree beginning at parent_point with initial node_text."""

    count_leafs = count_tree_leafs(decision_tree)
    root_feature_name = decision_tree.keys()[0]

    # Plot node_text
    center_point = (plot_tree.x_offset + (1.0 + float(count_leafs)) / 2.0 / plot_tree.total_width,
                    plot_tree.y_offset)
    plot_mid_text(center_point, parent_point, node_text)

    plot_node(root_feature_name, center_point, parent_point, decision_node)
    children = decision_tree[root_feature_name]
    plot_tree.y_offset -= 1.0 / plot_tree.total_depth
    for child_feature_name in children:
        if type(children[child_feature_name]).__name__ == 'dict':
            plot_tree(children[child_feature_name], center_point, str(child_feature_name))
        else:
            plot_tree.x_offset += 1.0 / plot_tree.total_width
            plot_node(children[child_feature_name], (plot_tree.x_offset, plot_tree.y_offset), center_point, leaf_node)
            plot_mid_text((plot_tree.x_offset, plot_tree.y_offset), center_point, str(root_feature_name))

    plot_tree.y_offset += 1.0 / plot_tree.total_depth


def create_plot(decision_tree):
    """Create a plot of created decision tree."""

    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axis_properties = dict(xticks=[], yticks=[])
    create_plot.ax1 = plt.subplot(111, frameon=False, **axis_properties)

    plot_tree.total_width = float(count_tree_leafs(decision_tree))
    plot_tree.total_depth = float(count_tree_depth(decision_tree))

    plot_tree.x_offset = -0.5 / plot_tree.total_width
    plot_tree.y_offset = 1.0

    plot_tree(decision_tree, (0.5, 1.0), '')

    plt.show()


def test_tree(index):
    """Get a test tree at index."""

    trees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
        {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return trees[index]
