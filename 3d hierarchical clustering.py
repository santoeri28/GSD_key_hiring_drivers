# Paper: Uncovering Key Drivers in Selecting Professionals for Global Software Development and Gig Economy
# Appendix D - 3D bubble chart to present an interactive hierarchical clustering graph illustrating the hierarchical structure of clusters for the recruitment of professionals.

# Import 
import plotly.express as px
import numpy as np
import pandas as pd

# Load your DataFrame
mydataset = "https://raw.githubusercontent.com/santoeri28/santoeri28.gsd.key.io/main/file_3Dcsv2.csv"
df = pd.read_csv(mydataset, sep=';', on_bad_lines='skip')
df.head()


fig = px.scatter_3d(df, x='Ri - Di', y='Ri + Di', z='Cosine Sim', size='Ri + Di', color='W_cluster',
                    hover_data=['Description'])
fig.update_layout(scene_zaxis_type="log")
fig.show()