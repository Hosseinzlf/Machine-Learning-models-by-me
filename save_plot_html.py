#Author: Hossein Zolfaghari
#May 2022

import plotly.graph_objects as go
import plotly
import numpy as np


# Create traces
fig = go.Figure()
#plot number 1 with line mode, name title of plot, x , and y.
fig.add_trace(go.Scatter(x=list(range(len(y_pred))), y= inputs_sc[:,2],
                    mode='lines',
                    name='Measured GHI Data'))
#plot number 2                    
fig.add_trace(go.Scatter(x=list(range(len(y_pred))), y= y_pred[:,2],
                    mode='lines',
                    name='Predicted GHI data'))
#Adding xlabel, ylabel, title
fig.update_layout(title='Model dropout',
                   xaxis_title='GHI index',
                   yaxis_title='GHI Normalized Value')
fig.show()
#Give address and the name of the file to save as html
plotly.io.write_html(fig, "/content/output.html")
