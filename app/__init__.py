from app.route import ROUTES
import solara


def get_routes():
    routes = []
    init_layout=0
    for route in ROUTES:
        routes.append(
            solara.Route(
                path=route['path'],
                component=route['component'],
                label=route['label'],
                layout=route['layout'] if init_layout==0 else None,
            )
        )
        init_layout+=1
    return routes

def main():
    return get_routes()