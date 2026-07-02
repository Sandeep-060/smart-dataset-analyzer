from src.components.sidebar import show_sidebar
from src.navigation.router import route_page
from src.utils.session import initialize_session_state

def main():
    initialize_session_state()
    selected_page = show_sidebar()
    route_page(selected_page)

if __name__ == "__main__":
    main()