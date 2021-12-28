import sqlite3
from sqlite3.dbapi2 import SQLITE_READ

# Function to create table
connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
fill = "N/A"
def create_table():
    # Create a table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS poi
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        address TEXT,
        postcode TEXT,
        city TEXT,
        state TEXT,
        lattitude TEXT,
        longitude TEXT,
        phone TEXT,
        website TEXT)
        """)
#create_table()
dictionary = {
"poi1" : {
'name':"Sultan Salahuddin Abdul Aziz Shah Mosque",
'desc':"Large, iconic mosque with a blue stained glass dome",
'address':"Persiaran Masjid St., Sekysen 14",
'postcode':"48000",
'city':"Shah Alam",
'state':"Selangor",
'lat':"3.07873245",
'long':"101.52058387356396",
'phone':"+60355199988",
'website':"http://www.mssaas.gov.my/"
},
"poi2" : {
'name':"Aquaria KLCC",
'desc':"The Aquaria KLCC is said to be the world’s largest aquarium",
'address':"Kuala Lumpur Convention Centre, Jalan Pinang",
'postcode':"50088",
'city':"Kuala Lumpur",
'state':"Wilayah Persekutuan",
'lat':"3.1533436",
'long':"101.7130586",
'phone':"+60323331888",
'website':"https://aquariaklcc.com/"},
"poi3" : {
'name':"Putrajaya Wetlands Park",
'desc':"Large wetlands area suited for activities",
'address':"Putrajaya",
'postcode':"62000",
'city':"N/A",
'state':"N/A",
'lat':"2.9687176379342683",
'long':"101.69645925423791",
'phone':"+60388877774",
'website':"N/A"},
"poi4" : {
'name':"Pantai Hospital Penang, hospital, Bayan Lepas, Malaysia",
'desc':"Pantai Hospital Penang offers services in Radiotherapy & Oncology, Cardiology, Dentistry, Neurology, Neurosurgery and Cardiothoracic",
'address':"82, Jalan Tengah, Bandar Bayan Baru",
'postcode':"11900",
'city':"Bayan Lepas",
'state':"Pulau Pinang",
'lat':"5.3140215",
'long':"100.2822783477892",
'phone':"+6046433888",
'website':"N/A"},
"poi5" : {
'name':"Ibu Pejabat Jabatan Kerja Raya",
'desc':"To perform functions and powers relating to Federal roads (excluding highways) under the Road Transport Act 1987 [Act 333]",
'address':"Jalan Sultan Salahuddin, Kuala Lumpur",
'postcode':"50480",
'city':"Kuala Lumpur",
'state':"Wilayah Persekutuan",
'lat':" 3.15498925",
'long':"101.68904472528295",
'phone':"+60326108888",
'website':"https://www.jkr.gov.my/my"},
"poi6" : {
'name':"University Putra Malaysia",
'desc':fill,
'address':"JALAN UNIVERSITI 1 Serdang, Seri Kembangan, Selangor",
'postcode':"43400",
'city':"Seri Kembangan",
'state':"Selangor",
'lat':"2.9934443",
'long':"101.71498237937473",
'phone':"+60397691000",
'website':"http://www.upm.edu.my/"},
"poi7" : {
'name':"Taman Botani Negara Shah Alam",
'desc':"Botanical garden featuring activities such as cycling, fishing, swimming & an adventure park.",
'address':"Taman Pertanian Malaysia, Shah Alam, Selangor",
'postcode':"40170",
'city':"Taman Pertanian",
'state':"Selangor",
'lat':"3.0961469",
'long':"101.511053",
'phone':"+60355107048",
'website':fill},
"poi8" : {
'name':"Tanjung Harapan Lighthouse",
'desc':"Tanjung Harapan is a 2km  stretch of tree-lined shoreline bordering the Port Klang Golf Resort and is a calm oasis amid the bustling industrial estates and shipping terminals of the surrounding North Port of Port Klang.",
'address':"Kawasan Perindustrian Selat Klang Utara, Pelabuhan Klang, Selangor",
'postcode':"42000",
'city':"Pelabuhan Klang",
'state':"Selangor",
'lat':"3.000347402104452",
'long':"101.36515749786494",
'phone':fill,
'website':fill},
"poi9" : {
'name':"Shah Alam National Botanical Park",
'desc':"Large park featuring botanical gardens, bike rentals, a high ropes course & a swimming pool.",
'address':"Taman Botani Negara, Seksyen 8, Shah Alam, Selangor",
'postcode':"40000",
'city':"Taman Pertanian",
'state':"Selangor",
'lat':"3.096405448049363",
'long':"101.51124648291824",
'phone':"+60355106922",
'website':"http://www.tbnsa.gov.my/"},
"poi10" : {
'name':"Merdeka Square",
'desc':"",
'address':"Jalan Raja, City Centre, Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur",
'postcode':"43400",
'city':"Kuala Lumpur",
'state':"Wilayah Persekutuan",
'lat':"3.15366053250143",
'long':"101.68318748399469",
'phone':fill,
'website':fill},
"poi11" : {
'name':"Pantai Tanjung Rhu, Pulau Cayrey",
'desc':"Pulau Carey to be an island in that sense of the word, as the body of water separating it from the mainland is in fact a river called Sungai Langat",
'address':"Jalan Pulau Careyr",
'postcode':"42000 ",
'city':"Pulau Carey",
'state':"Selangor",
'lat':"2.8288634604938463",
'long':"101.3325388810682",
'phone':"+6033187282",
'website':"http://www.mpkl.gov.my/"},
"poi12" : {
'name':"National Science Centre",
'desc':"Science & learning center featuring interactive exhibits & play areas for young kids & toddlers",
'address':"Persiaran Bukit Kiara Bukit Damansara, Bukit Kiarar",
'postcode':"50662",
'city':"Kuala Lumpur",
'state':"Wilayah Persekutuan",
'lat':"3.165374210443637",
'long':"101.63881275357471",
'phone':"+60320893400",
'website':"http://www.psn.gov.my/"},
"poi13" : {
'name':"Batu Caves",
'desc':"Limestone caves at the top of steep steps housing Hindu temples & shrines, plus a huge deity statue",
'address':"Batu Caves",
'postcode':"68100",
'city':"Gombak",
'state':"Selangor",
'lat':"3.2407209672671846",
'long':"101.68206262274437",
'phone':"+60361896284",
'website':"http://www.tourism.gov.my/en/nl/web-page/places/states-of-malaysia/selangor/batu-caves"},
"poi14" : {
'name':"Templer Park",
'desc':"Templer Park (Malay: Hutan Lipur Templer) is a forest reserve in Rawang, Gombak District",
'address':"22, Jalan 3/2, Templer Height, Templer Park",
'postcode':"48000",
'city':"Rawang",
'state':"Selangor",
'lat':"3.298071554750647",
'long':"101.62214099155321",
'phone':"+60162038562",
'website':"http://www.tprr.net/"},
"poi15" : {
'name':"Colmar Tropicale, Berjaya Hills",
'desc':"Colmar Tropicale is a French-themed village and it is located 2,600 feet (790 m) above sea level on 80 acres (320,000 m2) of natural forestland. The development is inspired by the original town of Colmar in Alsace, France, with elements taken from ancient surrounding villages like Riquewihr, Turckheim and Kaysersberg as well",
'address':"KM 48 Persimpangan Bertingkat, Lebuhraya Karak,Bukit Tinggi",
'postcode':"28750",
'city':"Bentong",
'state':"Pahang",
'lat':"3.4425067160329705",
'long':"101.83.755259747413",
'phone':"+6092213666",
'website': fill },
"poi16" : {
'name':"Zoo Negara Malaysia",
'desc':"Open-concept zoo featuring a wide range of domestic & exotic animals, from elephants to seals.",
'address':"Jalan Taman Zooview, Taman Zooview, 68000 Ampang, Selangor",
'postcode':"68000",
'city':"Ampang",
'state':"Selangor",
'lat':"3.2964815122500757",
'long': "101.75296134430884",
'phone':"+60182331200",
'website':"https://www.zoonegaramalaysia.my/" },
"poi17" : {
'name':"Leaning Tower of Teluk Intan",
'desc':"This landmark clocktower built in 1885 is a national monument & notable because it leans southwest.",
'address':"Lot 1&2, Komplex Menara Condong, Jalan Bandar, Pekan Teluk Intan, Teluk Intan, Perak",
'postcode':"36000",
'city':"Teluk Intan",
'state':"Perak",
'lat':"4.130487929726782",
'long': "100.99900398935426",
'phone':"+60182331200",
'website':"http://www.mpti.gov.my/en/visitors/places-interest/menara-condong" },
"poi18" : {
'name':"Menara Taming Sari",
'desc':"This modern tower features a rotating observation deck that ascends to 80 meters",
'address':"Jalan Merdeka",
'postcode':"75000",
'city':"Bandar Hilir",
'state':"Malacca",
'lat':"2.3253730090122486",
'long': "102.25979121015592",
'phone':"+6062881100",
'website':"https://menaratamingsari.com/" },
"poi19" : {
'name':"Endau Rompin National Park",
'desc':"Sprawling national park in a tropical rainforest featuring hiking trails & rock formations",
'address':"Taman Negara",
'postcode':"86500",
'city':"Skudai",
'state':"Johor",
'lat':"2.490407568464232",
'long': "103.25978553700523",
'phone':" +6079222875 ",
'website':fill},
"poi20" : {
'name':"A Famosa",
'desc':"One of the top most historical place in malaysia",
'address':"Jalan Parameswara, Bandar Hilir, 78000 Alor Gajah, Melaka",
'postcode':"78000",
'city':"Alor Gajah",
'state':"Malacca",
'lat':"2.3050328769887014",
'long': "102.24910755184396",
'phone':fill,
'website':fill},
}

        #update_data ()
updatedict = {
#
"poi11" : {
'name':"Pantai Tanjung Rhu, Pulau Cayrey",
'desc':"Pantai's new description",
'address':"New address for pantai",
'postcode':"12345",
'city':"New city updation",
'state':"State is updated",
'lat':"newLat",
'long':"newLong",
'phone':"+234156766",
'website':"pantaiupdated.com"},
"poi10" : {
'name':"Merdeka Square",
'desc':"This landmark square has 96m flagpole to mark the site of the first Malayan flag raising",
'address':"Jalan Raja City Centre",
'postcode':"updated 43400",
'city':"updated kuala lumpur",
'state':"updated wilayah persekutuan",
'lat':"101.200100000",
'long':"250.04200100",
'phone':"+6035510980",
'website':"www.merdekasquare.com"},
"poi2" : {
'name':"Aquaria KLCC",
'desc':"Can see marrine animals",
'address':"Jalan Pinang",
'postcode':"60224",
'city':"Skudai",
'state':"Johor Bahru",
'lat':"3.5550000",
'long':"111.234566",
'phone':"+6034567890",
'website':"www.aquariaklcc.com"},
"poi13" : {
'name':"Batu Caves",
'desc':"Limestone caves at the top of steep steps housing Hindu temples",
'address':"Batu Caves Kuala Lumpur",
'postcode':"68400",
'city':"Selayang",
'state':"Pahang",
'lat':"3.4072096",
'long':"10.2062622",
'phone':"+60312345678",
'website':"www.batu-caves.com"},

"poi14" : {
'name':"Templer Park",
'desc':"Malay Hutan Lipur Templer",
'address':"36, Jalan 4/3, Templer Height, Taman Templer Park",
'postcode':"4400",
'city':"Alor Setar",
'state':"Kedah",
'lat':"2.54750647",
'long':"121.099155321",
'phone':"+603620385621",
'website':"wwww.templerpark.com"},

"poi16" : {
'name':"Zoo Negara Malaysia",
'desc':"Open-concept zoo featuring animals",
'address':"Jalan Taman Zoo Negara",
'postcode':"58000",
'city':"Sungai Petani",
'state':"Kedah",
'lat':"2.564800757",
'long': "234.34430884",
'phone':"+60102931250",
'website':"www.zoonegaramalaysia.com" },
}
counter = 1    
# Function to insert record
def insert_data (name, desc, address,postcode,city,state,lat,lon,phone,website):
    try:
        cursor.execute("""
            INSERT INTO poi(name,description,address,postcode,city,state,lattitude,longitude,phone,website)
            VALUES(?,?,?,?,?,?,?,?,?,?)""",(name,desc,address,postcode,city,state,lat,lon,phone,website))

        print("\nRecord successfully inserted!\n")

    except Exception as e:
        # If error, display error message (e)
        print("\n Unable to insert record.\n Error type:"+ str(e))

        # Rollback database transaction
        connection.rollback()

    # Save the database transaction
    connection.commit()

# Function to read records
connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()
def read_firstrow():
        connection = sqlite3.connect("mydatabase.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM poi WHERE id = ?""",(1,))
        data = cursor.fetchall()
        print('This is the collected data \n ')
        for i in data:
            for det in i:
                print(det)
        # for rows in data:                                                                
        #     print("{0} {1}\t {2}\t {3}\t {4}\t {5} {6}\t {7}\t {8}\t".format(rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8]))
