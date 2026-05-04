from livereload import Server
from pathlib import Path

ROOT = Path(__file__).parent
HOST = "127.0.0.1"
PORT = 5500


def main() -> None:
    server = Server()
    server.watch(str(ROOT / "*.html"))
    server.watch(str(ROOT / "**/*.html"))
    server.watch(str(ROOT / "**/*.css"))
    server.watch(str(ROOT / "**/*.js"))
    print(f"Serving {ROOT} at http://{HOST}:{PORT}/")
    server.serve(host=HOST, port=PORT, root=str(ROOT), default_filename="index.html", open_url_delay=1)


if __name__ == "__main__":
    main()
