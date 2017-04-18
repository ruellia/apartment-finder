import os
import json

json_path = os.getenv('JSON_SETTINGS', "")

with open(json_path, 'r') as f:
    config = json.load(f)

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = config.get('min_price')

# The maximum rent you want to pay per month.
MAX_PRICE = config.get('max_price')

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = config.get('craigslist_site')

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = config.get('areas')

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "albany": [
        [37.898925, -122.373782],
        [37.866726, -122.281639],
    ],
    "rockridge": [
        [37.83826, -122.24073],
        [37.84680, -122.25944],
    ],
    "berkeley": [
        [37.86226, -122.25043],
        [37.86781, -122.26502],
    ],
    "north_berkeley": [
        [37.86425, -122.26330],
        [37.87655, -122.28974],
    ],
    "oakland": [
        [37.885438, -122.355881],
        [37.631714, -122.114793],
    ],
    "richmond": [
        [37.77188, -122.47263],
        [37.78029, -122.51005],
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = config.get('neighborhoods')

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = config.get('max_transit_distance') # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "oakland_19th_bart": [37.8118051,-122.2720873],
    "macarthur_bart": [37.8265657,-122.2686705],
    "rockridge_bart": [37.841286,-122.2566329],
    "downtown_berkeley_bart": [37.8629541,-122.276594],
    "north_berkeley_bart": [37.8713411,-122.2849758],
    "el_cerrito_plaza_bart": [37.902694, -122.298968]
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = config.get('craigslist_housing_section')

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#quikrent"

# The token that allows us to connect to slack.
SLACK_TOKEN = config.get('slack_token')

# ruellia's experiments
BEDROOMS = config.get('bed')

BATHROOMS = config.get('bath')
