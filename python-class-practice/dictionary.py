# ------------Dictionary------------
# Definition and properties of dictionary.
# Creation of dictionary.
# Traversing
# In-built method
# dictionary comprehension
# Assignment and class 


# -----------Definition and properties of dictionary.-----------
# 1. Dictionary is a data structure in python used to store multiple data in key: value format.
# 2. ordered, mutable
# 3. Indexing by key, not position
# 4. key must be any type of data 
# 5. value can be any type of data 
# 6. used in fast loop


# ---------Creation of dictionary-----------
# stu_profile={'aman':'noida','rohan':'delhi'}
# print(type(stu_profile))
# print(stu_profile)

# stu_marks=dict([('aman',300),('shivam',80)])
# print(stu_marks)

# stu_profile={'aman':'noida','rohan':'delhi'}
# stu_profile.update({'aman':'UP'})
# print(stu_profile)


# In-built method
# stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':44}
# v=stu_marks.values()
# k=stu_marks.keys()
# i=stu_marks.items()
# res=stu_marks.get('dev',"Not Found")
# print(v)
# print(k)
# print(i)
# print(res)


profile={
    'aman':{'address':["Noida","Delhi","Mumbai"],
    'hobbies':["reading","cooking","tavelling"],
    'password':{"insta":234545,"fb":"984549"}
    },
     'abhi':{'address':["UP","Delhi","gurugaon"],
    'hobbies':["playing","cooking","tavelling"],
    'password':{"insta":234545,"fb":"984549"}
     }
    }
# res=profile['aman']['password']["insta"]
res=profile['abhi']['hobbies']
print(res)










# Traversing
# stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':44}

