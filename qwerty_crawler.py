for i in college_data[:10001]:
        unitid = str(i['unitid'])
        print(unitid)
        import requests
        from lxml import html
        #url = 'https://nces.ed.gov/collegenavigator/?id=100937#general'
        #url = 'https://nces.ed.gov/collegenavigator/?id=144892#general'
        url = 'https://nces.ed.gov/collegenavigator/?id='+unitid+'#general'
        pageContent = requests.get(url)
        tree = html.fromstring(pageContent.content)


        ##Institution namesi

        inst_name = tree.xpath("//span[@class='headerlg']/text()")
        #print(inst_name)
        college = {}
        college['inst_name'] = inst_name[0] if inst_name else None
        if not inst_name:
            continue;

        ##HBCU
        hbcu = tree.xpath("//div[@id='ctl00_cphCollegeNavBody_ucInstitutionMain_divINFORight']/text()")
        if hbcu:
            text = 'Historically Black College or University'
            check = [i for i in hbcu if text in i]
            if check:
                college['hbcu'] = True
                print("HBCU is True")
            #print(hbcu)
            else:
                college['hbcu'] = False
        ##Admissions
            ##No of applicants
        try:
            a = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[1]/text()")
            total_applicants = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[2]/text()")
            male_applicant = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[3]/text()")
            female_applicant = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[4]/text()")

            #print(total_applicants, male_applicant,female_applicant)
            college['total_applicants'] = total_applicants[0] if total_applicants else None
            college['male_applicants'] = male_applicant[0] if male_applicant else None
            college['female_applicants'] = female_applicant[0] if female_applicant else None
        except Exception as e:
            print("no of applicants")
            print(e)
            pass

        ##percent admitted
        try:
            b = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[1]/text()")
            percent_admitted_total = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[2]/text()")
            percent_male_admitted = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[3]/text()")
            percent_female_admitted = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[4]/text()")
        #print(percent_admitted_total,percent_male_admitted,percent_female_admitted)
            college['total_admitted_percent'] = percent_admitted_total[0] if percent_admitted_total else None
            college['male_admitted_percent'] = percent_male_admitted[0] if percent_male_admitted else None
            college['female_admitted_percent'] = percent_female_admitted[0] if percent_female_admitted else None
        except Exception as e:
            print("percent admitted")
            pass
        ## ROTC
        rotc = tree.xpath("//div[@id='ctl00_cphCollegeNavBody_ucInstitutionMain_divNPC']/text()")
        try:
            army = 'Army'
            air = 'Air Force'
            navy = 'Navy'
            army = [i for i in rotc if army in i]
            navy = [i for i in rotc if navy in i]
            air = [i for i in rotc if air in i]
            if rotc and (air or navy or army):
                print(army,navy, air)
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
        college['male_admit_rate'] = data[1] if data else None
        college['female_admit_rate'] = data[2] if data else None
        ## Enrollment by Race/Ethnicity
        race = tree.xpath("//div[@id='enrolmt']//table[3]//tbody[1]//tr[1]//td[1]//img[1]/@alt")
        #print(race)
        if race:
            race = race[0]
            race_data = race.split('\r\n')
            race_dict={}
            for i in race_data:
                data = i.split(':')
                if data:
                    for j in range(1):
                        race_dict[data[j]] = data[j+1]
            college.update({"race":race_dict})
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
            college.update(age_dict)

        ##SAT/ACT required
        sat = tree.xpath("//div[@id='admsns']//table[3]//tbody[1]//tr[5]//td[2]/text()")
        print(sat)
        if sat:
            print("sat required")
            college['sat_required'] = False
        else:
            college['sat_required'] = True

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
        college.update({"athletic_teams":all_track_dict})
        colleges.append(college)
