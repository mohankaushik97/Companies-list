import sqlite3
from company import Company
from interfacedemo import Window

data_entry = Window()


conn = sqlite3.connect('companyDemo.db')

c = conn.cursor()

def create_first_table():
    # TODO: Only create the table if can't find one.
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS "Companies" (
	"Id"	INTEGER,
	"Name"	TEXT NOT NULL UNIQUE,
	"Industry"	TEXT,
	"Company_size"	TEXT,
	"Revenue"	TEXT,
	"Location"	TEXT,
	"Website"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
)""")
        c.execute("""CREATE TABLE IF NOT EXISTS "Roles" (
	"Id"	INTEGER,
	"Company_ID"	INTEGER,
	"Title"	TEXT,
	"Job_location"	TEXT,
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
        c.execute("""INSERT INTO companies(Name,Industry,Location,Company_size,Revenue,Website)
                   VALUES (?,?,?,?,?,?)""",(comp.name,comp.industry,comp.location,
                                            comp.company_size,comp.revenue,comp.website))

def update_company(comp):
    with conn:
        c.execute("""UPDATE companies SET revenue = :revenue WHERE name = :name""",
                  {'revenue':comp.revenue,'name':comp.name})

def get_company_by_location(location):
    c.execute("SELECT name,industry,location FROM companies WHERE location=:location",{'location': location})
    return c.fetchall()

def get_companyId_by_name(name):
    c.execute("SELECT id FROM companies WHERE name=:name",{'name': name})
    return c.fetchone()

def remove_company(comp):
    with conn:
        c.execute("DELETE from companies WHERE name=:name",{'name':comp.name})

comp_1 = Company('Tesla','Automotive','Fremont, CA')
comp_2 = Company('Lucid','Automotive','Tempe, AZ')

create_first_table()

# insert_company(comp_1)
# insert_company(comp_2)

companies = get_company_by_location('Tempe, AZ')
print(companies)

company_id = get_companyId_by_name('Lucid')[0]
print(company_id)

data_entry.mainloop()

conn.close()