def read_data():
    # Read data from the database
    counter = 1
    connection = sqlite3.connect("mydatabase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM poi")
    output = cursor.fetchall()
    print("\nNumber of record(s): " + str(len(output)) + "\n")
    for rows in output:
             print('This is Place of interest '+ str(counter))
             print(f'Name of is '+ rows[0])
             print(f'Description of {counter} row of is '+rows[1])
             print(f'Address of {counter} row is '+rows[2])
             print(f'Postcode of {counter} row is '+rows[3])
             print(f'City of {counter} row is '+rows[4])
             print(f'State of {counter} row is '+rows[5])
             print(f'Lat of {counter} row is '+rows[6])
             print(f'Long of {counter} row is '+rows[7])
             print(f'Phone of {counter} row is '+rows[8])
             print(f'Website of {counter} row is '+rows[9]) 
             counter+=1                                                 
        #print("{0}\t {1}\t {2}\t {3}\t {4}\t {5} {6}\t {7}\t {8}\t {9}\t".format(rows[0],rows[1],rows[2],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9]))
def update_data(name,desc,address,postcode,city,state,lat,lon,phone,website):
    cursor.execute("""SELECT name FROM poi WHERE name = ?""",(name,))
    name_from = cursor.fetchone()
    print(name_from)
    if name_from == None:
         print('/n Name does not exist '+name)
    else:
        try:
            cursor.execute("""UPDATE poi SET description ="%s", address ="%s", postcode ="%s", city ="%s", state ="%s", lattitude ="%s",longitude ="%s", phone ="%s", website ="%s" WHERE name ="%s" """ %(desc,address,postcode,city,state,lat,lon,phone,website,name))
            print("\nRecord succesfully inserted\n")
        except Exception as e:
          print("Unable to update the record, error type "+str(e))
          connection.rollback()
    
        connection.commit()

