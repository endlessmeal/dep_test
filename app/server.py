from aiohttp import web
from app.routes import setup_routes
from app.models import database, Page, Block


async def init_pg(app):
    with open('app/script.sql') as f:
        script = f.readlines()
    sql = ''
    for scr in script:
        sql += scr
    app["db"] = database
    database.create_tables([Page, Block])
    if Page.select().count() == 0:
        database.execute_sql(sql)


def make_app():
    app = web.Application()
    setup_routes(app)
    app.on_startup.append(init_pg)
    return app


web.run_app(make_app())
