from app.views import all_pages, show_page


def setup_routes(app):
    app.router.add_get('/api/v1/list_pages', all_pages)
    app.router.add_get('/api/v1/page/{page_id}', show_page)
