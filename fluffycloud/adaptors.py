"""FluffyCloud cloud adaptor."""

import functools

_fluffycloud_sdk = None


def import_package(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global _fluffycloud_sdk
        if _fluffycloud_sdk is None:
            try:
                import fluffycloud as _fluffycloud  # pylint: disable=import-outside-toplevel
                _fluffycloud_sdk = _fluffycloud
            except ImportError:
                raise ImportError(
                    'Fail to import dependencies for fluffycloud.'
                    'Try pip install "skypilot[fluffycloud]"') from None
        return func(*args, **kwargs)

    return wrapper


@import_package
def fluffycloud():
    """Return the fluffycloud package."""
    return _fluffycloud_sdk
