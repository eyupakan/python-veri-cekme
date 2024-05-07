import pandas as pd
import numpy as np
import json

from google_play_scraper import Sort, reviews, app

app_package_name = 'com.asis.izmirimkart'  # uygulamanın paket adını buraya yazın

result, _ = reviews(app_package_name, lang='tr', sort=Sort.NEWEST, count=2000) # burada 'tr' parametresi Türkçe yorumlar için kullanılıyor

reviews_df = pd.DataFrame(result)
reviews_df.to_csv('Play-Store-app-reviews.csv')