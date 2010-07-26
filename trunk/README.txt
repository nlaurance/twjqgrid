
tw.jqgrid documentation
=======================


tw.jqmultiselect is a tosca widget wrapper around jquery grid plugin
 which can be found here :

`http://www.trirand.com/blog/`_

the version released with this package is 3.7.2

in the view controller ::

    from tw.jqgrid import JqGrid
    colNames = ['ID','Title', 'Synopsis']
    colModel = [
                {'name':'id', 'index':'id', 'width':20, 'align':'right'},
                {'name':'title', 'index':'title','width':100, 'align':'left'},
                {'name':'synopsis', 'index':'synopsis','width':580, 'align':'left', 'sortable':False},
               ]
    grid_local = JqGrid(id='movie_list', url='/medias/fetch', caption='Movies',
                colNames=colNames, colModel=colModel,
                rowList=[10,20,50], rowNum=10,
                sortname='title',
                viewrecords=True,
                width=1000,
                shrinkToFit=True,
    )

    class MoviesController(BaseRestController):

        @expose('qubic.backoffice.templates.rest.movies.get_all')
        def get_all(self):
            pylons.c.grid = grid_local
            return dict(page='all medias')

in the template::

    ${tmpl_context.grid()}

now to feed data we need a controller::

    @expose('json')
    def fetch(self, page=1, rows=10, sidx=1, sord='asc', qtype=None, query=None, **kwargs):
        offset = (int(page)-1) * int(rows)
        q = Movie.query
        if (query):
            field = str(qtype)
            field_attr = Movie.__getattribute__(Movie, field)
            medias_q = medias_q.filter(field_attr.like(u'%%%s%%' % query))

        result_count = medias_q.count()
        total = result_count / int(rows)
        column = getattr(Movie.table.c, sidx)
        movies = q.order_by(getattr(column,sord)()).offset(offset).limit(rows)
        rows = [{'id'  : movie.id,
                 'cell': [movie.id,  '<a href="/medias/%s/">%s</a>' % (movie.id, movie.title),
                          movie.synopsis]} for movie in movies]
        return dict(page=page, total=total, records=result_count, rows=rows)


.. note:: this is written for an elixir model, adapt to your need