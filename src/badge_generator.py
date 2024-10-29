# src/badge_generator.py
class DocumentationBadges:
    def __init__(self):
        self.base_url = "https://hits.seeyoufarm.com/api/count/incr/badge.svg"
        self.github_pages_url = "ngnnah.github.io/energy-optimization"

    def get_badges_config(self):
        """Define badges for different sections with custom colors"""
        return {
            "index": {"color": "#79C83D", "title": "docs_visits"},  # Green
            "visuals/pipeline": {  # Updated path
                "color": "#FF6B6B",  # Red
                "title": "pipeline_views",
            },
            "visuals/timeline": {  # Updated path
                "color": "#4ECDC4",  # Teal
                "title": "timeline_views",
            },
            "visuals/tech_stack": {  # Updated path
                "color": "#45B7D1",  # Blue
                "title": "stack_views",
            },
        }

    def generate_badge_markdown(self, page_name, color_bg="#79C83D", title="visits"):
        """Generate markdown for a badge with custom colors and title"""
        if page_name:
            encoded_url = f"https%3A%2F%2F{self.github_pages_url}%2F{page_name}"
        else:
            encoded_url = f"https%3A%2F%2F{self.github_pages_url}"

        badge_url = f"{self.base_url}?url={encoded_url}&count_bg={color_bg.replace('#', '%23')}&title_bg=%23555555&title={title}&edge_flat=false"
        return f"[![{title}]({badge_url})](https://hits.seeyoufarm.com)"

    def generate_badge_html(self, page_name, color_bg="#79C83D", title="visits"):
        """Generate HTML for a badge with custom colors and title"""
        if page_name:
            encoded_url = f"https%3A%2F%2F{self.github_pages_url}%2F{page_name}"
        else:
            encoded_url = f"https%3A%2F%2F{self.github_pages_url}"

        badge_url = f"{self.base_url}?url={encoded_url}&count_bg={color_bg.replace('#', '%23')}&title_bg=%23555555&title={title}&edge_flat=false"
        return f'<img src="{badge_url}" alt="{title}" />'
