from app import main

if __name__ == '__main__':
    routes = main()

################################################################
# cách 2:
# import solara
# from app.pages.home import HomePage
# from app.pages.viz import VizPage
# from app.layouts.base import BaseLayout

# # @solara.component
# # def Page():
# #     solara.lab.ThemeToggle()

# routes = [
#     solara.Route(path="/", component=HomePage, label="HomePage", layout=BaseLayout),
#     solara.Route(path="viz", component=VizPage, label="VizPage")
# ]