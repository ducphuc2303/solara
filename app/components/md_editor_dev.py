import solara


@solara.component
def MdEditorDev(
    show_edit_md=False
):
    current_content, set_current_content = solara.use_state('')
    with solara.ColumnsResponsive(
            default=[12, 12], 
            medium=[6,6] if show_edit_md else [12, 12],
        ) as col:
        with solara.Div(
            style={
                'height': '500px',
                'border': '1px solid black',
                'padding': '10px',
                'border-radius': '5px',
                'display': 'none' if not show_edit_md else 'block',
            },
        ) as col1:
            solara.MarkdownEditor(value="", on_value=lambda x: set_current_content(x))
        with solara.Div() as col2:
            solara.Markdown(md_text=current_content)
    return col


# import solara

# @solara.component
# def MdEditorDev():
#     content, set_content = solara.use_state("")

#     def on_change(new_value):
#         set_content(new_value)

#     solara.Markdown(content)
#     solara.TextArea(on_value_change=on_change, value=content)
