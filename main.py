from controller.main_controller import start, cleanup


def main():
    try:
        start()
    finally:
        cleanup()


if __name__ == "__main__":
    main()

