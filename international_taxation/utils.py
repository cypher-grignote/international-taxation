def country_input():
    countries = {
        '1': 'France',
        '2': 'Hungary',
        '3': 'Czech Republic',
        '4': 'Bulgaria'
    }
    country = None
    first_key = min(countries.keys())
    last_key = max(countries.keys())

    while country not in countries:
        print('Choose a country')
        for key, value in countries.items():
            print(f'{key} - {value}')
        country = input(': ')
        if country not in countries:
            print(f"\nPlease, make a choice between {first_key} and {last_key}\n")
    return countries.get(country)

def legal_status_input(country):
    legal_statuses = {
        'France': ['SARL', 'SASU', 'Micro-entrepreneur'],
        'Hungary': ['KFT', 'Solo B2B', 'Solo B2C (KATA)'],
        'Czech Republic': ['OSVČ', 'SRO'],
        'Bulgaria': []
    }

def day_required(tjm, ca):
    return round(ca/tjm)