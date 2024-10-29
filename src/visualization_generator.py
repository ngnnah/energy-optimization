# visualization_generator.py
class ProjectDocumentation:
    def __init__(self):
        self.TEMPLATE_PATH = "templates"
        self.OUTPUT_PATH = "docs"
        self.VISUALS_PATH = "visuals"

    def generate_documentation(self):
        # Generate visualizations
        self.generate_visuals()
        # Generate documentation
        self.create_markdown_docs()
        # Generate index.html
        self.create_html_index()

    def generate_visuals(self):
        """Generate all interactive plotly visualizations as static HTML"""
        visuals = {
            "pipeline": self.create_pipeline_visual(),
            "timeline": self.create_timeline_visual(),
            "tech_stack": self.create_tech_stack_visual(),
        }

        for name, fig in visuals.items():
            fig.write_html(
                f"{self.VISUALS_PATH}/{name}.html",
                include_plotlyjs="cdn",
                full_html=False,
            )

    def create_markdown_docs(self):
        """Create markdown documentation with embedded visuals"""
        readme_content = """
# Smart Home Energy Optimization System

## Project Overview
An end-to-end data engineering pipeline for optimizing home energy consumption through real-time monitoring, analysis, and ML-powered recommendations.

## System Architecture
<details>
<summary>View Pipeline Diagram</summary>
<iframe src="visuals/pipeline.html" width="100%" height="600px" frameborder="0"></iframe>
</details>

## Development Timeline
<details>
<summary>View Project Timeline</summary>
<iframe src="visuals/timeline.html" width="100%" height="400px" frameborder="0"></iframe>
</details>

## Technical Stack
<details>
<summary>View Tech Stack</summary>
<iframe src="visuals/tech_stack.html" width="100%" height="500px" frameborder="0"></iframe>
</details>

## Implementation Guide

### Weekly Development Process
1. **Hour 1: Development**
   - Code implementation
   - Testing
   - Integration

2. **Hour 2: Review & Planning**
   - Documentation
   - Code review
   - Next steps planning

### Project Phases
1. **Foundation** (Weeks 1-4)
   - Environment setup
   - Data pipeline creation
   - Storage layer implementation

2. **Core Analytics** (Weeks 5-8)
   - Pattern detection
   - Time series processing
   - Basic ML models

3. **ML Integration** (Weeks 9-12)
   - Advanced ML pipeline
   - Optimization rules
   - Model deployment

4. **UI/Dashboard** (Weeks 13-16)
   - Dashboard development
   - Interactive features
   - Documentation & launch
"""
        with open(f"{self.OUTPUT_PATH}/README.md", "w") as f:
            f.write(readme_content)

    def create_html_index(self):
        """Create an HTML index page with embedded visualizations"""
        html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart Home Energy Optimization System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8fafc;
        }
        .visual-container {
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        .tab {
            padding: 10px 20px;
            background: #e2e8f0;
            border-radius: 4px;
            cursor: pointer;
        }
        .tab.active {
            background: #0ea5e9;
            color: white;
        }
        iframe {
            border: none;
            width: 100%;
            height: 600px;
        }
    </style>
</head>
<body>
    <h1>Smart Home Energy Optimization System</h1>
    
    <div class="visual-container">
        <h2>System Architecture</h2>
        <iframe src="visuals/pipeline.html"></iframe>
    </div>

    <div class="visual-container">
        <h2>Development Timeline</h2>
        <iframe src="visuals/timeline.html"></iframe>
    </div>

    <div class="visual-container">
        <h2>Technical Stack</h2>
        <iframe src="visuals/tech_stack.html"></iframe>
    </div>

    <script>
        // Add any interactive features
        document.addEventListener('DOMContentLoaded', function() {
            // Resize iframes based on content
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => {
                iframe.onload = function() {
                    iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
                }
            });
        });
    </script>
</body>
</html>
"""
        with open(f"{self.OUTPUT_PATH}/index.html", "w") as f:
            f.write(html_content)


# Project structure
"""
project/
├── src/
│   ├── visualization_generator.py
│   └── visualizations/
│       ├── pipeline.py
│       ├── timeline.py
│       └── tech_stack.py
├── docs/
│   ├── README.md
│   ├── index.html
│   └── visuals/
│       ├── pipeline.html
│       ├── timeline.html
│       └── tech_stack.html
├── templates/
│   └── base.html
└── README.md
"""

# Usage
if __name__ == "__main__":
    doc_generator = ProjectDocumentation()
    doc_generator.generate_documentation()
