class Role:

    def __init__(self,title="",city="",state="",department="",
                 job_level="",job_module="",poc="",
                 contact_origin="",contact_details="",referral_contact="",
                 application_date="", application_status=""):
        
        self.title = title
        self.city = city
        self.state = state
        self.department = department
        self.job_level = job_level
        self.job_module = job_module
        self.poc = poc
        self.poc_origin = contact_origin
        self.poc_details = contact_details
        self.referral_contact = referral_contact
        self.app_date = application_date
        self.app_status = application_status        

    @property
    def location(self):
        return '{}, {}'.format(self.city, self.state)

    def __repr__(self) -> str:
        return "Role('{}','{}','{}')".format(self.title,self.app_date,self.app_status)