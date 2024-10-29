# src/visualization_generator.py
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
import pandas as pd
import os
from badge_generator import DocumentationBadges


class ProjectDocumentation:
    def __init__(self):
        self.badges = DocumentationBadges()
        self.badges_config = self.badges.get_badges_config()

    def generate_visuals(self):
        """Generate all visualization files"""
        os.makedirs("docs/visuals", exist_ok=True)

        self.generate_pipeline_visual()
        self.generate_timeline_visual()
        self.generate_tech_stack_visual()

    def generate_pipeline_visual(self):
        """Generate pipeline architecture visualization"""
        nodes = [
            "Data Sources",
            "ETL Pipeline",
            "Storage",
            "Analysis",
            "ML Models",
            "API",
            "Dashboard",
        ]
        edges = [(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]

        G = nx.DiGraph()
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)

        edge_trace = go.Scatter(
            x=[], y=[], line=dict(width=2, color="#888"), hoverinfo="none", mode="lines"
        )

        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_trace["x"] += (x0, x1, None)
            edge_trace["y"] += (y0, y1, None)

        node_trace = go.Scatter(
            x=[pos[node][0] for node in G.nodes()],
            y=[pos[node][1] for node in G.nodes()],
            text=list(G.nodes()),
            mode="markers+text",
            hoverinfo="text",
            marker=dict(size=20, color="#0EA5E9"),
            textposition="bottom center",
        )

        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                showlegend=False,
                hovermode="closest",
                margin=dict(b=20, l=5, r=5, t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            ),
        )

        fig.write_html("docs/visuals/pipeline.html")

    def generate_timeline_visual(self):
        """Generate project timeline visualization"""
        df = pd.DataFrame(
            [
                dict(
                    Task="Foundation",
                    Start="2024-11-04",
                    End="2024-11-17",
                    Phase="Phase 1",
                ),
                dict(
                    Task="Data Pipeline",
                    Start="2024-11-18",
                    End="2024-12-01",
                    Phase="Phase 1",
                ),
                dict(
                    Task="Core Analytics",
                    Start="2024-12-02",
                    End="2024-12-29",
                    Phase="Phase 2",
                ),
                dict(
                    Task="ML Integration",
                    Start="2024-01-13",
                    End="2024-02-09",
                    Phase="Phase 3",
                ),
                dict(
                    Task="UI/Dashboard",
                    Start="2024-02-24",
                    End="2024-03-16",
                    Phase="Phase 4",
                ),
            ]
        )

        fig = px.timeline(df, x_start="Start", x_end="End", y="Task", color="Phase")
        fig.update_layout(
            title="Project Timeline", xaxis_title="Date", yaxis_title="Task"
        )

        fig.write_html("docs/visuals/timeline.html")

    def generate_tech_stack_visual(self):
        """Generate technical stack visualization"""
        tech_data = {
            "Category": [
                "Data Collection",
                "Data Collection",
                "Storage",
                "Storage",
                "Analysis",
                "Analysis",
                "UI",
                "UI",
            ],
            "Tool": [
                "Python Requests",
                "Weather API",
                "SQLite",
                "Pandas",
                "Scikit-learn",
                "Prophet",
                "Streamlit",
                "Plotly",
            ],
            "Value": [1, 1, 1, 1, 1, 1, 1, 1],
        }
        df = pd.DataFrame(tech_data)

        fig = px.treemap(df, path=["Category", "Tool"], values="Value")

        fig.update_layout(title="Technical Stack Components")

        fig.write_html("docs/visuals/tech_stack.html")

    def create_html_index(self):
        """Create main index.html with all visualizations and tracking"""
        html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart Home Energy Optimization System</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f8fafc;
            }}
            .nav-menu {{
                background: #1e293b;
                padding: 1rem;
                border-radius: 8px;
                margin-bottom: 2rem;
                position: sticky;
                top: 0;
                z-index: 1000;
            }}
            .nav-menu a {{
                color: white;
                text-decoration: none;
                padding: 0.5rem 1rem;
                margin: 0 0.5rem;
                border-radius: 4px;
                transition: background 0.3s;
            }}
            .nav-menu a:hover {{
                background: #334155;
            }}
            .visual-container {{
                background: white;
                border-radius: 8px;
                padding: 20px;
                margin: 20px 0;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}
            .badge-container {{
                margin: 10px 0;
                padding: 5px;
                background: #f1f5f9;
                border-radius: 4px;
                display: inline-block;
            }}
            .section-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1rem;
            }}
            .view-full-page {{
                background: #0ea5e9;
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 4px;
                text-decoration: none;
                font-size: 0.9rem;
                transition: background 0.3s;
            }}
            .view-full-page:hover {{
                background: #0284c7;
            }}
            iframe {{
                border: none;
                width: 100%;
                height: 600px;
                border-radius: 4px;
            }}
            .metrics {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1rem;
                margin: 1rem 0;
            }}
            .metric-card {{
                background: white;
                padding: 1rem;
                border-radius: 4px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div class="nav-menu">
            <a href="#overview">Overview</a>
            <a href="#pipeline">Pipeline</a>
            <a href="#timeline">Timeline</a>
            <a href="#tech-stack">Tech Stack</a>
            <a href="https://github.com/ngnnah/energy-optimization" target="_blank">GitHub</a>
        </div>

        <h1 id="overview">Smart Home Energy Optimization System</h1>
        <div class="badge-container">
            {self.badges.generate_badge_html("", 
                                        self.badges_config["index"]["color"],
                                        self.badges_config["index"]["title"])}
        </div>

        <div class="metrics">
            <div class="metric-card">
                <h3>Development Time</h3>
                <p>16 weeks</p>
            </div>
            <div class="metric-card">
                <h3>Core Components</h3>
                <p>4 modules</p>
            </div>
            <div class="metric-card">
                <h3>Data Sources</h3>
                <p>3 integrations</p>
            </div>
        </div>
        
        <div class="visual-container" id="pipeline">
            <div class="section-header">
                <h2>System Architecture</h2>
                <a href="visuals/pipeline.html" class="view-full-page" target="_blank">View Full Page</a>
            </div>
            <div class="badge-container">
                {self.badges.generate_badge_html("visuals/pipeline",
                                            self.badges_config["visuals/pipeline"]["color"],
                                            self.badges_config["visuals/pipeline"]["title"])}
            </div>
            <iframe src="visuals/pipeline.html"></iframe>
        </div>

        <div class="visual-container" id="timeline">
            <div class="section-header">
                <h2>Development Timeline</h2>
                <a href="visuals/timeline.html" class="view-full-page" target="_blank">View Full Page</a>
            </div>
            <div class="badge-container">
                {self.badges.generate_badge_html("visuals/timeline",
                                            self.badges_config["visuals/timeline"]["color"],
                                            self.badges_config["visuals/timeline"]["title"])}
            </div>
            <iframe src="visuals/timeline.html"></iframe>
        </div>

        <div class="visual-container" id="tech-stack">
            <div class="section-header">
                <h2>Technical Stack</h2>
                <a href="visuals/tech_stack.html" class="view-full-page" target="_blank">View Full Page</a>
            </div>
            <div class="badge-container">
                {self.badges.generate_badge_html("visuals/tech_stack",
                                            self.badges_config["visuals/tech_stack"]["color"],
                                            self.badges_config["visuals/tech_stack"]["title"])}
            </div>
            <iframe src="visuals/tech_stack.html"></iframe>
        </div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                // Smooth scrolling for navigation
                document.querySelectorAll('.nav-menu a[href^="#"]').forEach(anchor => {{
                    anchor.addEventListener('click', function (e) {{
                        e.preventDefault();
                        document.querySelector(this.getAttribute('href')).scrollIntoView({{
                            behavior: 'smooth'
                        }});
                    }});
                }});

                // Iframe height adjustment
                var iframes = document.querySelectorAll('iframe');
                for (var i = 0; i < iframes.length; i++) {{
                    iframes[i].onload = function() {{
                        this.style.height = this.contentWindow.document.body.scrollHeight + 'px';
                    }};
                }}
            }});
        </script>
    </body>
    </html>
    """
        with open("docs/index.html", "w") as f:
            f.write(html_content)

    def create_markdown_docs(self):
        """Create markdown documentation with tracking badges"""
        # Get badge configurations
        index_badge = self.badges.generate_badge_markdown(
            "index",
            self.badges_config["index"]["color"],
            self.badges_config["index"]["title"],
        )

        pipeline_badge = self.badges.generate_badge_markdown(
            "visuals/pipeline",
            self.badges_config["visuals/pipeline"]["color"],
            self.badges_config["visuals/pipeline"]["title"],
        )

        timeline_badge = self.badges.generate_badge_markdown(
            "visuals/timeline",
            self.badges_config["visuals/timeline"]["color"],
            self.badges_config["visuals/timeline"]["title"],
        )

        tech_stack_badge = self.badges.generate_badge_markdown(
            "visuals/tech_stack",
            self.badges_config["visuals/tech_stack"]["color"],
            self.badges_config["visuals/tech_stack"]["title"],
        )

        # Create documentation content
        readme_content = f"""
    # Smart Home Energy Optimization System

    {index_badge}

    ## Project Overview
    An end-to-end data engineering pipeline for optimizing home energy consumption.

    ## System Architecture
    {pipeline_badge}
    <details>
    <summary>View Pipeline Diagram</summary>
    <iframe src="visuals/pipeline.html" width="100%" height="600px" frameborder="0"></iframe>
    </details>

    ## Development Timeline
    {timeline_badge}
    <details>
    <summary>View Project Timeline</summary>
    <iframe src="visuals/timeline.html" width="100%" height="400px" frameborder="0"></iframe>
    </details>

    ## Technical Stack
    {tech_stack_badge}
    <details>
    <summary>View Tech Stack</summary>
    <iframe src="visuals/tech_stack.html" width="100%" height="500px" frameborder="0"></iframe>
    </details>
    """
        with open("docs/README.md", "w") as f:
            f.write(readme_content)

    def generate_documentation(self):
        """Generate all documentation files"""
        self.generate_visuals()
        self.create_html_index()
        self.create_markdown_docs()

        # Create .nojekyll file for GitHub Pages
        with open("docs/.nojekyll", "w") as f:
            pass


# Usage
if __name__ == "__main__":
    doc_generator = ProjectDocumentation()
    doc_generator.generate_documentation()
