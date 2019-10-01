for college in college_data[4649:]:
    import requests
    from lxml import html
    url = 'https://nces.ed.gov/collegenavigator/?id='+str(college['unitid'])+'#general'
    #url = 'https://nces.ed.gov/collegenavigator/?id=144892#general'
    #url = 'https://nces.ed.gov/collegenavigator/?id=102058#general'
    pageContent = requests.get(url)
    tree = html.fromstring(pageContent.content)

    ##SAT SCORE
    ##/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[12]/div[1]/div[2]/div[1]/table[4]/tbody[1]/tr[1]/td[2]
    sat_score = tree.xpath("//div[@id='admsns']//tr[11]//td[2]/text()")
    print("sat score", sat_score)
    ##UNDERGRADUATE ADMISSIONS FALL 2018
    #/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[12]/div[1]/div[2]/div[1]/table[2]/thead[1]/tr[1]/th[2]
    inst_name = tree.xpath("//span[@class='headerlg']/text()")
    if not inst_name:
        print(college['unitid'])
        continue

    ##Undergraduate enrollment
    total_number_enrolled = tree.xpath("//div[@id='enrolmt']//table[1]//tbody[1]//tr[1]//td[2]/text()")
    print("undergraduate enrollment", total_number_enrolled)
    if total_number_enrolled:
        college['total_number_enrolled'] = total_number_enrolled[0]
    ##Admissions
        ##No of applicants
    try:
        under_graduate = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[1]/text()")
        print("in under graduate")
        #print(under_graduate)
        ug = 'Undergraduate application fee (2018-2019): '
        under_graduate_test = [k for k in under_graduate if ug in k]
        #print("test", under_graduate_test)
        college['admit_data'] = {}
        college['enrolled_from_admit_data'] = {}
        if not under_graduate_test:
            a = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[1]/text()")
            total_number_of_applicants = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[2]/text()")
            total_number_of_male_applicants = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[3]/text()")
            total_number_of_female_applicants = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[4]/text()")

            print("no of applicants")
            print(total_number_of_applicants, total_number_of_male_applicants,total_number_of_female_applicants)

            college['admit_data']['total_number_of_applicants'] = total_number_of_applicants[0]
            college['admit_data']['total_number_of_male_applicants'] = total_number_of_male_applicants[0]
            college['admit_data']['total_number_of_female_applicants'] = total_number_of_female_applicants[0]
            ##percent admitted
            b = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[2]//td[1]/text()")
            percent_admitted_total = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[2]//td[2]/text()")
            percent_male_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[2]//td[3]/text()")
            percent_female_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[2]//td[4]/text()")
            print(percent_admitted_total,percent_male_admitted,percent_female_admitted)
            college['admit_data']['percent_admitted_total'] = percent_admitted_total[0]
            college['admit_data']['percent_admitted_male'] = percent_male_admitted[0]
            college['admit_data']['percent_admitted_female'] = percent_female_admitted[0]
            ##percent admitted who enrolled
            c = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[1]/text()")
            percent_admitted_enrolled_total = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[2]/text()")
            percent_male_enrolled_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[3]/text()")
            percent_female_enrolled_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[4]/text()")
            print(percent_admitted_enrolled_total,percent_male_enrolled_admitted,percent_female_enrolled_admitted)
            college['enrolled_from_admit_data']['percent_admitted_enrolled_total'] = percent_admitted_enrolled_total[0]
            college['enrolled_from_admit_data']['percent_enrolled_admitted_male'] = percent_male_enrolled_admitted[0]
            college['enrolled_from_admit_data']['percent_enrolled_admitted_female'] = percent_female_enrolled_admitted[0]
        else:
            ##under_graduate not present
            #//div[@id='admsns']//table[3]//tbody[1]//tr[1]//td[2]
            print("in else")
            a = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[1]/text()")
            total_number_of_applicants = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[2]/text()")
            total_number_of_male_applicants = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[3]/text()")
            total_number_of_female_applicants = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[4]/text()")

            print("no of applicants")
            print(total_number_of_applicants, total_number_of_male_applicants,total_number_of_female_applicants)
            college['admit_data']['total_number_of_applicants'] = total_number_of_applicants[0]
            college['admit_data']['total_number_of_male_applicants'] = total_number_of_male_applicants[0]
            college['admit_data']['total_number_of_female_applicants'] = total_number_of_female_applicants[0]

            ##percent admitted
            b = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[1]/text()")
            percent_admitted_total = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[2]/text()")
            percent_male_admitted = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[3]/text()")
            percent_female_admitted = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[4]/text()")
            print(percent_admitted_total,percent_male_admitted,percent_female_admitted)
            college['admit_data']['percent_admitted_total'] = percent_admitted_total[0]
            college['admit_data']['percent_admitted_male'] = percent_male_admitted[0]
            college['admit_data']['percent_admitted_female'] = percent_female_admitted[0]
            ##percent admitted who enrolled
            c = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[1]/text()")
            percent_admitted_enrolled_total = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[2]/text()")
            percent_male_enrolled_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[3]/text()")
            percent_female_enrolled_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[4]/text()")
            print(percent_admitted_enrolled_total,percent_male_enrolled_admitted,percent_female_enrolled_admitted)
            college['enrolled_from_admit_data']['percent_admitted_enrolled_total'] = percent_admitted_enrolled_total[0]
            college['enrolled_from_admit_data']['percent_enrolled_admitted_male'] = percent_male_enrolled_admitted[0]
            college['enrolled_from_admit_data']['percent_enrolled_admitted_female'] = percent_female_enrolled_admitted[0]
    except Exception as e:
        print(e)
        pass
    ## Enrollment by Gender
    enc = tree.xpath("//table[2]//tbody[1]//tr[1]//td[2]//img[1]/@alt")
    data = None
    if enc:
        enc = enc[0]
        #print(enc)
        data = enc.split('\r\n')
        #print("enc")
        print(data)
    else:
        print("No enc found")
    #male_percentage = data[3]
    #female_percerntage = data[5]
    #print(male_percentage, female_percerntage)
    college['enrollment_by_gender']  = {}
    college['enrollment_by_gender']['male_enrolled_percent'] = data[1].split(":")[1] if data else None
    college['enrollment_by_gender']['female_enrolled_percent'] = data[2].split(":")[1] if data else None
    ## Enrollment by Race/Ethnicity
    race = tree.xpath("//div[@id='enrolmt']//table[3]//tbody[1]//tr[1]//td[1]//img[1]/@alt")
    #print(race)
    if race:
        race = race[0]
        race_data = race.split('\r\n')
        enrollment_by_race={}
        for i in race_data:
            data = i.split(':')
            if data:
                for j in range(1):
                    enrollment_by_race[data[j]] = data[j+1]
        print(enrollment_by_race)
        college.update({"enrollment_by_race":enrollment_by_race})
    ##Enrollment by Age
    age = tree.xpath("//div[@id='enrolmt']//table[4]//tbody[1]//tr[1]//td[1]//img[1]/@alt")
    if age:
        age = age[0]
        age_data = age.split('\r\n')
        age_dict={}
        for i in age_data:
            data = i.split(':')
            if data:
                for j in range(1):
                    age_dict[data[j]] = data[j+1]
        college.update({"enrollment_by_age":age_dict})
    ##VARSITY ATHLETIC TEAMS

    #all_track = tree.xpath("//td[contains(text(),'All Track Combined')]/text()")
    #print(all_track)
    all_track_dict = {}
    #for i in range(1,4):
    try:
        for j in range(1,12):
            #print(i,j)
            type_of_sport = tree.xpath("//div[@id='sports']//tr[{}]//td[1]/text()".format(j))
            male = tree.xpath("//div[@id='sports']//tr[{}]//td[2]/text()".format(j))
            female = tree.xpath("//div[@id='sports']//tr[{}]//td[3]/text()".format(j))
            all_track_dict.update({str(type_of_sport[0]) :  {"male": male[0], "female": female[0]} })
            #print(type_of_sport,male,female)
    except Exception as e:
        print(e)
        pass
    #print(all_track_dict)
    college.update({"varsity_athletic_teams":all_track_dict})
    conn.zadd("collegedata", float(college['unitid']), college)
    print(college)
