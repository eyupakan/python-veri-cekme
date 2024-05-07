import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore
izmirimkart = AppStore(country='tr', app_name='i-zmirim-kart-dijital-kart', app_id = '1635926024')

izmirimkart.review(how_many=2000)
izmirimkart.reviews
ikdf = pd.DataFrame(np.array(izmirimkart.reviews),columns=['review'])
ikdf2 = ikdf.join(pd.DataFrame(ikdf.pop('review').tolist()))
ikdf2.head()
ikdf2.to_csv('Slack-app-reviews.csv')