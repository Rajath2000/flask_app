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