import logging

from behave import given, when, then

from features.configuration.configuration import Configuration
from features.pages.TescoLocationPage import TescoLocationPage

@given(u'I have a range of store IDs from {start:d} to {finish:d}')
def step_impl(context, start, finish):
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    context.start = start
    context.finish = finish
    context.invalidStoreID = []
    context.stores = []




@given(u'I retrieve the location details')
def step_impl(context):
    page = TescoLocationPage()
    config = Configuration()
    start = context.start
    finish = context.finish
    while start <= finish:
        context.currentURL = config.getURL().format(str(start))
        if page.getStorLocation(context, start) == False:
            context.invalidStoreID.append(start)
        start = start + 1


@then(u'I write out locations to the std output')
def step_impl(context):
    for stores in context.stores:
        print(stores['storeID'])
        print(stores['storeName'])
        print(stores['address'])
        print(stores['telephone'])

