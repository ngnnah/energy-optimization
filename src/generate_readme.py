# src/generate_readme.py
def generate_root_readme():
    readme_content = """# Smart Home Energy Optimization System

An end-to-end data engineering pipeline for optimizing home energy consumption through real-time monitoring, analysis, and ML-powered recommendations.

## System Architecture

```mermaid
graph LR
    classDef source fill:#FF6B6B,stroke:#FF6B6B,stroke-width:4px,color:white,font-weight:bold
    classDef process fill:#4ECDC4,stroke:#4ECDC4,stroke-width:4px,color:white,font-weight:bold
    classDef storage fill:#45B7D1,stroke:#45B7D1,stroke-width:4px,color:white,font-weight:bold
    classDef output fill:#96CEB4,stroke:#96CEB4,stroke-width:4px,color:white,font-weight:bold

    DataSources[Data Sources]:::source --> ETL[ETL Pipeline]:::process
    ETL --> Storage[Storage Layer]:::storage
    Storage --> Analysis[Analysis Engine]:::process
    
    DataSources --> RealTime[Real-time Stream]:::process
    RealTime --> Cache[Cache Layer]:::storage
    Cache --> ML[ML Models]:::process
    
    Analysis --> ML
    ML --> API[API Layer]:::output
    API --> Dashboard[Dashboard]:::output
```

## Development Timeline

```mermaid
graph TD
    classDef phase fill:#FF6B6B,stroke:#FF6B6B,stroke-width:4px,color:white,font-weight:bold
    classDef comp fill:#4ECDC4,stroke:#4ECDC4,stroke-width:4px,color:white,font-weight:bold

    %% Phase 1
    P1[Phase 1:<br/>Foundation]:::phase --> |4 weeks| D1[Data Pipeline<br/>Storage Layer<br/>Basic ETL]:::comp
    
    %% Phase 2
    P2[Phase 2:<br/>Analytics]:::phase --> |4 weeks| D2[Pattern Detection<br/>Time Series<br/>ML Models]:::comp
    
    %% Phase 3
    P3[Phase 3:<br/>Integration]:::phase --> |4 weeks| D3[API Development<br/>Model Deployment<br/>Testing]:::comp
    
    %% Phase 4
    P4[Phase 4:<br/>UI/Dashboard]:::phase --> |4 weeks| D4[Frontend<br/>Documentation<br/>Deployment]:::comp

    %% Layout hints
    P1 --> P2
    P3 --> P4
    P1 --> P3
    P2 --> P4
```

## Project Components

```mermaid
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
```

## Implementation Roadmap

```mermaid
graph TD
    classDef phase fill:#FF6B6B,stroke:#FF6B6B,stroke-width:4px,color:white,font-weight:bold
    classDef module fill:#4ECDC4,stroke:#4ECDC4,stroke-width:4px,color:white,font-weight:bold

    %% Top Row
    F[Foundation<br/>Module]:::phase --> |Data Flow| A[Analytics<br/>Module]:::phase
    
    %% Bottom Row
    I[Integration<br/>Module]:::phase --> |User Flow| U[UI/Dashboard<br/>Module]:::phase
    
    %% Vertical Connections
    F --> |Processing| I
    A --> |Results| U
    
    %% Components in each module
    F --> F1[ETL Pipeline<br/>Data Storage]:::module
    A --> A1[ML Models<br/>Time Series]:::module
    I --> I1[API Layer<br/>Testing]:::module
    U --> U1[Dashboard<br/>Deployment]:::module
```

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
# Install dependencies
pip install plotly pandas networkx

# Generate documentation
python src/visualization_generator.py
```

## Project Results
View the working project and results at: [Project Dashboard](https://ngnnah.github.io/energy-optimization/)
"""
    with open("README.md", "w") as f:
        f.write(readme_content)


if __name__ == "__main__":
    generate_root_readme()
