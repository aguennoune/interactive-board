#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports
import pandas as pd
import numpy as np
import panel as pn
pn.extension('tabulator')

import hvplot.pandas


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')


# In[3]:


df


# In[4]:


# Filtering the data by columns
df.columns


# In[5]:


# Filtering the data for the World
df[df['country'] == 'World']


# ##### Draw a sample dashboard for the project to illustrate the visualizations we want to show

# ##### (0) Some minor data processing

# In[6]:


# Fill NAs with 0s and create GDP per capita column
df = df.fillna(0)
df['gdp_per_capita'] = np.where(df['population'] != 0, df['gdp']/ df['population'], 0)


# In[7]:


# Make DataFrame Pipeline Interactive
idf = df.interactive()


# ##### (1) CO2 emission over time by continent

# In[8]:


# Define Panel widgets
year_slider = pn.widgets.IntSlider(name="Year slider", start=1750, end=2020, step=5, value=1850)
year_slider


# In[9]:


# lets have a look at how the data pipeline looks like
co2_pipeline


# In[66]:


# Radio buttons for CO2 measures
yaxis_co2 = pn.widgets.RadioButtonGroup(
    name='Y axis',
    options=['co2', 'co2_per_capita',],
    button_type='success'
)


# In[76]:


continents = ['World', 'Asia', 'Oceania', 'Europe', 'Africa', 'North America', 'South America', 'Antarctica']

co2_pipeline = (
    idf[
        (idf.year <= year_slider) &
        (idf.country.isin(continents))
    ]
    .groupby(['country', 'year'])[yaxis_co2].mean()
    .to_frame()
    .reset_index()
    .sort_values(by='year')
    .reset_index(drop=True)
)


# In[77]:


co2_plot = co2_pipeline.hvplot(x = 'year', by='country', y=yaxis_co2, line_width=2, title="CO2 emission by continent")
co2_plot


# In[78]:


co2_table = co2_pipeline.pipe(pn.widgets.Tabulator, pagination='remote', page_size=10, sizing_mode='stretch_width')
co2_table


# ##### (3) CO2 vs GDP scatterplot

# In[79]:


co2_vs_gdp_scatterplot_pipeline = (
    idf[
        (idf.year == year_slider) &
        (~ (idf.country.isin(continents)))
    ]
    .groupby(['country', 'year', 'gdp_per_capita'])['co2'].mean()
    .to_frame()
    .reset_index()
    .sort_values(by='year')
    .reset_index(drop=True)
)


# In[80]:


# Visualize the co2_vs_gdp_scatterplot_pipeline
co2_vs_gdp_scatterplot_pipeline


# In[81]:


co2_vs_gdp_scatterplot = co2_vs_gdp_scatterplot_pipeline.hvplot(x='gdp_per_capita', y='co2', by='country', size=80, kind="scatter", alpha=0.7, legend=False, height=500, width=500)
co2_vs_gdp_scatterplot


# ##### (4) Bar chart with CO2 sources by continent

# In[82]:


yaxis_co2_source = pn.widgets.RadioButtonGroup(
    name='Y axis',
    options=['coal_co2', 'oil_co2', 'gas_co2'],
    button_type='success'
)

continents_excl_world = ['Asia', 'Oceania', 'Europe', 'Africa', 'North America', 'South America', 'Antarctica']
co2_source_bar_pipeline = (
    idf[
        (idf.year == year_slider) &
        (idf.country.isin(continents_excl_world))
    ]
    .groupby(['year', 'country'])[yaxis_co2_source].sum()
    .to_frame()
    .reset_index()
    .sort_values(by='year')
    .reset_index(drop=True)
)


# In[83]:


co2_source_bar_plot = co2_source_bar_pipeline.hvplot(kind="bar", x='country', y=yaxis_co2_source, title='CO2 source by continent')
co2_source_bar_plot


# ##### Creating Dashboard

# In[84]:


# Layout using Template
template = pn.template.FastListTemplate(
    title="World CO2 emission dashboard",
    sidebar=[pn.pane.Markdown("# CO2 Emission and Climate Change"),
             pn.pane.Markdown("##### Carbon dioxide emissions are the primary driver of global climate change. It's widely recognised that to avoid..."),
             # pn.pane.PNG('climate_day.png', sizing_mode='scale_both'),
             pn.pane.Markdown("## Settings"),
            year_slider],
    main=[pn.Row(pn.Column(yaxis_co2,
                          co2_plot.panel(width=700), margin=(0,25)),
                co2_table.panel(width=500)),
         pn.Row(pn.Column(co2_vs_gdp_scatterplot.panel(width=600), margin=(0,25)), 
                pn.Column(yaxis_co2_source, co2_source_bar_plot.panel(width=600)))],
    accent_base_color="#88d8b0",
    header_background="#88d8b0",
)
# template.show()
template.servable();

