import asyncio
import asyncpg
import logging


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port='5432',
                                       user='postgres',
                                       database='products',
                                       password='password')
    try:
        async with connection.transaction():
            insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand')"
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception as e:
        logging.exception(f'Error while running transaction: {e}')
    finally:
        query = """SELECT brand_name FROM brand
                    WHERE brand_name LIKE 'big_%"""
        brands = await connection.fetch(query)
        print(f'Query result was: {brands}')

        await connection.close()

asyncio.run(main())
