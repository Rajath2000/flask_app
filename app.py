from flask import Flask, render_template ,request,redirect,url_for,jsonify,session,flash
from flask_wtf.file import FileField
from wtforms import SubmitField
from flask_wtf import Form
import sqlite3
import Database
app = Flask(__name__)
app.secret_key = "hello"

session = {"username":'',"role":''}


def signup(username,password):
    conn = sqlite3.connect("DepartmentSite.db")
    cur = conn.cursor()
    try:
        cur.execute("""INSERT INTO User(username, pass, usertype) 
					VALUES(?,?,?)""",(username,password,"U"))
        conn.commit()
        return True
    except Exception as err:
        return False
    finally:
        conn.close()
#login page
@app.route('/index.html',methods=['POST','GET'])
def index():
    if len(session['username'])==0:
        if request.method == 'POST':
            username=request.form['username']
            password=request.form['password']
            conn = sqlite3.connect("DepartmentSite.db")
            cur = conn.cursor()
            try:
                rows=cur.execute("""SELECT * FROM User WHERE username=(?) AND pass=(?)""",(username,password))
                rows=rows.fetchall()
                if(len(rows)==1 and rows[0][2]=='U'):
                    session['username']=username
                    session['role']=rows[0][2]
                    return redirect(url_for('Cocur'))
                elif(len(rows)==1 and rows[0][2]=='A'):
                    session['username']=username
                    session['role']=rows[0][2]
                    return render_template('',Username=username)
                else:
                    flash('Invalid username/password')  
                    return redirect(url_for('index')) 
            except Exception as err:
                print(err)
                return "<h1>{%err%}</h1>"
        else:
            return render_template('index.html')
    return redirect(url_for('Cocur'))

#signup page
@app.route('/Signup.html',methods=['POST','GET'])
def Signup():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        cpassword=request.form['cpassword']
        if(password!=cpassword):
            flash('password and confirm password doesnt match')
        else:
            if(signup(username, password)):
                return redirect(url_for('index'))
            else:
                flash('User Already exsists')
        return redirect(url_for('Signup'))
    else:
        return render_template('Signup.html')

#HomeUser
@app.route('/DashBoard.html',methods=['POST'])
def dashboard_user():
    if request.method == 'POST':
        return render_template('Dashboard.html',Username=session['username'])

#navigate
#student acivemets
#Co-curricular Activities
class UploadForm(Form):
    file = FileField()
    submit = SubmitField("submit")
    download = SubmitField("download")


    # form = UploadForm()
    # if form.validate_on_submit():
    #     file_name = form.file.data
    #     name=file_name.filename
    #     data=file_name.read()


