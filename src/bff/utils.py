from os import environ


def get_properties_url():
    return (
        "http://"
        + f"{environ.get('PROPERTIES_HOST', 'localhost')}:"
        + f"{environ.get('PROPERTIES_PORT', '3000')}"
    )


def get_contracts_url():
    return (
        "http://"
        + f"{environ.get('CONTRACTS_HOST', 'localhost')}:"
        + f"{environ.get('CONTRACTS_PORT', '3001')}"
    )


def get_listings_url():
    return (
        "http://"
        + f"{environ.get('LISTINGS_HOST', 'localhost')}:"
        + f"{environ.get('LISTINGS_PORT', '3002')}"
    )
