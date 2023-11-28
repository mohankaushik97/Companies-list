import sqlite3
import sys
sys.path.insert(0, 'D:\Companies list\ApplicationDatabase')
from Objects.company import Company
from Objects.role import Role



class Database():
    def __init__(self) -> None:
        # self.conn = sqlite3.connect(':memory:')
        self.create_tables()
        # comp_1 = Company()
        # self.insert_company(comp_1)
        # self.conn.close()

    def start_conn(self):
        # TODO: Change the connection when producing exe
        self.conn = sqlite3.connect('D:\Companies list\ApplicationDatabase\Database\database.db')
        # self.conn = sqlite3.connect('database.db')
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
                                "Website"	TEXT,
                                "Additional_info"   TEXT
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
                                "Poc_position"	TEXT,
                                "Application_date"	TEXT,
                                "Application_status"	TEXT,
                                "Application_result"    TEXT,
                                "Additional_info"   TEXT,
                                "Remarks"   TEXT,
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
                self.cursor.execute("""INSERT INTO companies(Name,Industry,City,State,Company_size,Revenue,Website,Additional_info)
                    VALUES (?,?,?,?,?,?,?,?)""",(company.name,company.industry,company.city,company.state,
                                                company.company_size,company.revenue,company.website,company.add_info))
        self.close_conn()

    def insert_role(self,role,company):
        companyId = self.get_companyId_by_name(company.name)
        # role = Role()
        self.start_conn()
        with self.conn:
            self.cursor.execute("""INSERT INTO roles(Company_ID,Title,Job_city,Job_state,Department,
                                Job_level,Job_module,Poc,Poc_origin,Poc_position,Application_date,
                                Application_status,Application_result,Additional_info,Remarks) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                (companyId,role.title,role.city,role.state,role.department,role.job_level,
                                 role.job_module,role.poc,role.poc_origin,role.poc_position,
                                 role.app_date,role.app_status,role.app_result,role.add_info,role.remarks))
        self.close_conn()

    def get_comp_data(self,name):
        self.start_conn()
        comp_name = name
        with self.conn:
            company = self.cursor.execute(""" SELECT companies WHERE name = {}
                                """.format(comp_name))
        print(company)
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
        print(company_id)
        self.close_conn()
        return company_id
    
    def get_comp_details_by_name(self,name):
        self.start_conn()
        self.cursor.execute("SELECT * FROM companies WHERE Name = '{}'".format(name))
        company = self.cursor.fetchone()
        print(company)
        comp = Company(*company) 
        self.close_conn()
        return comp
    
    def get_role_details(self,compName,roleTitle):
        self.start_conn()
        self.cursor.execute("SELECT Roles.* FROM Roles,Companies WHERE  Companies.Name LIKE '%{}%' AND roles.title LIKE '%{}%' AND Companies.ROWID = Roles.Company_ID".format(compName,roleTitle))
        role = self.cursor.fetchone()
        print(role)
        role = Role(*role)
        self.close_conn()
        return role
    
    def remove_company(self,company):
        self.start_conn()
        with self.conn:
            self.cursor.execute("DELETE from companies WHERE name=:name",{'name':company.name})

    def close_conn(self):
        self.conn.close()


if __name__ == "__main__":
    
    testObj = Database()
    company = testObj.get_comp_details_by_name("Tesla")
    role = testObj.get_role_details("VecTech","Mechatronics Engineer")
    print(role)