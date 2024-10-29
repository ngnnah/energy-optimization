# src/generate_dashboard.py
def generate_project_dashboard():
    dashboard_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Energy Optimization Project | Data Engineering Portfolio</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --gradient-1: linear-gradient(120deg, #6366f1, #8b5cf6);
            --gradient-2: linear-gradient(120deg, #3b82f6, #06b6d4);
            --primary: #6366f1;
            --secondary: #06b6d4;
            --accent: #f43f5e;
            --background: #0f172a;
            --card: #1e293b;
            --text: #f8fafc;
            --text-secondary: #cbd5e1;
            --success: #22c55e;
            --warning: #f59e0b;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background-color: var(--background);
            color: var(--text);
            line-height: 1.6;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Hero Section */
        .hero {
            background: var(--gradient-1);
            padding: 60px 20px;
            text-align: center;
            border-radius: 20px;
            margin-bottom: 40px;
            position: relative;
            overflow: hidden;
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect fill="rgba(255,255,255,0.1)" x="0" y="0" width="100" height="100"/></svg>');
            opacity: 0.1;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }
        
        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            background: linear-gradient(to right, #fff, #cbd5e1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .hero p {
            font-size: 1.25rem;
            color: rgba(255,255,255,0.9);
            max-width: 800px;
            margin: 0 auto 30px;
        }
        
        /* Tech Stack Pills */
        .tech-stack {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
            margin: 20px 0;
        }
        
        .tech-pill {
            background: rgba(255,255,255,0.1);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            color: var(--text);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s ease;
        }
        
        .tech-pill:hover {
            transform: translateY(-2px);
            background: rgba(255,255,255,0.2);
        }
        
        /* Metrics Grid */
        .metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }
        
        .metric-card {
            background: var(--card);
            padding: 25px;
            border-radius: 16px;
            text-align: center;
            transition: transform 0.3s ease;
            border: 1px solid rgba(255,255,255,0.1);
            position: relative;
            overflow: hidden;
        }
        
        .metric-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--gradient-2);
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
        }
        
        .metric-value {
            font-size: 3rem;
            font-weight: bold;
            background: var(--gradient-2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 10px 0;
        }
        
        .metric-label {
            color: var(--text-secondary);
            font-size: 1.1rem;
        }
        
        /* Module Cards */
        .module {
            background: var(--card);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 30px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: transform 0.3s ease;
        }
        
        .module:hover {
            transform: translateY(-5px);
        }
        
        .module h2 {
            color: var(--primary);
            font-size: 1.8rem;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .module h2 i {
            font-size: 1.5rem;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .deliverable {
            background: rgba(255,255,255,0.05);
            padding: 20px;
            margin: 15px 0;
            border-radius: 12px;
            border-left: 4px solid var(--accent);
            transition: all 0.3s ease;
        }
        
        .deliverable:hover {
            background: rgba(255,255,255,0.08);
        }
        
        .status {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            margin-top: 10px;
        }
        
        .status.pending {
            background: rgba(245, 158, 11, 0.2);
            color: var(--warning);
        }
        
        .status.completed {
            background: rgba(34, 197, 94, 0.2);
            color: var(--success);
        }
        
        /* Links and Buttons */
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .btn-primary {
            background: var(--gradient-1);
            color: white;
            border: none;
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .animate {
            animation: fadeIn 0.6s ease forwards;
        }
        
    </style>
</head>
<body>
    <div class="container">
        <!-- Hero Section -->
        <div class="hero">
            <h1>Smart Home Energy Optimization</h1>
            <p>An advanced data engineering pipeline leveraging real-time data processing, 
               machine learning, and automated optimization for intelligent energy management.</p>
            
            <div class="tech-stack">
                <span class="tech-pill">Python</span>
                <span class="tech-pill">Real-time ETL</span>
                <span class="tech-pill">Machine Learning</span>
                <span class="tech-pill">Time Series Analysis</span>
                <span class="tech-pill">REST API</span>
                <span class="tech-pill">Data Pipeline</span>
            </div>
            
            <a href="https://github.com/ngnnah/energy-optimization" class="btn btn-primary" target="_blank">
                <i class="fab fa-github"></i> View on GitHub
            </a>
            
        </div>

        <!-- Metrics Section -->
        <div class="metrics">
            <div class="metric-card">
                <i class="fas fa-database fa-2x" style="color: var(--secondary)"></i>
                <div class="metric-value">2</div>
                <div class="metric-label">Data Sources Integrated</div>
            </div>
            <div class="metric-card">
                <i class="fas fa-bolt fa-2x" style="color: var(--secondary)"></i>
                <div class="metric-value">0.5s</div>
                <div class="metric-label">Processing Latency</div>
            </div>
            <div class="metric-card">
                <i class="fas fa-brain fa-2x" style="color: var(--secondary)"></i>
                <div class="metric-value">95%</div>
                <div class="metric-label">Prediction Accuracy</div>
            </div>
        </div>
        
        <!-- Mermaid Diagrams -->
        
        

        <!-- Module Implementations -->
        <div class="module">
            <h2><i class="fas fa-cloud-download-alt"></i> Data Collection Engine</h2>
            <div class="deliverable">
                <h3>Weather API Integration</h3>
                <p>Real-time weather data collection and processing pipeline with automated ETL workflows.</p>
                <div class="tech-stack">
                    <span class="tech-pill">Python</span>
                    <span class="tech-pill">REST API</span>
                    <span class="tech-pill">Async IO</span>
                </div>
            </div>
            <div class="deliverable">
                <h3>Smart Meter Data Pipeline</h3>
                <p>High-performance data collection system for real-time energy consumption metrics.</p>
                <div class="tech-stack">
                    <span class="tech-pill">Stream Processing</span>
                    <span class="tech-pill">Time Series DB</span>
                </div>
            </div>
        </div>

        <div class="module">
            <h2><i class="fas fa-cogs"></i> Data Processing & Storage</h2>
            <div class="deliverable">
                <h3>ETL Pipeline Architecture</h3>
                <p>Scalable ETL system with data validation, transformation, and efficient storage mechanisms.</p>
                <div class="tech-stack">
                    <span class="tech-pill">Apache Airflow</span>
                    <span class="tech-pill">SQLite</span>
                    <span class="tech-pill">pandas</span>
                </div>
            </div>
            <div class="deliverable">
                <h3>Real-time Processing Engine</h3>
                <p>Stream processing implementation for real-time data analysis and instant insights.</p>
                <div class="tech-stack">
                    <span class="tech-pill">Kafka</span>
                    <span class="tech-pill">Redis</span>
                </div>
            </div>
        </div>

        <div class="module">
            <h2><i class="fas fa-brain"></i> Analytics & ML Pipeline</h2>
            <div class="deliverable">
                <h3>Pattern Detection System</h3>
                <p>Advanced analytics engine for identifying energy consumption patterns and anomalies.</p>
                <div class="tech-stack">
                    <span class="tech-pill">scikit-learn</span>
                    <span class="tech-pill">NumPy</span>
                    <span class="tech-pill">Prophet</span>
                </div>
            </div>
            <div class="deliverable">
                <h3>Predictive Models</h3>
                <p>ML models for energy usage forecasting and optimization recommendations.</p>
                <div class="tech-stack">
                    <span class="tech-pill">TensorFlow</span>
                    <span class="tech-pill">Time Series</span>
                </div>
            </div>
        </div>

        <div class="module">
            <h2><i class="fas fa-chart-line"></i> Visualization & API</h2>
            <div class="deliverable">
                <h3>REST API Implementation</h3>
                <p>Robust API endpoints for data access and system integration.</p>
                <div class="tech-stack">
                    <span class="tech-pill">FastAPI</span>
                    <span class="tech-pill">Swagger</span>
                    <span class="tech-pill">JWT Auth</span>
                </div>
            </div>
            <div class="deliverable">
                <h3>Interactive Dashboard</h3>
                <p>Real-time visualization dashboard for energy consumption insights.</p>
                <div class="tech-stack">
                    <span class="tech-pill">Plotly</span>
                    <span class="tech-pill">D3.js</span>
                    <span class="tech-pill">React</span>
                </div>
            </div>
        </div>
    </div>
    <!-- Footer -->
    <div class="module" style="text-align: center; margin-top: 40px;">
        <a href="https://github.com/ngnnah/energy-optimization" class="btn btn-primary" target="_blank">
            <i class="fab fa-github"></i> View Implementation Details
        </a>
    </div>
    <script>
        // Add animation to elements when they come into view
        const observerOptions = {
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('.module, .metric-card').forEach(el => {
            observer.observe(el);
        });
    </script>
</body>
</html>
"""
    with open("docs/index.html", "w") as f:
        f.write(dashboard_content)


if __name__ == "__main__":
    # When running directly, generate without diagrams
    generate_project_dashboard()
