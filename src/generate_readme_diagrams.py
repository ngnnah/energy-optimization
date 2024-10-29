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
    %% Styling
    classDef phase fill:#3B82F6,stroke:#3B82F6,stroke-width:2px,color:white,font-weight:bold
    classDef module fill:#10B981,stroke:#10B981,stroke-width:2px,color:white,font-weight:bold

    %% Phase 1: Foundation
    P1[Data Collection & Storage]:::phase --> M1[Weather API Integration]:::module
    P1 --> M2[Smart Meter Setup]:::module
    P1 --> M3[Database Design]:::module

    %% Phase 2: Processing
    P2[Data Processing]:::phase --> M4[ETL Pipeline]:::module
    P2 --> M5[Stream Processing]:::module
    P2 --> M6[Cache System]:::module

    %% Phase 3: Analytics
    P3[Analytics & ML]:::phase --> M7[Pattern Detection]:::module
    P3 --> M8[Predictive Models]:::module
    P3 --> M9[Optimization Logic]:::module

    %% Phase 4: Interface
    P4[API & Dashboard]:::phase --> M10[REST API]:::module
    P4 --> M11[Visualization]:::module
    P4 --> M12[Documentation]:::module

    %% Connections
    M3 --> P2
    M6 --> P3
    M9 --> P4
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
mindmap
    root((Energy<br/>System))
        Data Collection
            Python Scripts
            REST APIs
            Smart Meter SDK
        Processing
            Apache Airflow
            Redis Cache
            Stream Processing
        Storage
            Time Series DB
            SQLite
            Data Lake
        Analytics
            scikit-learn
            Prophet
            TensorFlow
        Interface
            FastAPI
            React
            D3.js
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
│   └── index.html      # Project Results Dashboard
└── README.md          # Project Documentation
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
# Generate root README
python generate_readme_diagrams.py
python generate_dashboard.py
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
"""
        # Read existing index.html
        with open("docs/index.html", "r") as f:
            content = f.read()

        # Insert diagrams after the metrics section
        content = content.replace(
            "<!-- Modules Section -->", f"{diagrams_html}\n<!-- Modules Section -->"
        )

        # Add Mermaid.js script
        mermaid_script = """
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
    mermaid.initialize({
        theme: 'dark',
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
    diagrams.update_index_html()


if __name__ == "__main__":
    main()
