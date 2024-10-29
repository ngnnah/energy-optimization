# src/visualizations/timeline.py
import plotly.express as px
import pandas as pd


def create_timeline_visual():
    # Timeline visualization code here
    df = pd.DataFrame(
        [
            dict(
                Task="Foundation", Start="2024-11-04", End="2024-11-17", Phase="Phase 1"
            ),
            # Add more tasks
        ]
    )

    fig = px.timeline(df, x_start="Start", x_end="End", y="Task", color="Phase")
    return fig
