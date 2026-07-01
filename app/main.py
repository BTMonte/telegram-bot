import asyncio
import logging
import signal

from app.core.config import BOT_TOKEN, ENV
from app.db.postgres import connect_postgres, close_postgres
from app.bot.bot import create_application


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


async def startup():
    logger.info(f"Starting application in {ENV} mode...")

    # DB ONLY in production
    if ENV == "prod":
        await connect_postgres()
        logger.info("Postgres connected")
    else:
        logger.info("Local mode: skipping Postgres connection")

    app = create_application(BOT_TOKEN)

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    logger.info("Bot started")
    return app


async def shutdown(app):
    logger.info("Shutting down...")

    try:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()
    except Exception as e:
        logger.warning(f"Bot shutdown issue: {e}")

    if ENV == "prod":
        try:
            await close_postgres()
            logger.info("Postgres disconnected")
        except Exception as e:
            logger.warning(f"DB shutdown issue: {e}")


async def main():
    app = await startup()

    stop_event = asyncio.Event()

    def stop():
        stop_event.set()

    signal.signal(signal.SIGINT, lambda *_: stop())
    signal.signal(signal.SIGTERM, lambda *_: stop())

    await stop_event.wait()

    await shutdown(app)


if __name__ == "__main__":
    asyncio.run(main())