from TwitterAPI import TwitterAPI
import unicodedata
import time
import datetime

#INSERT SEARCH QUERY IN THE SINGLE QUOTATIONS
SEARCH_TERM  = 'INSERT QUERY HERE'

GeocodeArray = ["32.366805,-86.299969,200mi",
                "58.301944,-134.419722,500mi",
                "33.448377,-112.074037,125mi",
                "34.746481,-92.289595,120mi",
                "38.581572,-121.4944,100mi",
                "39.739236,-104.990251,190mi",
                "41.763711,-72.685093,60mi",
                "39.158168,-75.524368,60mi",
                "28.5383350,-81.3792360,200mi",
                "33.748995,-84.387982,100mi",
                "21.306944,-157.858333,300mi",
                "43.61871,-116.214607,270mi",
                "39.781721,-89.650148,130mi",
                "41.343824581185686,-88.83819580078125,130mi",B
                "41.600545,-93.609106,120mi",
                "39.055824,-95.689018,120mi",
                "37.42252593456306,-84.605712890625,110mi",
                "30.135626231134612,-91.3897705078125,120mi",
                "44.78573392716592,-68.7799072265625,114mi",
                "39.279041894366785,-76.61041259765625,58mi",
                "42.35448465106744,-71.05133056640625,86mi",
                "42.732535,-84.555535,158mi",
                "44.953703,-93.089958,210mi",
                "32.298757,-90.18481,138mi",
                "38.796908303484294,-92.9827880859375,125mi",
                "47.040182144806664,-109.368896484375,218mi",
                "41.492120839687786,-99.415283203125,189mi",
                "39.33429742980725,-116.685791015625,253mi",
                '43.46002157809642,-71.60856485366821,48mi',
                "40.217053,-74.742938,45mi",
                "34.62716950197039,-106.06945753097534,230mi",
                "41.94314874732699,-75.3826904296875,121mi",
                "35.663711978252145,-78.9238715171814,120mi",
                "47.376615861813,-100.34326314926147,174mi",
                "39.961176,-82.998794,134mi",
                "35.46756,-97.516428,147mi",
                "43.93875961206275,-120.48643827438354,192mi",
                "41.370560930315676,-77.89707899093628,135mi",
                "41.65389996603372,-71.46509885787964,28mi",
                "33.65578083204097,-80.68359375,100mi",
                "44.0217676717761,-100.37261724472046,194mi",
                "35.93169895166453,-84.5621645450592,139mi",
                "30.267153,-97.743061,234mi",
                "39.568580293104645,-111.78118944168091,183mi",
                "44.260059,-72.575387,55mi",
                "37.540725,-77.436048,82mi",
                "47.39614140917534,-120.06629705429077,145mi",
                "38.39333888832238,-80.958251953125,135mi",
                "44.74673324024678,-89.45068359375,153mi",
                "42.96703768432213,-107.50094175338745,188mi"] 
                
StateArray   = ['Alabama',
                'Alaska',
                'Arizona',
                'Arkansas',
                'California',
                'Colorado',
                'Connecticut',
                'Delaware',
                'Florida',
                'Georgia',
                'Hawaii',
                'Idaho',
                'Illinois',
                'Indiana',
                'Iowa',
                'Kansas',
                'Kentucky',
                'Louisiana',
                'Maine',
                'Maryland',
                'Massachusetts',
                'Michigan',
                'Minnesota',
                'Mississippi',
                'Missouri',
                'Montana',
                'Nebraska',
                'Nevada',
                'New Hampshire',
                'New Jersey',
                "New Mexico",
                "New York",
                'North Carolina',
                'North Dakota',
                'Ohio',
                'Oklahoma',
                'Oregon',
                'Pennsylvania',
                'Rhode Island',
                'South Carolina',
                'South Dakota',
                'Tennessee',
                'Texas',
                'Utah',
                'Vermont',
                'Virginia',
                'Washington',
                'West Virginia',
                'Wisconsin',
                'Wyoming']
                
COUNT        = 100
tweets       = 0

CONSUMER_KEY        = 'INSERT HERE'
CONSUMER_SECRET     = 'INSERT HERE'
ACCESS_TOKEN_KEY    = 'INSERT HERE'
ACCESS_TOKEN_SECRET = 'INSERT HERE'

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

print('\n'                                                )
print('\n'                                                )
print('\n'                                                )
print('\n'                                                )
print('**************************************************')
print('DATA BELOW WAS CAPTURED: %s' %st                   ) 
print('**************************************************')
print('\n'                                                )
print('\n'                                                )
print('\n'                                                )
print('\n'                                                )

#INSERT TEXT FILE NAME IN THE SINGLE QUOTATIONS
csvfile1 = open('CANDIDATENAME_RESULTS_TWEET.txt','a')

csvfile1.write('\n'                                                )
csvfile1.write('\n'                                                )
csvfile1.write('\n'                                                )
csvfile1.write('\n'                                                )
csvfile1.write('**************************************************')
csvfile1.write('DATA BELOW WAS CAPTURED: %s' %st                   ) 
csvfile1.write('**************************************************')
csvfile1.write('\n'                                                )
csvfile1.write('\n'                                                )
csvfile1.write('\n'                                                )
csvfile1.write('\n'                                                )

for index in range(len(GeocodeArray)):

      print('\n'                                                      )
      print('**************************************************************************************************')
      print(str(SEARCH_TERM) + ' : ' + str(StateArray[index])         )
      print('**************************************************************************************************')
      print('\n'                                                      )

      r = api.request('search/tweets', {'q': SEARCH_TERM, 'geocode': GeocodeArray[index],'count': COUNT})
      c = 0
      n = 1
      
      csvfile1.write('\n'                                                      )
      csvfile1.write('*****************************************************************************************\n')
      csvfile1.write(str(SEARCH_TERM) + ' : ' + str(StateArray[index]) + '\n'  )
      csvfile1.write('*****************************************************************************************\n')
      csvfile1.write('\n'                                                      )

      for item in r.get_iterator():
            try:
               c += 1
               print c
               if 'text' in item:
                 text= item['text']
               if 'favorite_count' in item:
                 fav = item['favorite_count']
               if 'id' in item:
                 id1 = item['id']
               a = str(n)+'\t'+text.encode('utf-8')+'\t'+str(fav)+'\t'+str(id1)+ '\n'                   
               csvfile1.write(str(a))
               n += 1
               tweets += 1
            except UnicodeEncodeError:
               pass

print("Total Tweets Returned: %s" %tweets)

csvfile1.write('\n'                                   )
csvfile1.write("Total Tweets Returned: " + str(tweets))
csvfile1.write('\n'                                   )

csvfile1.close()
