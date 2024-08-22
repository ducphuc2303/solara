import solara
from typing import(
    List,
    Any
)
import solara.lab as lab 

@solara.component
def Baselayout(
    children: list[Any]
):
    with solara.Applayout() as layout:
        with solara.Appbar() as app_bar:
            lab.ThemeToggle()
        with solara.Sidebar() as sidebar:
            ...
        with solara.Div() as content:
            content.app_children(children)
    return layout

# import solara

# @solara.component
# def BaseLayout(children):
#     with solara.Column():
#         solara.Text("My Application Header")
#         children  # Hiển thị nội dung của các trang
#         solara.Text("My Application Footer")
