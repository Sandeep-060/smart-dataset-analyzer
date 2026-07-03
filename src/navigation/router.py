from src.pages.home import show_home_page
from src.pages.overview import show_overview_page
from src.pages.data_quality import show_data_quality_page
from src.pages.statistics import show_statistics_page
from src.pages.visualizations import show_visualization_page
from src.pages.correlation import show_correlation_page
from src.pages.outliers import show_outliers_page
from src.pages.feature_engineering import show_feature_engineering_page
from src.pages.health_score import show_health_score_page
from src.pages.report import show_report_page

def route_page(selected_page: str):
    """
    Display the correct page
    based on the selected navigation option.
    """

    routes = {
        "🏠 Home": show_home_page,
        "📁 Dataset Overview": show_overview_page,
        "🧹 Data Quality": show_data_quality_page,
        "📊 Statistics": show_statistics_page,
        "📈 Visualizations": show_visualization_page,
        "🔗 Correlation": show_correlation_page,
        "⚠ Outlier Detection": show_outliers_page,
        "⚙ Feature Engineering": show_feature_engineering_page,
        "❤️ Health Score": show_health_score_page,
        "📄 Report": show_report_page,
    }

    page_function = routes.get(selected_page)
    
    if page_function:
        page_function()