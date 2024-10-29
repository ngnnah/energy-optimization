# src/visualizations/tech_stack.py
import plotly.express as px
import pandas as pd


def create_tech_stack_visual():
    # Tech stack visualization code here
    tech_data = {
        "Category": ["Data Collection", "Storage", "Analysis", "UI"],
        "Tool": ["Python", "SQLite", "ML Models", "Dashboard"],
        "Value": [1, 1, 1, 1],
    }
    df = pd.DataFrame(tech_data)

    fig = px.treemap(df, path=["Category", "Tool"], values="Value")
    return fig
