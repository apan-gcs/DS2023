#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
11/14/23
Intensive Data Science 2
6 - Python matplotlib
https://docs.google.com/document/d/10PMM3EWpwUMkmsPhgSKo4WSOV328Qbd3FWcDB6f9S9A/

Examples of histograms.
"""

import numpy as np
import matplotlib.pyplot as plt


# OPTIONAL fun style based on xkcd comics
# Can adjust "amplitude" and "period"
#plt.xkcd(1, 100)

# Create figure and axis
fig, ax = plt.subplots()


# EXAMPLE 1. With random numbers

# Randomly generate 1000 numbers on standard normal dist.
#z = np.random.normal(0, 1, 1000)

# Set up bins: 0.5 between -3.5 and 3.5
#bins = np.arange(-3.5, 4.0, 0.5)

# Plot histogram with density and specific x-y limits
#ax.hist(z, bins=bins, density=True)
#ax.set_xlim(-3.5, 3.5)
#ax.set_ylim(0, .45)



# EXAMPLE 2. Test scores

# Set title and labels
ax.set_title("Math Grades")
ax.set_ylabel("Frequency")
ax.set_xlabel("Grade")

# Sample grade data
z = [82, 74, 78, 68, 88, 82, 74, 86, 70, 88, 94, 96, 92, 88, 90, 78, 82,
     94, 74, 100, 92, 76, 98, 72, 68, 86]

# Plot histograms with specific bins
ax.hist(z, bins=np.arange(65, 105, 5), rwidth=.95)

# Set x- and y-axis limits
ax.set_xlim(63, 102)
ax.set_ylim(0, 5.3)

# Calculate average/mean
average = np.mean(z).round(1)

# Vertical line at average
ax.vlines(average, 0, 5.3, color='black', linestyle='--')

# Annotate average: coords for arrow location, text location
ax.annotate(f"Avg:\n{average}", (83.5, 4.5), (80, 4.3),
            arrowprops={"arrowstyle":"->"},
            horizontalalignment='center')


# Version 2: Smaller bin sizes
# Without anotation
#ax.hist(z, bins=np.arange(67.5, 102.5, 2.5), rwidth=.95)
#ax.set_ylim(0, 3.2)
#ax.vlines(average, 0, 3.2, color='black', linestyle='--')


# Set face / background color
ax.set_facecolor("azure")


# Adjust layout; tight prevents overlaps
fig.tight_layout()

# Set figure dimensions (length x height) and resolution
#fig.set_size_inches(6, 4)
#fig.set_dpi(300)
