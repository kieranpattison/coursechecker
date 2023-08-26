class Course:

    dept = ""
    code = ""
    sect = ""
    sess = ""
    year = ""
    url = ""

    def __init__(self, dept_, code_, sect_, sess_, year_):
        self.dept = dept_
        self.code = code_
        self.sect = sect_
        self.sess = sess_
        self.year = year_
        self.url = "https://courses.students.ubc.ca/cs/courseschedule?sesscd=" + sess_ + "&pname=subjarea&tname=subj-section&sessyr=" + year_ + "&course=" + code_ + "&section=" + sect_ + "&dept=" + dept_
