from generate_dashboard import generate_project_dashboard


# src/generate_mermaid_diagrams.py
class MermaidDiagrams:
    def __init__(self):
        self.diagrams = {}
        self.generate_all_diagrams()

    def generate_all_diagrams(self):
        self.diagrams["system_architecture"] = self.generate_system_architecture()
        self.diagrams["implementation_roadmap"] = self.generate_implementation_roadmap()
        self.diagrams["development_phases"] = self.generate_development_phases()
        self.diagrams["tech_stack"] = self.generate_tech_stack()

    def generate_system_architecture(self):
        return """
```mermaid
graph LR
    %% Styling
    classDef source fill:#FF6B6B,stroke:#FF6B6B,stroke-width:2px,color:white,font-weight:bold
    classDef process fill:#4ECDC4,stroke:#4ECDC4,stroke-width:2px,color:white,font-weight:bold
    classDef storage fill:#45B7D1,stroke:#45B7D1,stroke-width:2px,color:white,font-weight:bold
    classDef ml fill:#A78BFA,stroke:#A78BFA,stroke-width:2px,color:white,font-weight:bold
    classDef output fill:#10B981,stroke:#10B981,stroke-width:2px,color:white,font-weight:bold

    %% Data Sources
    DS[Data Sources]:::source --> ETL[ETL Pipeline]:::process
    WA[Weather API]:::source --> ETL
    SM[Smart Meter]:::source --> ETL

    %% Processing Layer
    ETL --> TS[Time Series DB]:::storage
    ETL --> Cache[Cache Layer]:::storage

    %% Analysis Layer
    TS --> PD[Pattern Detection]:::ml
    Cache --> RT[Real-time Analysis]:::ml
    PD --> ML[ML Models]:::ml
    RT --> ML

    %% Output Layer
    ML --> API[REST API]:::output
    API --> DASH[Dashboard]:::output
    API --> OPT[Optimization Engine]:::output
```
"""

    def generate_implementation_roadmap(self):
        return """
```mermaid
graph TD
    classDef phase fill:#FF6B6B,stroke:#FF6B6B,stroke-width:4px,color:white,font-weight:bold,font-size:18px
    classDef module fill:#4ECDC4,stroke:#4ECDC4,stroke-width:4px,color:white,font-weight:bold,font-size:16px

    %% Top Row - Scale nodes with more content
    F[🚀 Foundation<br/>Module]:::phase --> |Data Flow| A[🧠 Analytics<br/>Module]:::phase
    
    %% Bottom Row
    I[⚡ Integration<br/>Module]:::phase --> |User Flow| U[📊 UI/Dashboard<br/>Module]:::phase
    
    %% Vertical Connections with descriptive labels
    F --> |Processing| I
    A --> |Results| U
    
    %% Components in each module with emojis and detailed text
    F --> F1[🔄 ETL Pipeline<br/>Data Storage<br/>API Integration]:::module
    A --> A1[📈 ML Models<br/>Time Series<br/>Predictions]:::module
    I --> I1[🔌 API Layer<br/>Testing<br/>Deployment]:::module
    U --> U1[💫 Dashboard<br/>Monitoring<br/>Alerts]:::module

    %% Style overrides for better visibility
    style F fill:#FF61D2,stroke:#FF61D2,color:#fff
    style A fill:#4D96FF,stroke:#4D96FF,color:#fff
    style I fill:#6C4AB6,stroke:#6C4AB6,color:#fff
    style U fill:#00D7FF,stroke:#00D7FF,color:#fff
    
    %% Module styling
    style F1 fill:#FF92E3,stroke:#FF92E3,color:#fff
    style A1 fill:#72AAFF,stroke:#72AAFF,color:#fff
    style I1 fill:#8B6AD6,stroke:#8B6AD6,color:#fff
    style U1 fill:#45E3FF,stroke:#45E3FF,color:#fff

    %% Link styling
    linkStyle 0,1,2,3,4,5,6,7 stroke-width:3px,fill:none,stroke:#FFB6C1
```
"""

    def generate_development_phases(self):
        return """
```mermaid
graph TB
    %% Styling
    classDef phase fill:#8B5CF6,stroke:#8B5CF6,stroke-width:2px,color:white,font-weight:bold
    classDef task fill:#EC4899,stroke:#EC4899,stroke-width:2px,color:white,font-weight:bold

    %% Foundation Phase
    F[Foundation Phase<br/>Weeks 1-4]:::phase --> F1[Data Source<br/>Integration]:::task
    F --> F2[Storage Layer<br/>Setup]:::task
    F --> F3[Basic ETL<br/>Pipeline]:::task

    %% Core Phase
    C[Core Phase<br/>Weeks 5-8]:::phase --> C1[Stream<br/>Processing]:::task
    C --> C2[Pattern<br/>Detection]:::task
    C --> C3[Basic ML<br/>Models]:::task

    %% Advanced Phase
    A[Advanced Phase<br/>Weeks 9-12]:::phase --> A1[Advanced<br/>Analytics]:::task
    A --> A2[Optimization<br/>Engine]:::task
    A --> A3[API<br/>Development]:::task

    %% Final Phase
    D[Delivery Phase<br/>Weeks 13-16]:::phase --> D1[Dashboard<br/>Development]:::task
    D --> D2[Testing &<br/>Optimization]:::task
    D --> D3[Documentation &<br/>Deployment]:::task

    %% Connections
    F --> C
    C --> A
    A --> D
```
"""

    def generate_tech_stack(self):
        return """
```mermaid
%%{init: {'theme':'forest'}}%%
mindmap
    root((🔋 Energy<br/>System))
        [📊 Data Pipeline]
            (🌤️ Weather API)
            (📈 Smart Meter)
            (🔄 ETL Process)
        [💾 Storage]
            (📀 SQLite)
            (📊 Time Series)
            (⚡ Cache Layer)
        [🧠 Analytics]
            (🔍 Pattern Detection)
            (📉 Forecasting)
            (⚙️ Optimization)
        [🎯 Interface]
            (🔌 REST API)
            (📱 Dashboard)
            (🔔 Alerts)
```
"""

    def update_readme(self):
        readme_template = f"""# Smart Home Energy Optimization System

An end-to-end data engineering pipeline for optimizing home energy consumption through real-time monitoring, analysis, and ML-powered recommendations.

## System Architecture
{self.diagrams['system_architecture']}

## Implementation Roadmap
{self.diagrams['implementation_roadmap']}

## Development Phases
{self.diagrams['development_phases']}

## Technical Stack
{self.diagrams['tech_stack']}



## Project Structure
```
energy-optimization/
├── src/
│   ├── generate_mermaid_diagrams.py    # Handles both README and diagram integration
│   ├── generate_dashboard.py           # Handles main dashboard UI docs/index.html
│   ├── data_collection/
│   │   ├── weather_api.py
│   │   └── smart_meter.py
│   ├── processing/
│   │   ├── etl_pipeline.py
│   │   └── event_stream.py
│   ├── analysis/
│   │   ├── pattern_detection.py
│   │   └── ml_models.py
│   └── api/
│       ├── routes.py
│       └── optimization.py
├── docs/
│   └── index.html                      # Project Results Dashboard
└── README.md                           # Project Documentation
```

## Project Features
- Real-time energy consumption monitoring
- Weather data integration and correlation
- ML-powered usage pattern detection
- Automated optimization recommendations
- Interactive visualization dashboard

## Technical Stack
- Data Collection: Python, Weather API, Smart Meter Integration
- Storage: SQLite, Time Series Database
- Analysis: Pattern Detection, ML Models
- Interface: REST API, Web Dashboard

## Local Development
```bash
# Generate root README and dashboard
python generate_docs.py
python -m http.server --directory docs
```

## Project Results
View the working project and results at: [Project Dashboard](https://ngnnah.github.io/energy-optimization/)
"""
        with open("README.md", "w") as f:
            f.write(readme_template)

    def update_index_html(self):
        # Create HTML version of diagrams for the dashboard
        diagrams_html = f"""
<div class="module">
    <h2><i class="fas fa-project-diagram"></i> System Architecture</h2>
    <div class="mermaid">
        {self.diagrams['system_architecture'].replace('```mermaid', '').replace('```', '')}
    </div>
</div>

<div class="module">
    <h2><i class="fas fa-road"></i> Implementation Roadmap</h2>
    <div class="mermaid">
        {self.diagrams['implementation_roadmap'].replace('```mermaid', '').replace('```', '')}
    </div>
</div>

<div class="module">
    <h2><i class="fas fa-tasks"></i> Development Phases</h2>
    <div class="mermaid">
        {self.diagrams['development_phases'].replace('```mermaid', '').replace('```', '')}
    </div>
</div>


<div class="module">
    <h2><i class="fas fa-tasks"></i> Technical Stack</h2>
    <div class="mermaid">
        {self.diagrams['tech_stack'].replace('```mermaid', '').replace('```', '')}
    </div>
</div>
"""
        # Read existing index.html
        with open("docs/index.html", "r") as f:
            content = f.read()

        # Insert diagrams after the metrics section
        content = content.replace(
            "<!-- Mermaid Diagrams -->", f"{diagrams_html}\n<!-- Mermaid Diagrams -->"
        )

        # Add Mermaid.js script
        mermaid_script = """
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
    mermaid.initialize({
        theme: 'base',
        themeVariables: {
            darkMode: true,
            background: '#1e293b',
            primaryColor: '#3B82F6',
            secondaryColor: '#10B981',
            tertiaryColor: '#8B5CF6',
            primaryTextColor: '#fff',
            fontSize: '16px'
        }
    });
</script>
"""
        content = content.replace("</head>", f"{mermaid_script}\n</head>")

        # Write updated content
        with open("docs/index.html", "w") as f:
            f.write(content)


def main():
    diagrams = MermaidDiagrams()
    diagrams.update_readme()
    generate_project_dashboard()
    diagrams.update_index_html()
    print("✅ Generated README.md with Mermaid diagrams")
    print("✅ Generated project dashboard at docs/index.html")
    print("\n📊 View documentation and results at:")
    print("- README: https://github.com/ngnnah/energy-optimization")
    print("- Dashboard: https://ngnnah.github.io/energy-optimization/")


if __name__ == "__main__":
    main()
