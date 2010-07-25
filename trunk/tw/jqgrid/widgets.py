from tw.api import Widget, JSLink, CSSLink

__all__ = ["Jqgrid"]

# declare your static resources here

## JS dependencies can be listed at 'javascript' so they'll get included
## before
# my_js = JSLink(modname=__name__, 
#                filename='static/jqgrid.js', javascript=[])

# my_css = CSSLink(modname=__name__, filename='static/jqgrid.css')

class Jqgrid(Widget):
    template = """<div id="${id}">${value}</div>"""
    ## You can also define the template in a separate package and refer to it
    ## using Buffet style uris
    #template = "tw.jqgrid.templates.jqgrid"

    #javascript = [my_js]
    #css = [my_css]

    def __init__(self, id=None, parent=None, children=[], **kw):
        """Initialize the widget here. The widget's initial state shall be
        determined solely by the arguments passed to this function; two
        widgets initialized with the same args. should behave in *exactly* the
        same way. You should *not* rely on any external source to determine
        initial state."""
        super(Jqgrid, self).__init__(id, parent, children, **kw)

    def update_params(self, d):
        """This method is called every time the widget is displayed. It's task
        is to prepare all variables that are sent to the template. Those
        variables can accessed as attributes of d."""
        super(Jqgrid, self).update_params(d)
