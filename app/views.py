from aiohttp import web
from app.models import Page, Block
from app.schema import ListBlocksSchema, BlockData


async def all_pages(request):
    query = Block.select().dicts()
    blocks = []
    for block in query:
        blocks.append({'name': block.get('name'), 'url': block.get('url')})
    block = BlockData(blocks)
    schema = ListBlocksSchema()
    data = schema.dump(block)
    return web.Response(
        content_type="application/json", text=str(data)
    )


async def show_page(request):
    id = request.match_info.get("page_id")
    update_query = Block.update(views=Block.views + 1).where(Block.page_id == id)
    update_query.execute()
    query = Block.select().where(Block.page_id == id).dicts()
    blocks = []
    for block in query:
        blocks.append({
            'name': block.get('name'),
            'url': block.get('url'),
            'page_id': id,
            'views': block.get('views')
        })
    block = BlockData(blocks)
    schema = ListBlocksSchema()
    data = schema.dump(block)

    return web.Response(
        content_type="application/json", text=str(data)
    )
