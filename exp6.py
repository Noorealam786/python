# students in exams
cet = {"Shanawaz", "Bob"}
jee = {"Noorealam", "Bob"}
neet = {"Hafin", "Eve"}
print("All students:", cet|jee|neet) #Union
print("Students in all exam:", cet & jee & neet) # intersection
print("Cet but not in jee:", cet - jee) #Difference
