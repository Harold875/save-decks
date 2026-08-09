from importlib.metadata import version, PackageNotFoundError


def get_version(package_name: str = "save-decks") -> str:
    """
    Get the project version from the Python metadata
    """
    # Buscar en los metadatos del paquete instalado
    try:
        return version(package_name)
    except PackageNotFoundError:
        return "0.0.0-dev"


if __name__ == "__main__":
    a = get_version()
    print(a)
