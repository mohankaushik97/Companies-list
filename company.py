class Company:
    def __init__(self,name="",industry="",state="", city="",website="",company_size="",revenue=""):
        self.name = name
        self.industry = industry
        self.city = city
        self.state = state
        self.website = website
        self.company_size = company_size
        self.revenue = revenue

    @property
    def location(self):
        return '{}, {}'.format(self.city, self.state)

    def __repr__(self):
        return "Company('{}','{}','{}')".format(self.name,self.industry,self.location)