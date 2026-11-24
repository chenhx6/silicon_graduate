"""Launch the desktop editor; no browser or web server required."""


def main(argv=None):
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="PDM desktop application")
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run the packaged Qt smoke test and exit",
    )
    parser.add_argument("--report", default="pdm-platform-report.json")
    args = parser.parse_args(argv)
    if args.self_test:
        from multipolepdm.gui.self_test import run_self_test

        return run_self_test(args.report)

    from PySide6.QtWidgets import QApplication
    from multipolepdm.gui.window import MainWindow

    app = QApplication.instance() or QApplication(sys.argv)
    app.setApplicationName("PDM")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
