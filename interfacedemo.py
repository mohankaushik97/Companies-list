import tkinter
from tkinter import ttk
# from tkcalendar import Calendar

def enter_data():
    # TODO: write code to use this
    print(Window.data())

class Window(tkinter.Tk):
    def __init__(self,*args,**kwargs) :
        tkinter.Tk.__init__(self,*args,**kwargs)
        self.title("Job applications")

        frame = tkinter.Frame(self)
        frame.pack()

        ### Companies info ###
        company_info_frame = tkinter.LabelFrame(frame,text= "Company info")
        company_info_frame.grid(row=0,column=0,padx=20,pady=10)

        ## Company name ##
        company_name_label = tkinter.Label(company_info_frame, text="Company name")
        company_name_label.grid(row=0,column=0)
        company_name_entry = tkinter.Entry(company_info_frame)
        company_name_entry.grid(row=1,column=0)


        # TODO: change the type to combobox
        ## Industry ##
        company_industry_label = tkinter.Label(company_info_frame,text="Company industry")
        company_industry_label.grid(row=0,column=1)
        company_industry_combobox = ttk.Combobox(company_info_frame,values=["Medical Device","Robotics"])
        company_industry_combobox.grid(row=1,column=1)

        ## Headquarters Location ##
        headquarters_label = tkinter.Label(company_info_frame,text="Headquarters Location")
        headquarters_label.grid(row=0,column=2)
        headquarters_entry = tkinter.Entry(company_info_frame)
        headquarters_entry.grid(row=1,column=2)

        ## Website ##
        website_label = tkinter.Label(company_info_frame,text="Company website")
        website_label.grid(row=2,column=0)
        website_entry = tkinter.Entry(company_info_frame)
        website_entry.grid(row=3,column=0)

        ## Company size ##
        company_size_label = tkinter.Label(company_info_frame,text="Company size")
        company_size_label.grid(row=2,column=1)
        company_size_entry = tkinter.Entry(company_info_frame)
        company_size_entry.grid(row=3,column=1)

        ## Company revenue ##
        company_revenue_label = tkinter.Label(company_info_frame,text="Company revenue")
        company_revenue_label.grid(row=2,column=2)
        company_revenue_entry = tkinter.Entry(company_info_frame)
        company_revenue_entry.grid(row=3,column=2)

        ### Role info ###
        role_info_frame = tkinter.LabelFrame(frame,text="Role information")
        role_info_frame.grid(row=1,column=0,padx=20,pady=10,sticky="news")

        ## Position Title ##
        position_title_label = tkinter.Label(role_info_frame,text="Position title")
        position_title_label.grid(row=0,column=0)
        position_title_entry = tkinter.Entry(role_info_frame)
        position_title_entry.grid(row=1,column=0)

        ## Job Location ##
        job_location_label = tkinter.Label(role_info_frame,text="Job Location")
        job_location_label.grid(row=0,column=1)
        job_location_entry = tkinter.Entry(role_info_frame)
        job_location_entry.grid(row=1,column=1)

        ## Department ##
        department_label = tkinter.Label(role_info_frame,text="Department")
        department_label.grid(row=0,column=2)
        department_entry = tkinter.Entry(role_info_frame)
        department_entry.grid(row=1,column=2)

        ## Job level ##
        # TODO: Combobox for job levels
        job_level_label = tkinter.Label(role_info_frame,text="Job Level")
        job_level_label.grid(row=2,column=0)
        job_level_entry = tkinter.Entry(role_info_frame)
        job_level_entry.grid(row=3,column=0)


        ## Job modality ##
        # TODO: combobox with primary/support 
        job_modality_label = tkinter.Label(role_info_frame,text="Job Modality")
        job_modality_label.grid(row=2,column=1)
        job_modality_entry = tkinter.Entry(role_info_frame)
        job_modality_entry.grid(row=3,column=1)

        ## Person of contact ## 
        poc_label = tkinter.Label(role_info_frame,text="Person of Contact")
        poc_label.grid(row=2,column=2)
        poc_entry = tkinter.Entry(role_info_frame)
        poc_entry.grid(row=3,column=2)


        ## Contact Origin ## 
        contact_origin_label = tkinter.Label(role_info_frame,text="Contact Origin")
        contact_origin_label.grid(row=4,column=0)
        contact_origin_entry = tkinter.Entry(role_info_frame)
        contact_origin_entry.grid(row=5,column=0)

        ## Contact detials ##
        # Linkedin/ email
        contact_details_label = tkinter.Label(role_info_frame,text="Contact Details")
        contact_details_label.grid(row=4,column=1)
        contact_details_entry = tkinter.Entry(role_info_frame)
        contact_details_entry.grid(row=5,column=1)

        ## Personal reference ## 
        personal_referral_label = tkinter.Label(role_info_frame,text="Referral Contact")
        personal_referral_label.grid(row=4,column=2)
        personal_referral_entry = tkinter.Entry(role_info_frame)
        personal_referral_entry.grid(row=5,column=2)

        ## Application date ## 
        application_date_label = tkinter.Label(role_info_frame,text="Application date")
        application_date_label.grid(row=6,column=0)
        application_date_entry = tkinter.Entry(role_info_frame)
        application_date_entry.grid(row=7,column=0)

        ## Application status ## 
        application_status_label = tkinter.Label(role_info_frame,text="Application status")
        application_status_label.grid(row=6,column=1)
        application_status_entry = tkinter.Entry(role_info_frame)
        application_status_entry.grid(row=7,column=1)

        for widget in company_info_frame.winfo_children():
            widget.grid_configure(padx=10,pady=5)


        for widget in role_info_frame.winfo_children():
            widget.grid_configure(padx=10,pady=5)


        button = tkinter.Button(frame,text="Enter Data",command=enter_data)
        button.grid(row=2,column=0,sticky="news",padx=40,pady=10)

        close_button = tkinter.Button(frame,text="Close",command=self.destroy)
        close_button.grid(row=3,column=0,sticky="news",padx=60,pady=10)

    def data() -> str:
        return "This data"


if __name__ == "__main__":
    testObj = Window()
    testObj.mainloop()
