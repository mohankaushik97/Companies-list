class Role:

    def __init__(self,id ="",title="",city="",state="",department="",
                 job_level="",job_module="",poc="",
                 contact_origin="",contact_position="",
                 application_date="", application_status="", application_result="",add_info="",remarks=""):
        
        self.comp_id = id
        self.title = title
        self.city = city
        self.state = state
        self.department = department
        self.job_level = job_level
        self.job_module = job_module
        self.poc = poc
        self.poc_origin = contact_origin
        self.poc_position = contact_position
        self.app_date = application_date
        self.app_status = application_status
        self.app_result = application_result
        self.add_info = add_info
        self.remarks = remarks

    @property
    def location(self):
        return '{}, {}'.format(self.city, self.state)

    def __repr__(self) -> str:
        return "Role('{}','{}','{}')".format(self.title,self.app_date,self.app_status)