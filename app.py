import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load GTFS data (adjust these paths if necessary)
routes = pd.read_csv('routes.txt')
trips = pd.read_csv('trips.txt')
stop_times = pd.read_csv('stop_times.txt')
stops = pd.read_csv('stops.txt')
calendar_dates = pd.read_csv('calendar_dates.txt')

# --- Sidebar ---
st.sidebar.title('Filters')

# Date selection
date_selected = st.sidebar.date_input('Select a date')
date_selected_str = date_selected.strftime('%Y%m%d')

# Prepare calendar exceptions
service_exceptions = calendar_dates[calendar_dates['date'] == int(date_selected_str)]

# Service IDs active today
added_services = service_exceptions[service_exceptions['exception_type'] == 1]['service_id'].unique()
canceled_services = service_exceptions[service_exceptions['exception_type'] == 2]['service_id'].unique()

# Trips available today
available_trips = trips[trips['service_id'].isin(added_services)]

# Route filter
available_route_ids = available_trips['route_id'].unique()
available_routes = routes[routes['route_id'].isin(available_route_ids)]
selected_route = st.sidebar.selectbox('Select a route', available_routes['route_id'].tolist())

# Trip filter
route_trips = available_trips[available_trips['route_id'] == selected_route]
selected_trip = st.sidebar.selectbox('Select a trip', route_trips['trip_id'].tolist())

# --- Main KPIs ---
st.title('Transit Operating Dashboard')

col1, col2, col3 = st.columns(3)
col1.metric("Total Trips Today", len(available_trips))
col2.metric("Active Routes", len(available_routes))
col3.metric("Added Trips", len(added_services))

# --- Scheduled Trips List ---
st.subheader('Scheduled Trips for Selected Date')
st.dataframe(route_trips[['trip_id', 'trip_headsign']])

# --- Stop Sequence Viewer ---
st.subheader('Stop Sequence for Selected Trip')
trip_stops = stop_times[stop_times['trip_id'] == selected_trip].sort_values('stop_sequence')
trip_stops = trip_stops.merge(stops, on='stop_id')
st.dataframe(trip_stops[['stop_sequence', 'stop_name', 'arrival_time', 'departure_time']])

# --- Map the stops ---
st.subheader('Stop Map for Selected Trip')
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(trip_stops['stop_lon'], trip_stops['stop_lat'])
for i, row in trip_stops.iterrows():
    ax.annotate(row['stop_name'], (row['stop_lon'], row['stop_lat']), fontsize=8)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Stop Locations')
st.pyplot(fig)

# --- Notes ---
st.caption('Note: Only added services shown today. If no services were added on this day, no trips will appear.')
