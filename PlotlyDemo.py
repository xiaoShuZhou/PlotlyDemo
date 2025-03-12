# Import necessary libraries
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Sample data: Sales by product category over months
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Electronics': [300, 320, 310, 340, 360],
    'Clothing': [150, 160, 170, 165, 180],
    'Books': [80, 85, 90, 95, 100]
}

# Create a DataFrame
df = pd.DataFrame(data)

# 1. Bar Chart with Plotly Express
bar_fig = px.bar(df, x='Month', y=['Electronics', 'Clothing', 'Books'], 
                 barmode='group', title='Monthly Sales by Category',
                 labels={'value': 'Sales ($)', 'variable': 'Category'})

# 2. Line Chart with Plotly Express
line_fig = px.line(df, x='Month', y=['Electronics', 'Clothing', 'Books'], 
                   title='Sales Trend Over Months',
                   labels={'value': 'Sales ($)', 'variable': 'Category'})

# 3. Combined Chart with Plotly Graph Objects
combined_fig = go.Figure()

# Add bar traces
combined_fig.add_trace(go.Bar(x=df['Month'], y=df['Electronics'], name='Electronics'))
combined_fig.add_trace(go.Bar(x=df['Month'], y=df['Clothing'], name='Clothing'))
combined_fig.add_trace(go.Bar(x=df['Month'], y=df['Books'], name='Books'))

# Add line traces
combined_fig.add_trace(go.Scatter(x=df['Month'], y=df['Electronics'], mode='lines+markers', name='Electronics Trend'))
combined_fig.add_trace(go.Scatter(x=df['Month'], y=df['Clothing'], mode='lines+markers', name='Clothing Trend'))
combined_fig.add_trace(go.Scatter(x=df['Month'], y=df['Books'], mode='lines+markers', name='Books Trend'))

# Update layout
combined_fig.update_layout(title='Combined Sales Visualization',
                          xaxis_title='Month',
                          yaxis_title='Sales ($)',
                          barmode='group')

# Show the plots
bar_fig.show()
line_fig.show()
combined_fig.show()