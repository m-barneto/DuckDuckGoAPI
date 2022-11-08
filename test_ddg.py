import pytest
import requests

DDG_API_URL = 'https://api.duckduckgo.com'
CURRENT_PRESIDENTS = [
    'Washington',
    'Adams',
    'Jefferson',
    'Madison',
    'Monroe',
    'Jackson',
    'Buren',
    'Harrison',
    'Tyler',
    'Polk',
    'Taylor',
    'Fillmore',
    'Pierce',
    'Buchanan',
    'Lincoln',
    'Johnson',
    'Grant',
    'Hayes',
    'Garfield',
    'Arthur',
    'Cleveland',
    'McKinley',
    'Roosevelt',
    'Taft',
    'Wilson',
    'Harding',
    'Coolidge',
    'Hoover',
    'Truman',
    'Eisenhower',
    'Kennedy',
    'Nixon',
    'Ford',
    'Carter',
    'Reagan',
    'Bush',
    'Clinton',
    'Obama',
    'Trump',
    'Biden',
]


def test_ddg_presidents():
    # Term to search for
    search_item = 'presidents of the united states'

    # Get response from api and get the json data
    resp = requests.get(DDG_API_URL + f'/?q={search_item}&format=json')
    rsp_data = resp.json()

    # Create a list of text entries containing all the text information in RelatedTopics
    entries = []
    for entry in list(rsp_data['RelatedTopics']):
        entries.append(entry['Text'])
    
    # Copy our list of presidents
    # By making CURRENT_PRESIDENTS, we can use it if we need to add more tests
    # We need to copy it instead of modifying directly because it's a constant that should be updated when new presidents are elected
    # If we modified it directly, it could interfere with tests added in the future
    president_names = CURRENT_PRESIDENTS.copy()

    # Go through each text entry
    for text_entry in entries:
        # Then interate over each president in our list
        for president in president_names:
            # If we find the president name in our current entry
            if president in text_entry:
                # Remove it from our list
                president_names.remove(president)
    
    # We should be left over with an empty list
    assert len(president_names) == 0, f"Presidents weren't listed: {president_names}"