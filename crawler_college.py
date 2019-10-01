college_data = []
for j in range(1,8):
    r = requests.get("https://ed-data-portal.urban.org/api/v1/college-university/ipeds/directory/2017/?page=%d"%(j))
    data = r.json()
    college = {}
   #globals()["college_data%d"%(j)] = []
   for i in data['results']:
        college = {}
        college['unitid'] = i['unitid']
        college['Institution Name'] = i['inst_name']
        college['US State']= i['state_abbr']
        college['US Region'] = i['region']
        college['HBCU'] = i['hbcu']
        college['locale'] = i['urban_centric_locale']
        college['Size'] = i['inst_size']
        college_data.append(college)
