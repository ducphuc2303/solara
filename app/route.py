import solara as slr
from app.layouts import (
    BaseLayout,
)
from app.pages import (
    HomePage,
    VizPage,
)

ROUTES = [
    {
        'path': '/',
        'component': HomePage,
        'label': 'Trang chủ',
        'layout': BaseLayout,
    },
    {
        'path': 'viz',
        'component': VizPage,
        'label': 'Viz',
    }
]