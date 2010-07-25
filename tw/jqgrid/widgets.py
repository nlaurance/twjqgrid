from tw.api import Widget, JSLink, CSSLink
from tw.jquery import jquery_js
from tw.jquery.ui import jquery_ui_all_js
from tw.jquery.ui import

__all__ = ["Jqgrid"]

# declare your static resources here
i18n_jqgrid = JSLink(modname=__name__,
               filename='static/i18n/grid.locale-en.js',
               javascript=[])

jquery_jqgrid = JSLink(modname=__name__,
               filename='static/javascript/jquery.jqGrid.min.js',
               javascript=[jquery_js, jquery_ui_all_js, i18n_jqgrid])

jqgrid_ui_css = CSSLink(modname=__name__, filename='static/css/jquery-ui-1.8.2.custom.css')
jqgrid_css = CSSLink(modname=__name__, filename='static/css/ui.jqgrid.css')

class JqGrid(Widget):
    """
    jqgrid full options : http://www.trirand.com/jqgridwiki/doku.php?id=wiki:options
    """
    template = """
             <table id="${id}"></table>
             <div id="${id}_pager"></div>
             """

    javascript = [jquery_jqgrid]
    css = [jqgrid_ui_css, jqgrid_css]

    params = {
           "url": "Tells us where to get the data.",
           "datatype" : "This tells jqGrid the type of information being returned so it can construct the grid.",
           "mtype" :"Tells us how to make the ajax call: either 'GET' or 'POST'.",
           "colNames" :"An array in which we place the names of the columns. ",
           # column model options : http://www.trirand.com/jqgridwiki/doku.php?id=wiki:colmodel_options
           "colModel" :"An array that describes the model of the columns.",
           "pager" :"Defines that we want to use a pager bar to navigate through the records.",
           "rowNum" :"Sets how many records we want to view in the grid.",
           "rowList" :"An array to construct a select box element in the pager in which we can change the number of the visible rows.",
           "sortname" :"Sets the initial sorting column.",
           "viewrecords" :"Defines whether we want to display the number of total records from the query in the pager bar",
           "caption" :"Sets the caption for the grid.",
           }

    datatype = "json"
    mtype = "GET"

    def __init__(self, **kwargs):
        """
        """
        super(JqGrid, self).__init__(**kwargs)
        if not getattr(d,"id",None):
            raise ValueError, "JqGrid is supposed to have id"
        if not getattr(d,"url",None):
            raise ValueError, "JqGrid must have url for fetching data"
        if not getattr(d,"colModel",None):
            raise ValueError, "JqGrid must have colModel for setting up the columns"

        if not getattr(d,"pager",None):
            self.pager = '%s_pager' % self.id

    def update_params(self, d):
        super(JqGrid, self).update_params(d)

        grid_params = dict(url=self.url,
                           datatype=self.datatype,
                           mtype=self.mtype,
                           colNames=self.colNames,
                           colModel=self.colModel,
                           pager=self.pager,
                           rowNum=self.rowNum,
                           rowList=self.rowList,
                           sortname=self.sortname,
                           viewrecords=self.viewrecords,
                           caption=self.caption,
                           )
        call = js_function('$("#%s").jqGrid' % d.id)(grid_params)
        self.add_call(call)