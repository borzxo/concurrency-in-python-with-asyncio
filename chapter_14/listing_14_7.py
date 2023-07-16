async def s_h():
    print('Hello')


async def s_g():
    print('Goodbye')


async def m_g():
    await s_h()
    await s_g()


coro = m_g()

coro.send(None)
