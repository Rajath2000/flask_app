import sqlite3


def init_db():
    conn = sqlite3.connect("DepartmentSite.db")
    c = conn.cursor()
    conn.commit()
	# Create cocur Table
    c.execute('''CREATE TABLE IF NOT EXISTS CocurricularActivitie(SINO INTEGER PRIMARY KEY AUTOINCREMENT,USN TEXT,STUDENTNAME TEXT,NAMEOFACTIVITY TEXT,OrganizingInstituteORDepartment TEXT,ACTIVITYVENUE TEXT,AwardsORAchievements TEXT,Fillename TEXT,Filedata BLOP)''')
    conn.commit()
    #users table
    c.execute(
                """CREATE TABLE IF NOT EXISTS User(
                username TEXT PRIMARY KEY,
                pass TEXT,
                usertype TEXT
                );"""
        )
    conn.commit()
    #Extra curicuar activities table
    c.execute(
        """CREATE TABLE IF NOT EXISTS ExtracurricularActivities(
            SINO INTEGER PRIMARY KEY AUTOINCREMENT,
            USN TEXT,
            STUDENTNAME TEXT,
            NAMEOFACTIVITY TEXT,
            OrganizingInstituteORDepartment TEXT,
            ACTIVITYVENUE TEXT,
            AwardsORAchievements TEXT,
            Fillename TEXT,
            Filedata BLOP

        );"""
    )

    conn.commit()

    #Student Paper Publication in Journal
    c.execute("""CREATE TABLE IF NOT EXISTS StudentPaperPublicationinJournal(
            SINO INTEGER PRIMARY KEY AUTOINCREMENT,
            USN TEXT,
            STUDENTNAME TEXT,
            AuthorName TEXT,
            CoAuthor TEXT,
            NameofJournal TEXT,
            Title TEXT,
            Publisher TEXT,
            VolumeNumber TEXT,
            PageNumber TEXT,
            PublicationDate Date,
            Fillename TEXT,
            Filedata BLOP
    );""")
    conn.commit()

    c.execute("""CREATE TABLE IF NOT EXISTS StudentPaperPublicationinConferences(
            SINO INTEGER PRIMARY KEY AUTOINCREMENT,
            USN TEXT,
            STUDENTNAME TEXT,
            AuthorName TEXT,
            CoAuthor TEXT,
            NameofConferences TEXT,
            ConferenceVenue TEXT,
            Title TEXT,
            Publisher TEXT,
            VolumeNumber TEXT,
            PageNumber TEXT,
            PublicationDate Date,
            Fillename TEXT,
            Filedata BLOP);""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS MOOCCourseDetails(
            SINO INTEGER PRIMARY KEY AUTOINCREMENT,
            USN TEXT,
            STUDENTNAME TEXT,
            NameoftheCourse TEXT,
            CourseOfferedOrganization TEXT,
            ModeofWorkshop TEXT,
            startDate Date,
            endDate Date,
            NumberOfDays TEXT,
            Fillename TEXT,
            Filedata BLOP
            );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS Internships(
        SINO INTEGER PRIMARY KEY AUTOINCREMENT,
        USN TEXT,
        STUDENTNAME TEXT,
        Companyname TEXT,
        CompanyAdress TEXT,
        CompanyContactpersonName TEXT,
        CompanyContactpersonPhoneNumber TEXT,
        InternshipDomain TEXT,
        FromDate Date,
        ToDate Date,
        Duration TEXT,
        Fillename TEXT,
        Filedata BLOP
        );""")
    conn.commit()

    c.execute("""CREATE TABLE IF NOT EXISTS FpaperpublicationinJournal(
        SINO INTEGER PRIMARY KEY AUTOINCREMENT,
        FID TEXT,
        FACULTYNAME TEXT,
        AuthorName TEXT,
        CoAuthor TEXT,
        NameofJournal TEXT,
        Title TEXT,
        Publisher TEXT,
        VolumeNumber TEXT,
        PageNumber TEXT,
        PublicationDate Date,
        Fillename TEXT,
        Filedata BLOP
        );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS FpaperpublicationinConferences(
        SINO INTEGER PRIMARY KEY AUTOINCREMENT,
        FID TEXT,
        FACULTYNAME TEXT,
        AuthorName TEXT,
        CoAuthor TEXT,
        NameofConferences TEXT,
        ConferenceVenue TEXT,
        Title TEXT,
        Publisher TEXT,
        VolumeNumber TEXT,
        PageNumber TEXT,
        PublicationDate Date,
        Fillename TEXT,
        Filedata BLOP
        );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS BookChapterPublication(
        SINO INTEGER PRIMARY KEY AUTOINCREMENT,
        FID TEXT,
        FACULTYNAME TEXT,
        AuthorName TEXT,
        CoAuthor TEXT,
        BookChapterTitle TEXT,
        BookTitle TEXT,
        Publisher TEXT,
        PublicationDate Date,
        Fillename TEXT,
        Filedata BLOP
        );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS FMOOCCourseDetails(
            SINO INTEGER PRIMARY KEY AUTOINCREMENT,
            FID TEXT,
            FACULTYNAME TEXT,
            NameoftheCourse TEXT,
            CourseOfferedOrganization TEXT,
            ModeofWorkshop TEXT,
            startDate Date,
            endDate Date,
            NumberOfDays TEXT,
            Fillename TEXT,
            Filedata BLOP
            );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS FDP(
            SINO INTEGER PRIMARY KEY AUTOINCREMENT,
            FID TEXT,
            FACULTYNAME TEXT,
            NameofWorkshop TEXT,
            Venue TEXT,
            Organizer TEXT,
            ModeofWorkshop TEXT,
            startDate Date,
            endDate Date,
            NoDays TEXT,
            Fillename TEXT,
            Filedata BLOP
            );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS ProjectFundingorGrants(
            SINO INTEGER PRIMARY KEY AUTOINCREMENT,
            FID TEXT,
            FACULTYNAME TEXT,
            projectTitle TEXT,
            PrincipalInvestigator TEXT,
            CoPrincipalInvestigator TEXT,
            FundingAgency TEXT,
            AmountSanctioned TEXT,
            MonthandYearofFunding TEXT,
            ProjectDuration TEXT,
            Projectstatus TEXT,
            Fillename TEXT,
            Filedata BLOP
            );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS PatentORIPRDetails(
            SINO INTEGER PRIMARY KEY AUTOINCREMENT,
            FID TEXT,
            FACULTYNAME TEXT,
            Title TEXT,
            PatentReferenceNumber TEXT,
            Country TEXT,
            DateofFiling Date,
            DateofApproval Date,
            Fillename TEXT,
            Filedata BLOP
            );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS FacultyInnovationDetails(
        SINO INTEGER PRIMARY KEY AUTOINCREMENT,
        FID TEXT,
        FACULTYNAME TEXT,
        InnovationDetails TEXT,
        Fillename TEXT,
        Filedata BLOP
        );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS OtherAchivementsbyFaculty(
        SINO INTEGER PRIMARY KEY AUTOINCREMENT,
        FID TEXT,
        FACULTYNAME TEXT,
        DetailsOfAchivement TEXT,
        Fillename TEXT,
        Filedata BLOP
        );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS EventorActivityReports(
        SINO INTEGER PRIMARY KEY AUTOINCREMENT,
        EventName TEXT,
        EventDetails TEXT,
        ResourcePersonName TEXT,
        ResourcePersonAdress TEXT,
        EventDateTime TEXT,
        Venue TEXT,
        studentParticipantsCount TEXT,
        FacultyParticipantsCount TEXT,
        Cordinator TEXT,
        Fillename TEXT,
        Filedata BLOP
        );""")
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS FacultyDetails(
        FID TEXT PRIMARY KEY,
        FACULTYNAME TEXT,
        Degree TEXT,
        Univercity TEXT,
        Yearofcompletion TEXT,
        AssociationWithInstitution TEXT,
        Designation TEXT,
        DateOfDesignationasProffeser Date,
        DateofjoiningInstitution Date,
        Department TEXT,
        Specialization TEXT,
        ResearchPaperPublications TEXT,
        PhDGuidance TEXT,
        PhDReceivingyear TEXT,
        CurrentlyAssociated TEXT,
        NatureofAssociation TEXT
        );""")
    conn.commit()
    

    conn.close()


