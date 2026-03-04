import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.title("Interactive Data Visualization with Plotly")

# -----------------------------
# Dataset
# -----------------------------
data = {
    "year":[2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
    "avg_solve_time":[28,22,18,20,24,30,34,38,42,44,45],
    "best_solve_time":[18,16,14,15,17,19,21,23,25,27,28],
    "practice_hours":[400,350,300,200,120,80,60,40,25,15,10],
    "solves_per_year":[2000,1800,1500,1200,900,700,600,500,400,250,150],
    "sleep_hours":[8,8,7.5,7,7,6.5,6,6,6,5.5,5],
    "stress_level":[2,3,3,4,5,6,7,7,8,8,9],
    "caffeine_mg":[50,60,80,120,150,200,220,240,260,280,300],
    "social_media_hours":[0,0,0.5,2,3,3.5,4,4.5,5,5.5,6]
}

df = pd.DataFrame(data)

# -----------------------------
# Sidebar Menu
# -----------------------------
chart_type = st.sidebar.selectbox(
    "Select Visualization",
    [
        "Dataset",
        "Line Chart",
        "Scatter Plot",
        "Bar Chart",
        "Histogram Comparison",
        "Box Plot",
        "Bubble Chart",
        "Correlation Heatmap",
        "Scatter Matrix",
        "3D Scatter Plot"
    ]
)

# -----------------------------
# Dataset
# -----------------------------
if chart_type == "Dataset":

    st.subheader("Rubik's Cube Performance Dataset")
    st.dataframe(df)

# -----------------------------
# Line Chart
# -----------------------------
elif chart_type == "Line Chart":

    fig = px.line(
        df,
        x="year",
        y=["avg_solve_time","best_solve_time"],
        markers=True,
        color_discrete_sequence=["#1f77b4","#e74c3c"],
        title="Rubik's Cube Performance Over Time"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

    if st.checkbox("Show Code"):
        st.code("""
fig = px.line(df, x="year", y=["avg_solve_time","best_solve_time"], markers=True)
fig.show()
""", language="python")

# -----------------------------
# Scatter Plot
# -----------------------------
elif chart_type == "Scatter Plot":

    fig = px.scatter(
        df,
        x="practice_hours",
        y="avg_solve_time",
        color="stress_level",
        color_continuous_scale="Viridis",
        title="Practice Hours vs Solve Time"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Bar Chart
# -----------------------------
elif chart_type == "Bar Chart":

    fig = px.bar(
        df,
        x="year",
        y="practice_hours",
        color="practice_hours",
        color_continuous_scale="Greens",
        title="Practice Hours Per Year"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Histogram Comparison
# -----------------------------
elif chart_type == "Histogram Comparison":

    early_years = df.avg_solve_time[df.year <= 2017]
    later_years = df.avg_solve_time[df.year >= 2018]

    trace1 = go.Histogram(
        x=early_years,
        opacity=0.75,
        name="Before Smartphone",
        marker=dict(color='rgba(231,76,60,0.7)')
    )

    trace2 = go.Histogram(
        x=later_years,
        opacity=0.75,
        name="After Smartphone",
        marker=dict(color='rgba(52,152,219,0.7)')
    )

    fig = go.Figure(data=[trace1, trace2])

    fig.update_layout(
        barmode='overlay',
        template="plotly_white",
        title="Solve Time Distribution Before vs After Smartphone",
        xaxis_title="Solve Time (seconds)",
        yaxis_title="Count"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Box Plot
# -----------------------------
elif chart_type == "Box Plot":

    fig = px.box(
        df,
        y="avg_solve_time",
        points="all",
        color_discrete_sequence=["#8e44ad"],
        title="Solve Time Distribution"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Bubble Chart
# -----------------------------
elif chart_type == "Bubble Chart":

    fig = px.scatter(
        df,
        x="practice_hours",
        y="avg_solve_time",
        size="solves_per_year",
        color="year",
        size_max=60,
        title="Practice vs Performance (Bubble Chart)"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Correlation Heatmap
# -----------------------------
elif chart_type == "Correlation Heatmap":

    corr = df.corr()

    fig = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        colorscale="RdBu",
        zmin=-1,
        zmax=1,
        text=np.round(corr.values,2),
        texttemplate="%{text}"
    ))

    fig.update_layout(
        title="Correlation Between Lifestyle Factors and Performance",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Scatter Matrix
# -----------------------------
elif chart_type == "Scatter Matrix":

    fig = px.scatter_matrix(
        df,
        dimensions=[
            "avg_solve_time",
            "practice_hours",
            "stress_level",
            "sleep_hours",
            "social_media_hours"
        ],
        color="stress_level",
        color_continuous_scale="Viridis"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 3D Scatter Plot
# -----------------------------
elif chart_type == "3D Scatter Plot":

    fig = go.Figure(data=[go.Scatter3d(
        x=df["practice_hours"],
        y=df["avg_solve_time"],
        z=df["stress_level"],
        mode='markers',
        marker=dict(
            size=8,
            color=df["social_media_hours"],
            colorscale='Viridis',
            opacity=0.8
        )
    )])

    fig.update_layout(
        title="3D Visualization of Performance Factors",
        scene=dict(
            xaxis_title="Practice Hours",
            yaxis_title="Average Solve Time",
            zaxis_title="Stress Level"
        ),
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

    if st.checkbox("Show Code"):
        st.code("""
fig = go.Figure(data=[go.Scatter3d(
    x=df["practice_hours"],
    y=df["avg_solve_time"],
    z=df["stress_level"],
    mode='markers'
)])
fig.show()
""", language="python")
