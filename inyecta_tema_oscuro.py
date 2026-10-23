"""Añade el enlace a tema-oscuro.css en todas las páginas .htm del repositorio."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
ENLACE = '<link rel="stylesheet" href="tema-oscuro.css">'


def inyectar(ruta: Path) -> bool:
    """Inserta ENLACE antes de </head>. Devuelve True si el archivo cambió."""
    try:
        html = ruta.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Omitido (no es UTF-8): {ruta.name}")
        return False
    if ENLACE in html or "</head>" not in html:
        return False
    ruta.write_text(html.replace("</head>", f"{ENLACE}\n</head>", 1), encoding="utf-8")
    return True


def main() -> None:
    """Procesa todas las páginas .htm en la raíz."""
    cambiadas = sum(inyectar(p) for p in sorted(RAIZ.glob("*.htm")))
    print(f"Páginas modificadas: {cambiadas}")


if __name__ == "__main__":
    main()