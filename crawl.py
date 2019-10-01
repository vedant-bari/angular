import requests
from lxml import html
#url = 'https://nces.ed.gov/collegenavigator/?id=178369#general'
#url = 'https://nces.ed.gov/collegenavigator/?id=144892#general'
url= 'https://nces.ed.gov/collegenavigator/?id=178369#general'
#url = 'https://nces.ed.gov/collegenavigator/?id=102058#general'
pageContent = requests.get(url)
tree = html.fromstring(pageContent.content)


##SAT SCORE
##/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[12]/div[1]/div[2]/div[1]/table[4]/tbody[1]/tr[1]/td[2]
##/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[12]/div[1]/div[2]/div[1]/table[4]/tbody[1]/tr[1]/td[2]
##//div[@id='admsns']//table[4]//tbody[1]//tr[1]//td[1]
count = tree.xpath("Students submitting scores')]//following::td")
elememt = tree.xpath(count[0]//text())
print("count", count)

sat_number_submitting= tree.xpath("//div[@id='admsns']//table[4]//tbody[1]//tr[1]//td[2]/text()")
sat_percent_submitting = tree.xpath("//div[@id='admsns']//table[4]//tbody[1]//tr[1]//td[3]/text()")
act_number_submitting = tree.xpath("//div[@id='admsns']//table[4]//tbody[1]//tr[2]//td[2]/text()")
act_percent_submitting = tree.xpath("//div[@id='admsns']//table[4]//tbody[1]//tr[2]//td[3]/text()")
print("sat score", sat_number_submitting, sat_percent_submitting, act_number_submitting, act_percent_submitting)


##Test SCORE
##/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[12]/div[1]/div[2]/div[1]/table[4]/tbody[1]/tr[1]/td[1]
##/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[12]/div[1]/div[2]/div[1]/table[5]/tbody[1]/tr[1]/td[1]
sat_crit_read_25_pctl = tree.xpath("//div[@id='admsns']//table[4]//tbody[1]//tr[1]//td[2]/text()")
sat_crit_read_75_pctl= tree.xpath("//div[@id='admsns']//table[4]//tbody[1]//tr[1]//td[3]/text()")

print("sat_evidence",sat_crit_read_25_pctl, sat_crit_read_75_pctl)

sat_math_25_pctl = tree.xpath("//div[@id='admsns']//table[5]//tbody[1]//tr[2]//td[2]/text()")
sat_math_75_pctl = tree.xpath("//div[@id='admsns']//table[5]//tbody[1]//tr[2]//td[3]/text()")
print("sat_math",sat_math_25_pctl,sat_math_75_pctl)

act_composite_25_percentile = tree.xpath("//div[@id='admsns']//table[5]//tbody[1]//tr[3]//td[2]/text()")
act_composite_75_percentile =  tree.xpath("//div[@id='admsns']//table[5]//tbody[1]//tr[3]//td[3]/text()")
print("act_composite", act_composite_25_percentile, act_composite_75_percentile)

act_english_25_percentile =  tree.xpath("//div[@id='admsns']//table[5]//tbody[1]//tr[4]//td[2]/text()")
act_english_75_percentile = tree.xpath("//div[@id='admsns']//table[5]//tbody[1]//tr[4]//td[3]/text()")
print("act_english", act_english_25_percentile, act_english_75_percentile)

act_math_25_pctl = tree.xpath("//div[@id='admsns']//table[5]//tbody[1]//tr[5]//td[2]/text()")
act_math_75_pctl = tree.xpath("//div[@id='admsns']//table[5]//tbody[1]//tr[5]//td[3]/text()")
print("act_math", act_math_25_pctl, act_math_75_pctl)

##UNDERGRADUATE ADMISSIONS FALL 2018
#/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[12]/div[1]/div[2]/div[1]/table[2]/thead[1]/tr[1]/th[2]
no = tree.xpath("//div[@id='divctl00_cphCollegeNavBody_ucInstitutionMain_ctl04']//th[contains(text(),'Total')]/text()")
print("in admission")
print(no)

##Institution namesi

inst_name = tree.xpath("//span[@class='headerlg']/text()")
print(inst_name)
#if not inst_name:
    # continue;

##HBCU
hbcu = tree.xpath("//div[@id='ctl00_cphCollegeNavBody_ucInstitutionMain_divINFORight']/text()")
if hbcu:
    text = 'Historically Black College or University'
    check = [i for i in hbcu if text in i]
    if check:
        print("HBCU is True")
    #print(hbcu)
##Admissions
##No of applicants
#/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[12]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]
#//table[@class='tabular']//td[contains(text(),'6,012')]
#/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[11]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]
#/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[11]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]
undergraduate_enrolment = tree.xpath("//div[@id='enrolmt']//table[1]//tbody[1]//tr[1]//td[2]/text()")
print("undergraduate enrollment", undergraduate_enrolment)
##Undergrade Enrollment

 #/html[1]/body[1]/div[1]/form[1]/div[3]/div[2]/div[3]/div[11]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]
try:
    under_graduate = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[1]/text()")
    print("in under graduate")
    #print(under_graduate)
    ug = 'Undergraduate application fee (2018-2019): '
    under_graduate_test = [k for k in under_graduate if ug in k]
    print("test", under_graduate_test)
    if not under_graduate_test:
        a = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[1]/text()")
        total_applicants = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[2]/text()")
        male_applicant = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[3]/text()")
        female_applicant = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[1]//td[4]/text()")

        print("no of applicants")
        print(a,total_applicants, male_applicant,female_applicant)


        ##percent admitted
        b = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[2]//td[1]/text()")
        percent_admitted_total = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[2]//td[2]/text()")
        percent_male_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[2]//td[3]/text()")
        percent_female_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[2]//td[4]/text()")
        print(percent_admitted_total,percent_male_admitted,percent_female_admitted)

        ##percent admitted who enrolled
        c = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[1]/text()")
        percent_admitted_enrolled_total = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[2]/text()")
        percent_male_enrolled_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[3]/text()")
        percent_female_enrolled_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[4]/text()")
        print(percent_admitted_enrolled_total,percent_male_enrolled_admitted,percent_female_enrolled_admitted)
    else:
        ##under_graduate not present
        #//div[@id='admsns']//table[3]//tbody[1]//tr[1]//td[2]
        print("in else")
        a = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[1]/text()")
        total_applicants = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[2]/text()")
        male_applicant = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[3]/text()")
        female_applicant = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[1]//td[4]/text()")

        print("no of applicants")
        print(a,total_applicants, male_applicant,female_applicant)


        ##percent admitted
        b = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[1]/text()")
        percent_admitted_total = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[2]/text()")
        percent_male_admitted = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[3]/text()")
        percent_female_admitted = tree.xpath("//div[@id='admsns']//table[2]//tbody[1]//tr[2]//td[4]/text()")
        print(percent_admitted_total,percent_male_admitted,percent_female_admitted)

        ##percent admitted who enrolled
        c = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[1]/text()")
        percent_admitted_enrolled_total = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[2]/text()")
        percent_male_enrolled_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[3]/text()")
        percent_female_enrolled_admitted = tree.xpath("//div[@id='admsns']//table[1]//tbody[1]//tr[3]//td[4]/text()")
        print(percent_admitted_enrolled_total,percent_male_enrolled_admitted,percent_female_enrolled_admitted)

except Exception as e:
    print(e)
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
if enc:
    enc = enc[0]
    print(enc)
    data = enc.split('\r\n')
    print("enc")
    print(data)
else:
    print("No enc found")
#male_percentage = data[3]
#female_percerntage = data[5]
#print(male_percentage, female_percerntage)


## Enrollment by Race/Ethnicity
race = tree.xpath("//div[@id='enrolmt']//table[3]//tbody[1]//tr[1]//td[1]//img[1]/@alt")
if race:
    race = race[0]
    race_data = race.split('\r\n')
    race_dict={}
    for i in race_data:
        data = i.split(':')
        if data:
            for j in range(1):
                race_dict[data[j]] = data[j+1]
    print(race_dict)

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
    print(age_dict)

##SAT/ACT required
sat = tree.xpath("//div[@id='admsns']//table[3]//tbody[1]//tr[5]//td[2]/text()")
print(sat)
if sat:
    print("sat required")


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
print(all_track_dict)
#import csv
#
# with open('College_database_crawl - Sheet1.csv', mode='w') as employee_file:

# with open('College_database_crawl - Sheet1.csv','w') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
#     writer = csv.writer(csv_file, )
#     for row in reader:
#         ##Institution Name
#         row[0] = inst_name[0]
# #         writer.writerow(row)
#
# with open('College_database_crawl - Sheet1.csv', 'r') as readFile:
# reader = csv.reader(readFile)
# lines = list(reader)
# # lines[2] = row
# print(row)
#
# with open('College_database_crawl - Sheet1.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(lines)
