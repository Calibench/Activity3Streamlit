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

# Display the filtered data as a table
st.write('Filtered Data:')
st.write(filtered_data)

# Create a bar chart using matplotlib and display it using Streamlit
fig, ax = plt.subplots()
years = [column for column in filtered_data.columns if 'Y' in column]
temperatures = filtered_data[years].mean().values # assuming that we take the average temperature if an area appears multiple times
ax.plot(years, temperatures)
ax.set_xlabel('Year')
ax.set_ylabel('Temperature')
ax.set_title(f'{selected_area} - Average Temperature Over the Years')
st.pyplot(fig)
