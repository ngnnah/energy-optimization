# src/badge_generator.py
class DocumentationBadges:
    def __init__(self):
        self.base_url = "https://hits.seeyoufarm.com/api/count/incr/badge.svg"
        self.github_pages_url = (
            "https://ngnnah.github.io/energy-optimization"  # Update this
        )

    def generate_badge_markdown(self, page_name, color_bg="#79C83D", title="visits"):
        """Generate markdown for a badge with custom colors and title"""
        encoded_url = f"https%3A%2F%2F{self.github_pages_url}%2F{page_name}"
        badge_url = f"{self.base_url}?url={encoded_url}&count_bg={color_bg.replace('#', '%23')}&title_bg=%23555555&title={title}&edge_flat=false"
        return f"[![{title}]({badge_url})](https://hits.seeyoufarm.com)"

    def generate_badge_html(self, page_name, color_bg="#79C83D", title="visits"):
        """Generate HTML for a badge with custom colors and title"""
        encoded_url = f"https%3A%2F%2F{self.github_pages_url}%2F{page_name}"
        badge_url = f"{self.base_url}?url={encoded_url}&count_bg={color_bg.replace('#', '%23')}&title_bg=%23555555&title={title}&edge_flat=false"
        return f'<img src="{badge_url}" alt="{title}" />'

    def get_badges_config(self):
        """Define badges for different sections with custom colors"""
        return {
            "index": {"color": "#79C83D", "title": "total_visits"},  # Main page
            "pipeline": {"color": "#FF6B6B", "title": "pipeline_views"},
            "timeline": {"color": "#4ECDC4", "title": "timeline_views"},
            "tech_stack": {"color": "#45B7D1", "title": "stack_views"},
        }
