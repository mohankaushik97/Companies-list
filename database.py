import sqlite3
from company import Company
from role import Role

class Database():
    def __init__(self) -> None:
        # self.conn = sqlite3.connect(':memory:')
        self.create_tables()
        # comp_1 = Company()
        # self.insert_company(comp_1)
        # self.conn.close()

    def start_conn(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        
    def create_tables(self):
        self.start_conn()
        with self.conn:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS "Companies" (
                                "Name"	TEXT NOT NULL UNIQUE,
                                "Industry"	TEXT,
                                "Company_size"	TEXT,
                                "Revenue"	TEXT,
                                "City"	TEXT,
                                "State" TEXT,
                                "Website"	TEXT
                            )""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS "Roles" (
                                "Company_ID"	INTEGER,
                                "Title"	TEXT,
                                "Job_city"	TEXT,
                                "Job_state" TEXT,
                                "Department"	TEXT,
                                "Job_level"	TEXT,
                                "Job_module"	TEXT,
                                "Poc"	TEXT,
                                "Poc_origin"	TEXT,
                                "Poc_details"	TEXT,
                                "Application_date"	TEXT,
                                "Application_status"	TEXT,
                                "Application_result"    TEXT,
                                FOREIGN KEY("Company_ID") REFERENCES "Companies"("rowid")
                            );""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Applications_overview AS SELECT 
                                Companies.Name, 
                                Roles.Title, 
                                Roles.Department,
                                Roles.Application_status, 
                                Roles.Application_result 
                                FROM Companies, Roles 
                                WHERE Roles.Company_ID = Companies.ROWID""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS App_complete AS SELECT Companies.Name, Roles.* 
                                FROM Companies,Roles WHERE Roles.Company_ID = Companies.ROWID""")

        self.close_conn()

    def insert_company(self,company):
    # TODO: make an if condition to prevent multiple entries of same company
        self.start_conn()
        value = self.is_company_present(company)
        if not value:
            with self.conn:
                self.cursor.execute("""INSERT INTO companies(Name,Industry,City,State,Company_size,Revenue,Website)
                    VALUES (?,?,?,?,?,?,?)""",(company.name,company.industry,company.city,company.state,
                                                company.company_size,company.revenue,company.website))
        self.close_conn()

    def insert_role(self,role,company):
        companyId = self.get_companyId_by_name(company.name)
        # role = Role()
        self.start_conn()
        with self.conn:
            self.cursor.execute("""INSERT INTO roles(Company_ID,Title,Job_city,Job_state,Department,
                                Job_level,Job_module,Poc,Poc_origin,Poc_details,Application_date,
                                Application_status,Application_result) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                (companyId,role.title,role.city,role.state,role.department,role.job_level,
                                 role.job_module,role.poc,role.poc_origin,role.poc_details,
                                 role.app_date,role.app_status,role.app_result))
        self.close_conn()

    def update_company(self,company):
        self.start_conn()
        with self.conn:
            self.cursor.execute("""UPDATE companies SET revenue = :revenue WHERE name = :name""",
                  {'revenue':company.revenue,'name':company.name})
        self.close_conn()

    def is_company_present(self,company):
        self.start_conn()
        self.cursor.execute("SELECT rowid FROM companies WHERE name=:name",{'name': company.name})
        if len(self.cursor.fetchall()) == 0:
            return False
        else:
            return True

    def get_company_by_state(self,state):
        self.start_conn()
        self.cursor.execute("SELECT name,industry,location FROM companies WHERE state=:state",{'state': state})
        companies = self.cursor.fetchall()
        self.close_conn()
        return companies
    
    def get_companyId_by_name(self,name):
        self.start_conn()
        self.cursor.execute("SELECT rowid FROM companies WHERE name=:name",{'name': name})
        company_id = self.cursor.fetchone()[0]
        self.close_conn()
        return company_id
    
    def remove_company(self,company):
        self.start_conn()
        with self.conn:
            self.cursor.execute("DELETE from companies WHERE name=:name",{'name':company.name})

    def close_conn(self):
        self.conn.close()


if __name__ == "__main__":
    testObj = Database()
    comp_1 = Company('Tesla','Automotive','Fremont, CA')
    testObj.insert_company(comp_1)
    testObj.close_conn()
