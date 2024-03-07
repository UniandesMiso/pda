from requests import post

from bff.utils import get_properties_url, get_contracts_url, get_listings_url


def create_ground_mutation(_, info, input):
    url = get_properties_url()
    response = post(f"{url}/grounds", json=input)
    return response.json()


def create_sale_mutation(_, info, input):
    url = get_contracts_url()
    response = post(f"{url}/sales", json=input)
    return response.json()


def process_listing_mutation(_, info, input):
    url = get_listings_url()
    response = post(f"{url}/information", json=input)
    return response.json()
