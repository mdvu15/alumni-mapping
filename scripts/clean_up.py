import psycopg2
from decimal import *
import psycopg2.extensions
from pygeolib import GeocoderError
from pygeocoder import Geocoder

not_valid_f = open('not_valid.csv', 'w')
out_file = open('clean.csv', 'w')

def clean(line, conn):
	x=0
	query=''
	address = line[1:4]
	address = [x for x in address if x is not None]
	id, city, state, zipc = line[0], line[4], line[5], line[6]
	addr = ' '.join(address).split(' ')
	while x < len(addr): 
		addr[x] = addr[x].replace('.','')
		if addr[x] in ["Apt", "PO", "Apartment"]:
			x+=2
		else:
			query += addr[x].rstrip('.') + ' '
			x+=1
	addr = query
	#out_file.write(str(id) + ',' + addr.rstrip(' ') + ',' + city + ',' + state + ',' + zipc.split('-')[0].rstrip('\n').lstrip('0') + '\n')
	out_file.write(str(id) + ',' + zipc.split('-')[0].rstrip('\n').lstrip('0') + '\n')
	
	
	# query += city + ', ' + state + ' ' + zipc.split('-')[0].rstrip('\n')
# 	print(str(query))
# 	valid, lati, longi = getLatLong(query)
# 	print(valid, lati, longi)
# 	if not valid:
# 		not_valid_f.write(str(id + ',' + query + ',' + city + ',' + state + ',' + zipc + ',' + str(longi) + ',' + str(lati)))
# 	else:
# 		writeToDB(conn, lati, longi, id, addr)

## get a cursor on the database
def getLatLong(query):
	try:
		results = Geocoder.geocode(query)
	except GeocoderError:
		print('couldn\'t find address')
	not_valid = []
	if results.valid_address:
		return(True, results.latitude, results.longitude)
	else:
		not_valid.append(query)
		return(False, results.latitude, results.longitude)
		
def writeToDB(conn, lat, long, id, addr):
	cursor = conn.cursor()
	try:
		cursor.execute(str("update clean_alums set address = '" + addr + "'," +
						"latitude = " + lat + 
						"longitude = "+ long + 
						" where alum_id = " + id + ";" ))
	except:
		print(cursor.statusmessage)
		print('count not update clean_alums table')
	

## main
try:
	conn = psycopg2.connect("dbname='buzzlightyear_db' user='buzzlightyear' password=''")
except:
	print('Unable to connect to database')
	exit(1)
	
cur = conn.cursor()
conn.set_session(readonly=False)
try:
	cur.execute(str("select alum_id, address_1, address_2, address_3, city" +
					", state, zipcode from alums;"))
except:
	print(cur.statusmessage)
	print('could not execute select from table alums')

rows = cur.fetchall()
cur.close()
for row in rows:
	clean(list(row), conn)
	
	