def delete_data():
    try:
        cursor.execute("""DELETE FROM poi""")
        print('Deleted all the data of the database')
    except Exception as e:
        # If error, display error message (e)
        print("\n Unable to insert record.\n Error type:"+ str(e))

        # Rollback database transaction
        connection.rollback()

    # Save the database transaction
    connection.commit()
def delete_two(name):
    try:
        cursor.execute("""DELETE FROM poi WHERE name = "%s" """ %(name))
        print('2 records deleted succesfully')
    except Exception as e:
        # If error, display error message (e)
        print("\n Unable to insert record.\n Error type:"+ str(e))

        # Rollback database transaction
        connection.rollback()

    # Save the database transaction
    connection.commit()


if __name__ == "__main__":
    

#Insert data to database
    for i in dictionary.values():
            name = i['name']
            desc = i['desc']
            address = i['address']
            postcode = i['postcode']
            city = i['city']
            state = i['state']
            lat = i['lat']
            long = i['long']
            phone = i['phone']
            website = i['website']
            counter += 1
            #Insert data function call
            #insert_data(name,desc,address,postcode,city,state,lat,long,phone,website)
    #delete two poi data
    deletedict = dict()
    deletedict['poi1'] = dictionary['poi19']
    deletedict['poi2'] = dictionary['poi20']
    for i in deletedict.values():
                name = i['name']
                #delete_two(name)
#--------------------------------------------------------------------------------------------      
   #Updates several poi data
    for i in updatedict.values():
             name = i['name']
             desc = i['desc']
             address = i['address']
             postcode = i['postcode']
             city = i['city']
             state = i['state']
             lat = i['lat']
             long = i['long']
             phone = i['phone']
             website = i['website']
             print('This is Place of interest '+ str(counter))
             print('Name is '+ name)
             print('Type of name '+str(type(name)))
             print('Desc is '+desc)
             print('Address is '+address)
             print('Postcode is '+postcode)
             print('City is '+city)
             print('State is '+state)
             print('Lat is '+lat)
             print('Long is '+long)
             print('Phone is '+phone)
             print('Website is '+website)
             #name,desc,address,postcode,city,state,lat,lon,phone,website
             #update function call
             #update_data(name,desc,address,postcode,city,state,lat,long,phone,website)
#--------------------------------------------------------------------------------------------------------------------------------
   # Delete all data from the table
delete_data()
   #Read first row of the table
    #read_firstrow()
   #Read all data from the table
    #read_data()