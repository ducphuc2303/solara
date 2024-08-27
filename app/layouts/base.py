import solara
from typing import(
    Any
)
import solara.lab as lab 

@solara.component
def BaseLayout(
    children: list[Any]
):
    with solara.AppLayout() as layout:
        with solara.AppBar() as app_bar:
            lab.ThemeToggle()
        with solara.Sidebar() as sidebar:
            ...
        with solara.Div() as content:
            content.add_children(children)
    return layout