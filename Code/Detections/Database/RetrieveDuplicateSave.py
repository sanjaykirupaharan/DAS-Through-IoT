import random
import pandas as pd
from datetime import datetime
import firebase_admin
from firebase_admin import db
from firebase_admin import firestore
from firebase_admin import credentials

# https://morioh.com/p/a593f973aff0

# Fetch the service account key JSON file contents
cred = credentials.Certificate('test-dataentry-firebase-adminsdk-xfc6m-b6b604539a.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-dataentry-default-rtdb.firebaseio.com/'
})


def average(dict, name):
    lat_list = dict['lat']
    lng_list = dict['lng']
    t_lat = 0
    t_lng = 0
    for j in range(len(lat_list)):
        t_lat += lat_list[j]
        t_lng += lng_list[j]
    sum_lat = t_lat / len(lat_list)
    sum_lng = t_lng / len(lng_list)
    avg_dict = {'lat': sum_lat, 'lng': sum_lng, 'name': name}
    return avg_dict


def SaveFirestore(dname, latvalue, lngvalue, sign):
    db = firestore.client()
    doc_ref = db.collection('coordinates').document(dname)
    doc_ref.set({
        u'lat': latvalue,
        u'lng': lngvalue,
        u'sign': sign
    })


temp_list = []
temp_main_list = []
main_dict = {}
final_dict = {}
sign_list = []
temp_dict = {'lat': 0, 'lng': 0, 'name': ''}
temp_lat = []
temp_lng = []
temp = []
i = 0
count = 0

# current date and time
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
date = date_time.split('/')
reference_name = '/{}_{}_{}'.format(date[0], date[1], date[2].split(',')[0])
doc_name = '{}_{}_{}-{}'.format(date[0], date[1], date[2].split(',')[0], date[2].split(',')[1].strip())

ref = db.reference('/11_02_2021')
# ref = db.reference(reference_name)

# Retrieve data dictonery from firebase real-time database
while True:
    doc = ref.get()
    for key, value in doc.items():
        field = ref.child(key).get()
        if field is None:
            break  # Break the loop when i goes out of the index

        else:
            main_dict = doc
    print("[INFO] Data retieved...")
    break

# print(main_dict)


while True:
    print(main_dict)
    if len(main_dict) <= 1:
        for key, value in main_dict.items():
            final_dict.update({count: value})
        print("[INFO] Main list out of index")
        break

    else:
        # print(len(main_list))
        for key, value in main_dict.items():
            sign_list.append(value['name'])
        for name in sign_list:
            for key, value in main_dict.items():
                if name == value['name']:
                    lat_min_val = float(value['lat']) - 0.00001
                    lat_max_val = float(value['lat']) + 0.00001
                    lng_min_val = float(value['lng']) - 0.00001
                    lng_max_val = float(value['lng']) + 0.00001

                    if lat_min_val <= float(value['lat']) <= lat_max_val or lng_min_val <= float(
                            value['lng']) <= lng_max_val:
                        temp_lat.append(float(value['lat']))
                        temp_lng.append(float(value['lng']))

                    else:
                        final_dict.update({count: value})
                        count += 1

                    temp_dict = {'lat': temp_lat, 'lng': temp_lng, 'name': value['name']}
                    avg_dict = average(temp_dict, name)
                    final_dict.update({count: avg_dict})

                    temp_dict = {'lat': 0, 'lng': 0, 'name': ''}
                    count = count + 1

        print("[INFO] Averaged...")
        break

print("final dic: ", final_dict)
coordinates = pd.DataFrame(data=final_dict).T
coordinates = coordinates.drop_duplicates(keep='first')
print("[INFO] Duplicated...")

it = 0
for index, row in coordinates.iterrows():
    SaveFirestore(str(index), row[0], row[1], row[2])
    it = it + 1
print("No of fields : ", it)
print("[INFO] Finished...")
