#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
11/9/23
Intensive Data Science 2
6 - Python matplotlib
https://docs.google.com/document/d/10PMM3EWpwUMkmsPhgSKo4WSOV328Qbd3FWcDB6f9S9A/

Final example with sinx and cosx on subplots.
"""

import numpy as np
import matplotlib.pyplot as plt


# OPTIONAL fun style based on xkcd comics
# Can adjust "amplitude" and "period"
plt.xkcd(1, 100)


# Create figure and axes (two rows, one column)
fig, (ax, ax2) = plt.subplots(2, 1)

# Set title and labels
fig.suptitle("Plotting Trigonometric Functions", fontsize=14)
#ax.set_title("First Plot")
ax.set_ylabel("sin(x)")
ax2.set_ylabel("cos(x)")
ax2.set_xlabel("x")


# Setting up first plot: sin(x)
# Plot dotted line
x = np.linspace(0, 4*np.pi, 1000)
y = np.sin(x)

ax.plot(x, y, color='red', linewidth=4, linestyle='--')

# Plot key points
#x2 = [0, np.pi, np.pi*2]  # Could manually indicate points
x2 = np.linspace(0, 4*np.pi, 9)
y2 = np.sin(x2)

ax.plot(x2, y2, color='red', marker='o',
        markersize=10, linestyle='')


# Setting up the second plot: cos(x)
# Use the same x-points as sin(x), but with cos
y_cos = np.cos(x)
y2_cos = np.cos(x2)

ax2.plot(x, y_cos, color='teal', linewidth=4,
        linestyle='--')

ax2.plot(x2, y2_cos, color='teal', marker='o',
        markersize=10, linestyle='')


# Set face / background color
ax.set_facecolor("mistyrose")
ax2.set_facecolor("azure")

# Adjust layout; tight prevents overlaps
fig.tight_layout()

# Set figure dimensions (length x height) and resolution
fig.set_size_inches(8, 6)
fig.set_dpi(300)
