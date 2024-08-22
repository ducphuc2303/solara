import solara
from app.components import (
    MdEditorDev
)


@solara.component
def HomePage():
    with solara.Div() as page:
        show_edit_md, set_show_edit_md = solara.use_state(False)
        solara.Button(
            label='Edit Markdown',
            on_click=lambda: set_show_edit_md(not show_edit_md)
        )
        
        MdEditorDev(show_edit_md=show_edit_md)
    return page