import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('Environment_Temperature_change_E_All_Data_NOFLAG.csv', encoding='ISO-8859-1')

# Add a title to the app
st.title('Interactive Temperature Dashboard')

# Create a dropdown for area selection
selected_area = st.selectbox('Select an Area', df['Area'].unique())

# Filter the dataset based on user selections
filtered_data = df[df['Area'] == selected_area]

# Get year columns
year_columns = [col for col in df.columns if 'Y' in col]

# Create a new dataframe with only the year columns
yearly_data = filtered_data[year_columns].T

# Create the line chart using matplotlib and display it using Streamlit
fig, ax = plt.subplots()
ax.plot(yearly_data.index, yearly_data[selected_area])
ax.set_xlabel('Year')
ax.set_ylabel('Temperature')
ax.set_title(f'Temperature Changes in {selected_area} Over the Years')
plt.xticks([])  # Hide x-axis labels
st.pyplot(fig)
