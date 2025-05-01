# GTFS Schedule Dashboard (GO Transit Focused Project) 🚍📊

This interactive dashboard was created as a **self-initiated project** to explore how GTFS (General Transit Feed Specification) data from **GO Transit** can support **transit scheduling**, **operational monitoring**, and **short-term planning** — key responsibilities for roles like the Junior Analyst (Operations Performance) at Metrolinx.

It uses official GTFS schedule data published by **Metrolinx** for GO Transit and was built with **Streamlit**, allowing instant filtering and visualization of routes, trips, stops, and key service metrics.

---

## 🎯 Purpose

This project was built to:

- Demonstrate my ability to work with GTFS schedule data
- Analyze operational transit patterns
- Practice technical tasks such as trip segmentation, calendar exception handling, and route filtering
- Simulate responsibilities relevant to schedule updates, GTFS feed maintenance, and short-term transit planning

---

## 🔍 Features

- Filter GO Transit services by **date**, **route**, and **trip**
- View stop sequences, arrival/departure times, and route-level summaries
- Map stop locations using latitude/longitude
- Visualize KPIs:
  - Total trips for a selected day
  - Active routes
  - Number of added/canceled services

---

## 📦 Tools Used

- [Streamlit](https://streamlit.io/) – Interactive Python dashboard framework
- [Pandas](https://pandas.pydata.org/) – Data wrangling and analysis
- [Matplotlib](https://matplotlib.org/) – Visualizations
- [GTFS Format](https://gtfs.org/) – Transit data standard

---

## 📁 Folder Overview

```
gtfs_dashboard_project/
├── app.py                 # Main Streamlit app
├── requirements.txt       # For Streamlit Cloud deployment
├── routes.txt             # GTFS files
├── trips.txt
├── stops.txt
├── stop_times.txt
├── calendar_dates.txt
└── ...
```

---

## 🚀 Live App

🔗 [Click here to view the live GTFS Schedule Dashboard](https://go-gtfs-schedule-dashboard-bwwij7emkatezpytldm9es.streamlit.app/)

Hosted on **Streamlit Cloud**.

---

## 📊 Data Source

This dashboard uses publicly available GTFS static schedule data from:

🔗 [Metrolinx Open Data Portal](https://www.metrolinx.com/en/about-us/open-data)  
→ **The General Transit Feed Specification (GTFS) – GO Transit**

This data includes schedule, route, stop, and service calendar information, made available for public use under Metrolinx's open data initiative.

---

## 🤖 AI-Assisted Development

This project was developed with significant assistance from **ChatGPT (OpenAI)**.  
Most of the Python and Streamlit code, as well as GTFS parsing logic and deployment guidance, was generated through interactive prompts and iterative refinement using ChatGPT.  

All final decisions, data interpretation, and structural choices were made by the author.

---

## 🧑‍💻 About Me

**Sanuja Senadeera**  
Toronto-based Business/Data Analyst passionate about public transit, operational analysis, and using data to improve system performance.

This project was designed as a technical case study to support my application for the **Junior Analyst, Operations Performance Management** role at Metrolinx.

📫 [LinkedIn](https://linkedin.com/in/sanujasenadeera) | [GitHub](https://github.com/sanujav18)

---

## 📄 License

This project is open-source under the MIT License.