@app.route('/Cocur.html',methods=['POST','GET'])
def Cocur():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            USN=request.form['USN']
            Name=request.form['Name']
            NameOfActivity=request.form['NameOfActivity']
            OrganizingInstitute=request.form['OrganizingInstitute']
            ActivityVenue=request.form['ActivityVenue']
            AwardsAchievements=request.form['AwardsAchievements']
            print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements)
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO CocurricularActivitie (USN,STUDENTNAME,NAMEOFACTIVITY,OrganizingInstituteORDepartment,ACTIVITYVENUE,AwardsORAchievements,Fillename,Filedata)VALUES(?,?,?,?,?,?,?,?)""",(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('Cocur'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('Cocur.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#ExtraCurricularActivities.html
@app.route('/ExtraCurricularActivities.html',methods=['POST','GET'])
def ExtraCurricularActivities():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            USN=request.form['USN']
            Name=request.form['Name']
            NameOfActivity=request.form['NameOfActivity']
            OrganizingInstitute=request.form['OrganizingInstitute']
            ActivityVenue=request.form['ActivityVenue']
            AwardsAchievements=request.form['AwardsAchievements']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO ExtracurricularActivities (USN,STUDENTNAME,NAMEOFACTIVITY,OrganizingInstituteORDepartment,ACTIVITYVENUE,AwardsORAchievements,Fillename,Filedata)VALUES(?,?,?,?,?,?,?,?)""",(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('ExtraCurricularActivities'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('ExtracurricularActivities.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#StudentPaperPublicationGen
@app.route('/StudentPaperPublicationGen.html',methods=['POST','GET'])
def StudentPaperPublicationGen():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            USN=request.form['USN']
            STUDENTNAME=request.form['Name']
            AuthorName=request.form['AuthorName']
            CoAuthor=request.form['Co-Author']
            NameofJournal=request.form['Journal']
            Title=request.form['Title']
            Publisher=request.form['Publisher']
            VolumeNumber=request.form['VolumeNumber']
            PageNumber=request.form['PageNumber']
            PublicationDate=request.form['Publication-Date']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO StudentPaperPublicationinJournal (
                        USN,
                        STUDENTNAME,
                        AuthorName,
                        CoAuthor,
                        NameofJournal,
                        Title,
                        Publisher,
                        VolumeNumber,
                        PageNumber,
                        PublicationDate,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",(USN,STUDENTNAME,AuthorName,CoAuthor,NameofJournal,Title,Publisher,VolumeNumber,PageNumber,PublicationDate,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('StudentPaperPublicationGen'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('StudentPaperPublicationGen.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#StudentPaperPublicationConference
@app.route('/StudentPaperPublicationConference.html',methods=['POST','GET'])
def StudentPaperPublicationConference():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            USN=request.form['USN']
            STUDENTNAME=request.form['Name']
            AuthorName=request.form['AuthorName']
            CoAuthor=request.form['Co-Author']
            NameofConferences=request.form['Conference']
            ConferenceVenue=request.form['Conference-Venue']
            Title=request.form['Title']
            Publisher=request.form['Publisher']
            VolumeNumber=request.form['VolumeNumber']
            PageNumber=request.form['PageNumber']
            PublicationDate=request.form['Publication-Date']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO StudentPaperPublicationinConferences (
                        USN,
                        STUDENTNAME,
                        AuthorName,
                        CoAuthor,
                        NameofConferences,
                        ConferenceVenue,
                        Title,
                        Publisher,
                        VolumeNumber,
                        PageNumber,
                        PublicationDate,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(USN,STUDENTNAME,AuthorName,CoAuthor,NameofConferences,ConferenceVenue,Title,Publisher,VolumeNumber,PageNumber,PublicationDate,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('StudentPaperPublicationConference'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('StudentPaperPublicationConference.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#MOOC Course Details(student)
@app.route('/Course.html',methods=['POST','GET'])
def Course():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            USN=request.form['USN']
            STUDENTNAME=request.form['Name']
            NameoftheCourse=request.form['name-of-Course']
            CourseOfferedOrganization=request.form['Course-Offered-Organization']
            ModeofWorkshop=request.form['Mode-of-Workshop']
            startDate=request.form['Start-Date']
            endDate=request.form['End-Date']
            NumberOfDays=request.form['No-of-Days']
            print(USN,STUDENTNAME,NameoftheCourse,CourseOfferedOrganization,ModeofWorkshop,startDate,endDate,NumberOfDays)
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO MOOCCourseDetails(
                        USN,
                        STUDENTNAME,
                        NameoftheCourse,
                        CourseOfferedOrganization,
                        ModeofWorkshop,
                        startDate,
                        endDate,
                        NumberOfDays,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?,?);""",(USN,STUDENTNAME,NameoftheCourse,CourseOfferedOrganization,ModeofWorkshop,startDate,endDate,NumberOfDays,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('Course'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('Course.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#Internship
@app.route('/Internship.html',methods=['POST','GET'])
def Internship():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            USN=request.form['USN']
            STUDENTNAME=request.form['Name']
            Companyname=request.form['Company-name']
            CompanyAdress=request.form['Company-Adress']
            CompanyContactpersonName=request.form['Person-name']
            CompanyContactpersonPhoneNumber=request.form['Phone']
            InternshipDomain=request.form['Internship-Domain']
            FromDate=request.form['Date-from']
            ToDate=request.form['Date-to']
            Duration=request.form['Duration']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO Internships(
                        USN,
                        STUDENTNAME,
                        Companyname,
                        CompanyAdress,
                        CompanyContactpersonName,
                        CompanyContactpersonPhoneNumber,
                        InternshipDomain,
                        FromDate,
                        ToDate,
                        Duration,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?,?,?,?);""",(USN,STUDENTNAME,Companyname,CompanyAdress,CompanyContactpersonName,CompanyContactpersonPhoneNumber,InternshipDomain,FromDate,ToDate,Duration,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('Internship'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('Internship.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#Faculty Achievement
#paperpublicationinJournal
@app.route('/paperpublicationinJournal.html',methods=['POST','GET'])
def paperpublicationinJournal():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['FName']
            AuthorName=request.form['AuthorName']
            CoAuthor=request.form['Co-Author']
            NameofJournal=request.form['Journal']
            Title=request.form['Title']
            Publisher=request.form['Publisher']
            VolumeNumber=request.form['VolumeNumber']
            PageNumber=request.form['PageNumber']
            PublicationDate=request.form['Publication-Date']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO FpaperpublicationinJournal(
                        FID,
                        FACULTYNAME,
                        AuthorName,
                        CoAuthor,
                        NameofJournal,
                        Title,
                        Publisher,
                        VolumeNumber,
                        PageNumber,
                        PublicationDate,
                        Fillename,
                    Filedata)VALUES(?,?,?,?,?,?,?,?,?,?,?,?);""",(FID,FACULTYNAME,AuthorName,CoAuthor,NameofJournal,Title,Publisher,VolumeNumber,PageNumber,PublicationDate,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('paperpublicationinJournal'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('paperpublicationinJournal.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))


    
#paperpublicationinConferences
@app.route('/paperpublicationinConferences.html',methods=['POST','GET'])
def paperpublicationinConferences():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['FName']
            AuthorName=request.form['AuthorName']
            CoAuthor=request.form['Co-Author']
            NameofConferences=request.form['Conference']
            ConferenceVenue=request.form['Conference-Venue']
            Title=request.form['Title']
            Publisher=request.form['Publisher']
            VolumeNumber=request.form['VolumeNumber']
            PageNumber=request.form['PageNumber']
            PublicationDate=request.form['Publication-Date']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO FpaperpublicationinConferences (
                        FID,
                        FACULTYNAME,
                        AuthorName,
                        CoAuthor,
                        NameofConferences,
                        ConferenceVenue,
                        Title,
                        Publisher,
                        VolumeNumber,
                        PageNumber,
                        PublicationDate,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(FID,FACULTYNAME,AuthorName,CoAuthor,NameofConferences,ConferenceVenue,Title,Publisher,VolumeNumber,PageNumber,PublicationDate,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('paperpublicationinConferences'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('paperpublicationinConferences.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#BookChapterPublication
@app.route('/BookChapterPublication.html',methods=['POST','GET'])
def BookChapterPublication():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['FName']
            AuthorName=request.form['AuthorName']
            CoAuthor=request.form['Co-Author']
            BookChapterTitle=request.form['Book-Chapter-Title']
            BookTitle=request.form['Book-Title']
            Publisher=request.form['Publisher']
            PublicationDate=request.form['Publication-Date']
           
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO BookChapterPublication (
                        FID,FACULTYNAME,AuthorName,CoAuthor,BookChapterTitle,BookTitle,Publisher,PublicationDate,Fillename,Filedata)
                        VALUES(?,?,?,?,?,?,?,?,?,?)""",(FID,FACULTYNAME,AuthorName,CoAuthor,BookChapterTitle,BookTitle,Publisher,PublicationDate,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('BookChapterPublication'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('BookChapterPublication.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#MoocCourseDetais
@app.route('/MoocCourseDetais.html',methods=['POST','GET'])
def MoocCourseDetais():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['FName']
            NameoftheCourse=request.form['name-of-Course']
            CourseOfferedOrganization=request.form['Course-Offered-Organization']
            ModeofWorkshop=request.form['Mode-of-Workshop']
            startDate=request.form['Start-Date']
            endDate=request.form['End-Date']
            NumberOfDays=request.form['No-of-Days']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO FMOOCCourseDetails(
                        FID,
                        FACULTYNAME,
                        NameoftheCourse,
                        CourseOfferedOrganization,
                        ModeofWorkshop,
                        startDate,
                        endDate,
                        NumberOfDays,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?,?);""",(FID,FACULTYNAME,NameoftheCourse,CourseOfferedOrganization,ModeofWorkshop,startDate,endDate,NumberOfDays,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('MoocCourseDetais'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('MoocCourseDetais.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#FDP
@app.route('/FDP.html',methods=['POST','GET'])
def FDP():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['FName']
            NameofWorkshop=request.form['name-of-FDP']
            Venue=request.form['Venue']
            Organizer=request.form['Organizer']
            ModeofWorkshop=request.form['Mode-of-Workshop']
            startDate=request.form['Start-Date']
            endDate=request.form['End-Date']
            NumberOfDays=request.form['No-of-Days']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO FDP(
                        FID,
                        FACULTYNAME,
                        NameofWorkshop,
                        Venue,
                        Organizer,
                        ModeofWorkshop,
                        startDate,
                        endDate,
                        NoDays,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?,?,?);""",(FID,FACULTYNAME,NameofWorkshop,Venue,Organizer,ModeofWorkshop,startDate,endDate,NumberOfDays,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('FDP'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('FDP.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#ProjectFunding
@app.route('/ProjectFunding.html',methods=['POST','GET'])
def ProjectFunding():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['FName']
            projectTitle=request.form['Project-Title']
            PrincipalInvestigator=request.form['Principal-Investigator']
            CoPrincipalInvestigator=request.form['Co-Principal-Investigator']
            FundingAgency=request.form['Funding-Agency']
            AmountSanctioned=request.form['Amount-Sanctioned']
            MonthandYearofFunding=request.form['Funding-Day']
            ProjectDuration=request.form['project-duration']
            Projectstatus=request.form['Project-status']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO ProjectFundingorGrants(
                        FID,
                        FACULTYNAME,
                        projectTitle,
                        PrincipalInvestigator,
                        CoPrincipalInvestigator,
                        FundingAgency,
                        AmountSanctioned,
                        MonthandYearofFunding,
                        ProjectDuration,
                        Projectstatus,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?,?,?,?);""",(FID,FACULTYNAME,projectTitle,PrincipalInvestigator,CoPrincipalInvestigator,FundingAgency,AmountSanctioned,MonthandYearofFunding,ProjectDuration,Projectstatus,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('ProjectFunding'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('ProjectFunding.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#patent
@app.route('/patent.html',methods=['POST','GET'])
def patent():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['FName']
            Title=request.form['Title']
            PatentReferenceNumber=request.form['Patent-Reference-Number']
            Country=request.form['country']
            DateofFiling=request.form['Date-of-Filing']
            DateofApproval=request.form['Date-of-Approval']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO PatentORIPRDetails(
                        FID,
                        FACULTYNAME,
                        Title,
                        PatentReferenceNumber,
                        Country,
                        DateofFiling,
                        DateofApproval,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?);""",(FID,FACULTYNAME,Title,PatentReferenceNumber,Country,DateofFiling,DateofApproval,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('patent'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('patent.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))


#FID
@app.route('/FID.html',methods=['POST','GET'])
def FID():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['FName']
            InnovationDetails=request.form['Details']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO FacultyInnovationDetails(
                        FID,
                        FACULTYNAME,
                        InnovationDetails,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?);""",(FID,FACULTYNAME,InnovationDetails,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('FID'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('FID.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))


#otherachivementsbyFacuty
@app.route('/otherachivementsbyFacuty.html',methods=['POST','GET'])
def otherachivementsbyFacuty():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['FName']
            DetailsOfAchivement=request.form['Details']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO OtherAchivementsbyFaculty(
                        FID,
                        FACULTYNAME,
                        DetailsOfAchivement,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?);""",(FID,FACULTYNAME,DetailsOfAchivement,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('otherachivementsbyFacuty'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('otherachivementsbyFacuty.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#EventActivityReports
@app.route('/EventActivityReports.html',methods=['POST','GET'])
def EventActivityReports():
    if len(session['username'])!=0:
        form = UploadForm()
        if request.method == 'POST':
            EventName=request.form['Event-name']
            EventDetails=request.form['EDetails']
            ResourcePersonName=request.form['Resource-pname']
            ResourcePersonAdress=request.form['Resource-Address']
            EventDateTime=request.form['Date-Time']
            Venue=request.form['Event-Venue']
            studentParticipantsCount=request.form['No-Student']
            FacultyParticipantsCount=request.form['No-Faculty']
            Cordinator=request.form['Coordinator']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            if form.validate_on_submit():
                file_name = form.file.data
                name=file_name.filename
                data=file_name.read()
                conn=sqlite3.connect("DepartmentSite.db")
                cur=conn.cursor()
                try:
                    cur.execute("""INSERT INTO EventorActivityReports(
                        EventName,
                        EventDetails,
                        ResourcePersonName,
                        ResourcePersonAdress,
                        EventDateTime,
                        Venue,
                        studentParticipantsCount,
                        FacultyParticipantsCount,
                        Cordinator,
                        Fillename,
                        Filedata)VALUES(?,?,?,?,?,?,?,?,?,?,?);""",(EventName,EventDetails,ResourcePersonName,ResourcePersonAdress,EventDateTime,Venue,studentParticipantsCount,FacultyParticipantsCount,Cordinator,name,data))
                    conn.commit()
                    conn.close()
                    flash("Added to DataBase")
                except Exception as err:
                    print(err)
                return redirect(url_for('EventActivityReports'))
            # return render_template("Cocur.html", form=form,Username=session['username'])
        return render_template('EventActivityReports.html',Username=session['username'],form=form)
    else:
        return redirect(url_for('index'))

#FD
@app.route('/FD.html',methods=['POST','GET'])
def FD():
    if len(session['username'])!=0:
        if request.method == 'POST':
            FID=request.form['FID']
            FACULTYNAME=request.form['Name-of-Faculty']
            Degree=request.form['Degree']
            Univercity=request.form['Univercity']
            Yearofcompletion=request.form['Year-of-completion']
            AssociationWithInstitution=request.form['Association']
            Designation=request.form['Designation']
            DateOfDesignationasProffeser=request.form['Date-Designated-As-Proffeser']
            DateofjoiningInstitution=request.form['Date-joining-Institution']
            Department=request.form['Department']
            Specialization=request.form['Specialization']
            ResearchPaperPublications=request.form['Research-Paper-Publications']
            PhDGuidance=request.form['Guidance']
            PhDReceivingyear=request.form['Ph-D-Receiving-year']
            CurrentlyAssociated=request.form['Currently-Associated']
            NatureofAssociation=request.form['Nature-of-Association']
            # print(USN,Name,NameOfActivity,OrganizingInstitute,ActivityVenue,AwardsAchievements,name,data)
            # return render_template("Cocur.html", form=form,Username=session['username'])
            conn=sqlite3.connect("DepartmentSite.db")
            cur=conn.cursor()
            try:
                cur.execute("""INSERT INTO FacultyDetails(
                FID,
                FACULTYNAME,
                Degree,
                Univercity,
                Yearofcompletion,
                AssociationWithInstitution,
                Designation,
                DateOfDesignationasProffeser,
                DateofjoiningInstitution,
                Department,
                Specialization,
                ResearchPaperPublications,
                PhDGuidance,
                PhDReceivingyear,
                CurrentlyAssociated,
                NatureofAssociation
                )VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(FID,FACULTYNAME,Degree,Univercity,Yearofcompletion,AssociationWithInstitution,Designation,DateOfDesignationasProffeser,DateofjoiningInstitution,Department,Specialization,ResearchPaperPublications,PhDGuidance,PhDReceivingyear,CurrentlyAssociated,NatureofAssociation))
                conn.commit()
                conn.close()
                flash("Added to DataBase")
            except Exception as err:
                print(err)
            return redirect(url_for('FD'))
        return render_template('FD.html',Username=session['username'])
    else:
        return redirect(url_for('index'))


@app.route('/logout.html')
def logout():
    session['username']=''
    return redirect(url_for('index'))

# UPLOAD_FOLDER = '../public/uploads'
# app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# def allowed_file(filename):
#     	return '.' in filename and \
# 		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
# @app.route('/test.html',methods=['POST','GET'])
# def test():
#     if request.method == 'POST':
#         file=request.files['file']
#         if(file and allowed_file(file.filename)):
#             filename=secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             conn = sqlite3.connect("files.db")
#             cur = conn.cursor()
#             k=[filename]
            
#             cur.execute("INSERT INTO files VALUES(?)",tuple(k))
#             conn.commit()
#             conn.close()
#         return redirect(url_for('test'))
#     else:
#         return render_template('test.html')




# @app.route('/upload.html',methods=['POST','GET'])
# def upload():
#     form = UploadForm()
#     # if request.method == "POST":
#         if form.validate_on_submit():
#             file_name = form.file.data
#             conn= sqlite3.connect("files.db")
#             cursor = conn.cursor()
#             cursor.execute("""INSERT INTO my_table (name, data) VALUES (?,?) """,(file_name.filename,file_name.read()))
#             conn.commit()
#             cursor.close()
#             conn.close()
#             return render_template("upload.html", form=form)

#     return render_template("upload.html", form=form)

if __name__ == '__main__':
    Database.init_db()
    app.run(debug=True)