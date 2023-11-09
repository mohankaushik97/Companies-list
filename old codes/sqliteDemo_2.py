import sqlite3
# from company import Company

class Sqlite():
    def __init__(self):
        super().__init__()  
        self.conn = sqlite3.connect('ApplicationsDemo.db')
        self.cursor = self.conn.cursor()
    
	def create_first_table():
		# TODO: Only create the table if can't find one.
		with self.conn:
			self.cursor.execute("""CREATE TABLE IF NOT EXISTS "Companies" (
		"Id"	INTEGER,
		"Name"	TEXT NOT NULL UNIQUE,
		"Industry"	TEXT,
		"Company_size"	TEXT,
		"Revenue"	TEXT,
		"City"	TEXT,
		"State" TEXT,
		"Website"	TEXT,
		PRIMARY KEY("Id" AUTOINCREMENT)
	)""")
			self.cursor.execute("""CREATE TABLE IF NOT EXISTS "Roles" (
		"Id"	INTEGER,
		"Company_ID"	INTEGER,
		"Title"	TEXT,
		"Job_city"	TEXT,
		"Job_state" TEXT,
		"Department"	TEXT,
		"Job_level"	TEXT,
		"Job_module"	TEXT,
		"PoC"	TEXT,
		"Contact_origin"	TEXT,
		"Contact_details"	TEXT,
		"referral_contact"	TEXT,
		"Application_date"	BLOB,
		"Application_status"	TEXT,
		PRIMARY KEY("Id" AUTOINCREMENT),
		FOREIGN KEY("Company_ID") REFERENCES "Companies"("Id")
	);""")

def insert_company(comp):
    # TODO: make an if condition to prevent multiple entries of same company
    with conn:
        self.cursor.execute("""INSERT INTO companies(Name,Industry,City,State,Company_size,Revenue,Website)
                   VALUES (?,?,?,?,?,?)""",(comp.name,comp.industry,comp.city,comp.state,
                                            comp.company_size,comp.revenue,comp.website))

def update_company(comp):
    with conn:
        self.cursor.execute("""UPDATE companies SET revenue = :revenue WHERE name = :name""",
                  {'revenue':comp.revenue,'name':comp.name})

def get_company_by_location(location):
    self.cursor.execute("SELECT name,industry,location FROM companies WHERE location=:location",{'location': location})
    return self.cursor.fetchall()

def get_companyId_by_name(name):
    self.cursor.execute("SELECT id FROM companies WHERE name=:name",{'name': name})
    return self.cursor.fetchone()

def remove_company(comp):
    with conn:
        self.cursor.execute("DELETE from companies WHERE name=:name",{'name':comp.name})

# comp_1 = Company('Tesla','Automotive','Fremont, CA')
# comp_2 = Company('Lucid','Automotive','Tempe, AZ')

create_first_table()

# insert_company(comp_1)
# insert_company(comp_2)

# companies = get_company_by_location('Tempe, AZ')
# print(companies)

# company_id = get_companyId_by_name('Lucid')[0]
# print(company_id)


conn.close()