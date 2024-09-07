# from datetime import *
#
# class Project:
#     def __init__(self,name,startDate,endDate):
#         self.name=name
#         self.startDate=startDate
#         self.endDate=endDate
#         self.tasks=[]
#
#     def addTask(self,task):
#         self.tasks.append(task)
#
# class Task:
#     def __init__(self,name,duration):
#         self.name=name
#         self.duration=duration
#         self.resources=[]
#
#     def addResource(self,resource):
#         self.resources.append(resource)
#
# class Resource:
#     def __init__(self,name,skill):
#         self.name=name
#         self.skill=skill
#
# project=Project("AI",date(2021,1,1),date(2022,1,1))
# task=Task("Create a Bot",90)
# resource=Resource("John","Pyhton")
# task.addResource(resource)
# project.addTask(task)
#
# for eachTask in project.tasks:
#     print(eachTask.name)
#     for eachResource in eachTask.resources:
#         print(eachResource.name)
#         print(eachResource.skill)

class Event:
    def __init__(self,startTime,endTime):
        self.startTime=startTime
        self.endTime=endTime
        self.venues=[]

    def addVenue(self,venue):
        self.venues.append(venue)


class Venue:
    def __init__(self,name):
        self.name=name
        self.addresses=[]

    def addAddress(self,address):
        self.addresses.append(address)


class Address:
    def __init__(self,street,city,state,country,pincode):
        self.street=street
        self.city=city
        self.state=state
        self.country=country
        self.pincode=pincode
        self.surnames=[]

    def addSurname(self,surname):
        self.surnames.append(surname)

class Surname:
    def __init__(self,surname,religion):
        self.surname=surname
        self.religion=religion

event=Event("12am","8pm")
venue=Venue("Shri Gardens")
address=Address("Near Bapat chouraha","Indore","MP","India",452007)
surname=Surname("Joshi","Hindu")
venue.addAddress(address)
event.addVenue(venue)
address.addSurname(surname)

print("{}-{}".format(event.startTime,event.endTime))

for eachVenue in event.venues:
    print(eachVenue.name)
    for eachAddress in eachVenue.addresses:
        print("{},{},{},{},{}".format(eachAddress.street,eachAddress.city,eachAddress.state,eachAddress.country,eachAddress.pincode))
        for eachSurname in eachAddress.surnames:
            print("{} belonging ot this religion : {}".format(eachSurname.surname,eachSurname.religion))
