# src/visualization_generator.py
import os
from badge_generator import DocumentationBadges


class ProjectDocumentation:
    def __init__(self):
        self.badges = DocumentationBadges()
        self.badges_config = self.badges.get_badges_config()

    def generate_visuals(self):
        """Generate all visualization files"""
        os.makedirs("docs/visuals", exist_ok=True)

        # Generate each visualization
        self.generate_pipeline_visual()
        self.generate_timeline_visual()
        self.generate_tech_stack_visual()
        self.generate_progress_tracker()
        self.generate_milestone_tracker()

    def generate_pipeline_visual(self):
        """Generate system architecture using Mermaid.js"""
        with open("docs/visuals/pipeline.html", "w") as f:
            f.write(
                """
    <!DOCTYPE html>
    <html>
    <head>
        <title>System Architecture</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 20px;
                background: #1a1a1a;
                color: white;
            }
            .mermaid { 
                background: #1a1a1a; 
                padding: 20px; 
                border-radius: 8px;
            }
            .title {
                color: white;
                text-align: center;
                font-size: 24px;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <h1 class="title">System Architecture</h1>
        <div class="mermaid">
        graph LR
            classDef source fill:#FF6B6B,stroke:#FF6B6B,stroke-width:4px,color:white,font-weight:bold
            classDef process fill:#4ECDC4,stroke:#4ECDC4,stroke-width:4px,color:white,font-weight:bold
            classDef storage fill:#45B7D1,stroke:#45B7D1,stroke-width:4px,color:white,font-weight:bold
            classDef output fill:#96CEB4,stroke:#96CEB4,stroke-width:4px,color:white,font-weight:bold

            %% First Line - Data Flow
            S[Weather API]:::source --> P[ETL Pipeline]:::process
            P --> D[Time Series DB]:::storage
            D --> A[Analysis Engine]:::process
            A --> M[ML Models]:::output

            %% Second Line - User Interface Flow
            U[Smart Meter]:::source --> E[Event Stream]:::process
            E --> C[Cache Layer]:::storage
            C --> O[Optimization]:::process
            O --> UI[Dashboard]:::output

            %% Vertical Connections
            S -.-> U
            P -.-> E
            D -.-> C
            A -.-> O
            M -.-> UI
        </div>
        <script>
            mermaid.initialize({ 
                startOnLoad: true,
                theme: 'dark',
                themeVariables: {
                    fontFamily: 'arial',
                    fontSize: '16px'
                }
            });
        </script>
    </body>
    </html>
    """
            )

    def generate_timeline_visual(self):
        """Generate project timeline using Mermaid.js"""
        with open("docs/visuals/timeline.html", "w") as f:
            f.write(
                """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Development Timeline</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 20px;
                background: #1a1a1a;
                color: white;
            }
            .mermaid { 
                background: #1a1a1a; 
                padding: 20px; 
                border-radius: 8px;
            }
            .title {
                color: white;
                text-align: center;
                font-size: 24px;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <h1 class="title">Development Timeline</h1>
        <div class="mermaid">
        gantt
            title Project Milestones
            dateFormat YYYY-MM-DD
            axisFormat %b-%Y
            
            section 1️⃣ Foundation
            Environment Setup     :crit, active, a1, 2024-11-04, 7d
            Data Pipeline        :crit, a2, after a1, 14d
            Storage Layer        :a3, after a2, 7d
            
            section 2️⃣ Core Analytics
            Pattern Detection    :crit, b1, after a3, 14d
            Time Series Analysis :b2, after b1, 14d
            ML Models Basic      :crit, b3, after b2, 14d
            
            section 3️⃣ Integration
            Advanced Pipeline    :crit, c1, after b3, 14d
            Model Deployment     :c2, after c1, 14d
            
            section 4️⃣ UI/Dashboard
            API Development      :crit, d1, after c2, 14d
            Dashboard           :crit, d2, after d1, 14d
            Documentation       :d3, after d2, 7d
        </div>
        <script>
            mermaid.initialize({ 
                startOnLoad: true,
                theme: 'dark',
                gantt: {
                    titleTopMargin: 25,
                    barHeight: 40,
                    barGap: 4,
                    topPadding: 50,
                    sidePadding: 50
                }
            });
        </script>
    </body>
    </html>
    """
            )

    def generate_tech_stack_visual(self):
        """Generate tech stack visualization using Mermaid.js"""
        with open("docs/visuals/tech_stack.html", "w") as f:
            f.write(
                """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Technical Stack</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 20px;
                background: #1a1a1a;
                color: white;
            }
            .mermaid { 
                background: #1a1a1a; 
                padding: 20px; 
                border-radius: 8px;
            }
            .title {
                color: white;
                text-align: center;
                font-size: 24px;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <h1 class="title">Technical Stack</h1>
        <div class="mermaid">
        mindmap
            root((Energy<br/>System))
                Data Pipeline
                    Weather API
                    Smart Meter Data
                    ETL Process
                Storage
                    SQLite
                    Time Series DB
                    Cache Layer
                Analytics
                    Pattern Detection
                    Forecasting
                    Optimization
                Interface
                    REST API
                    Dashboard
                    Alerts
        </div>
        <script>
            mermaid.initialize({ 
                startOnLoad: true,
                theme: 'dark'
            });
        </script>
    </body>
    </html>
    """
            )

    def generate_progress_tracker(self):
        """Generate progress tracking visualization"""
        with open("docs/visuals/progress.html", "w") as f:
            f.write(
                """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Project Progress</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 20px;
                background: #1a1a1a;
                color: white;
            }
            .mermaid { 
                background: #1a1a1a; 
                padding: 20px; 
                border-radius: 8px;
            }
            .title {
                color: white;
                text-align: center;
                font-size: 24px;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <h1 class="title">Project Progress</h1>
        <div class="mermaid">
        journey
            title Development Progress
            section Foundation
            Setup Dev Environment: 5: done
            Weather API Integration: 4: done
            Data Pipeline: 3: in-progress
            Storage Implementation: 2: pending
            section Analytics
            Pattern Detection: 1: pending
            Time Series Processing: 1: pending
            Basic ML Models: 1: pending
            section Integration
            Advanced Pipeline: 1: pending
            Model Deployment: 1: pending
            section UI
            API Layer: 1: pending
            Dashboard: 1: pending
            Documentation: 1: pending
        </div>
        <script>
            mermaid.initialize({ 
                startOnLoad: true,
                theme: 'dark'
            });
        </script>
    </body>
    </html>
    """
            )

    def generate_milestone_tracker(self):
        """Generate milestone tracking visualization"""
        with open("docs/visuals/milestones.html", "w") as f:
            f.write(
                """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Project Milestones</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 20px;
                background: #1a1a1a;
                color: white;
            }
            .mermaid { 
                background: #1a1a1a; 
                padding: 20px; 
                border-radius: 8px;
            }
            .title {
                color: white;
                text-align: center;
                font-size: 24px;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <h1 class="title">Project Milestones</h1>
        <div class="mermaid">
        graph TD
            classDef milestone fill:#FF6B6B,stroke:#FF6B6B,stroke-width:4px,color:white,font-weight:bold
            classDef completed fill:#4ECDC4,stroke:#4ECDC4,stroke-width:4px,color:white,font-weight:bold
            classDef inprogress fill:#45B7D1,stroke:#45B7D1,stroke-width:4px,color:white,font-weight:bold
            classDef pending fill:#96CEB4,stroke:#96CEB4,stroke-width:4px,color:white,font-weight:bold

            M1[Milestone 1: Foundation]:::milestone --> |Completed| T1[Environment Setup]:::completed
            M1 --> |In Progress| T2[Data Pipeline]:::inprogress
            M1 --> |Pending| T3[Storage Layer]:::pending

            M2[Milestone 2: Analytics]:::milestone --> T4[Pattern Detection]:::pending
            M2 --> T5[Time Series Analysis]:::pending
            M2 --> T6[ML Models]:::pending

            M3[Milestone 3: Integration]:::milestone --> T7[API Development]:::pending
            M3 --> T8[Model Deployment]:::pending
            M3 --> T9[Testing]:::pending

            M4[Milestone 4: UI/Dashboard]:::milestone --> T10[Frontend]:::pending
            M4 --> T11[Documentation]:::pending
            M4 --> T12[Deployment]:::pending

            linkStyle default stroke:#666,stroke-width:2px
        </div>
        <script>
            mermaid.initialize({ 
                startOnLoad: true,
                theme: 'dark'
            });
        </script>
    </body>
    </html>
    """
            )

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
                background-color: #1a1a1a;
                color: white;
            }}
            .nav-menu {{
                background: #333;
                padding: 1rem;
                border-radius: 8px;
                margin-bottom: 2rem;
                position: sticky;
                top: 0;
                z-index: 1000;
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
            }}
            .nav-menu a {{
                color: white;
                text-decoration: none;
                padding: 0.5rem 1rem;
                border-radius: 4px;
                transition: background 0.3s;
            }}
            .nav-menu a:hover {{
                background: #45B7D1;
            }}
            .visual-container {{
                background: #2d2d2d;
                border-radius: 8px;
                padding: 20px;
                margin: 20px 0;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            }}
            .badge-container {{
                margin: 10px 0;
                padding: 5px;
                background: #333;
                border-radius: 4px;
                display: inline-block;
            }}
            .section-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1rem;
                border-bottom: 2px solid #45B7D1;
                padding-bottom: 0.5rem;
            }}
            .view-full-page {{
                background: #45B7D1;
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 4px;
                text-decoration: none;
                font-size: 0.9rem;
                transition: background 0.3s;
            }}
            .view-full-page:hover {{
                background: #FF6B6B;
            }}
            iframe {{
                border: none;
                width: 100%;
                height: 600px;
                border-radius: 4px;
                background: #1a1a1a;
            }}
            .metrics {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1rem;
                margin: 1rem 0;
            }}
            .metric-card {{
                background: #333;
                padding: 1rem;
                border-radius: 4px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="nav-menu">
            <a href="#overview">Overview</a>
            <a href="#pipeline">Architecture</a>
            <a href="#timeline">Timeline</a>
            <a href="#tech-stack">Tech Stack</a>
            <a href="#progress">Progress</a>
            <a href="#milestones">Milestones</a>
            <a href="https://github.com/ngnnah/energy-optimization" target="_blank">GitHub</a>
        </div>

        <h1 id="overview">Smart Home Energy Optimization System</h1>
        <div class="badge-container">
            {self.badges.generate_badge_html("index", 
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

        <div class="visual-container" id="progress">
            <div class="section-header">
                <h2>Project Progress</h2>
                <a href="visuals/progress.html" class="view-full-page" target="_blank">View Full Page</a>
            </div>
            <div class="badge-container">
                {self.badges.generate_badge_html("visuals/progress",
                                            self.badges_config["visuals/progress"]["color"],
                                            self.badges_config["visuals/progress"]["title"])}
            </div>
            <iframe src="visuals/progress.html"></iframe>
        </div>

        <div class="visual-container" id="milestones">
            <div class="section-header">
                <h2>Project Milestones</h2>
                <a href="visuals/milestones.html" class="view-full-page" target="_blank">View Full Page</a>
            </div>
            <div class="badge-container">
                {self.badges.generate_badge_html("visuals/milestones",
                                            self.badges_config["visuals/milestones"]["color"],
                                            self.badges_config["visuals/milestones"]["title"])}
            </div>
            <iframe src="visuals/milestones.html"></iframe>
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
