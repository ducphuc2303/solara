# from app import main


# if __name__ == '__main__':
#     routes = main()

import solara
from app.route import routes
from app.layouts import BaseLayout

@solara.component
def App():
    solara.RouteTable(routes)

solara.render(App, layout=BaseLayout)
