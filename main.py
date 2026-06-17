from infra.logger import LoggerFactory
from ui.app_window import AppWindow


def main():

    logger = LoggerFactory.create_logger()

    app = AppWindow(logger)

    app.start()


if __name__ == "__main__":
    main()