from sanic import response


async def handle(request):
    from app.models.documents import Posts
    tpost = Posts(
        title='Inserted via umongo+sanic apis',
        body='Running test;',
        published=True,
        meta={
            'dvotes': 0,
            'update': 0
        }
    )
    #r = await posts.find_one()
    await tpost.commit()

    return response.json(tpost.dump())

async def getAll(request):
    from app.models.documents import Posts
    posts = Posts()
    r = await posts.find_one()

    return response.json(r)
