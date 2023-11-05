class Company:
    def __init__(self,name,industry,location,website="",company_size="",revenue=""):
        self.name = name
        self.industry = industry
        self.location = location
        self.website = website
        self.company_size = company_size
        self.revenue = revenue

    

    def __repr__(self):
        return "Company('{}','{}','{}')".format(self.name,self.industry,self.location)