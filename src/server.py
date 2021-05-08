from core import app
import logging


logging.basicConfig(
    format=(
        '%(asctime)s,%(msecs)-3d - %(name)-12s - %(levelname)-8s => '
        '%(message)s'
    ),
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

if __name__ == '__main__':
    import routes
    app.run(host='0.0.0.0', port=3200)
    logging.getLogger(__name__).info("Server is running")
