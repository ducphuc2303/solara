import solara
from app.pages import HomePage, VizPage

routes = [
    solara.Route(path="/", component=HomePage, name="Home"),
    solara.Route(path="/viz", component=VizPage, name="Visualization"),
]
