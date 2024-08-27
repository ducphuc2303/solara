from app.pages.home import HomePage
from app.pages.viz import VizPage
from app.layouts.base import BaseLayout

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