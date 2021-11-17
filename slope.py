import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

# Set up the data
data = np.concatenate(
    [[np.random.normal(loc=1, size=15), 15*['site1'], 15*['healthy']],
     [np.random.normal(loc=3, size=15), 15*['site2'], 15*['healthy']],
     [np.random.normal(loc=0, size=15), 15*['site3'], 15*['healthy']],
     [np.random.normal(loc=1, size=15), 15*['site1'], 15*['disease']],
     [np.random.normal(loc=1, size=15), 15*['site2'], 15*['disease']],
     [np.random.normal(loc=3, size=15), 15*['site3'], 15*['disease']]],
    axis=1)
df = pd.DataFrame(columns=['value', 'site', 'label'], data=data.T)
df['value'] = df['value'].astype(float)

# Show every ninth row
df.iloc[::9]

fig, ax = plt.subplots(figsize=(4, 3))

# Set up list to track sites
sites = []
i = 1.0
for site, subdf in df.groupby('site'):
    sites.append(site)
    # Get the values for healthy and disease patients
    h = subdf.query('label == "healthy"')['value'].values
    d = subdf.query('label == "disease"')['value'].values

    # Set up the x-axis values
    x1 = i - 0.2
    x2 = i + 0.2

    # Plot the lines connecting the dots
    for hi, di in zip(h, d):
        ax.plot([x1, x2], [hi, di], c='gray')

    # Plot the points
    ax.scatter(len(h)*[x1-0.01], h, c='k',
               s=25, label='healthy')
    ax.scatter(len(d)*[x2+0.01], d, c='k',
               s=25, label='disease')


    # Update x-axis
    i += 1

# Fix the axes and labels
ax.set_xticks([1, 2, 3])
_ = ax.set_xticklabels(sites, fontsize='x-large')
