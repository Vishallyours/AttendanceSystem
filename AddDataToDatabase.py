import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtimepython-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Vishal Sain",
            "major": "CSE",
            "starting_year": 2020,
            "total-Attendance": 6,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2023-12-11 09:54:34"
    },    "852741":
        {
            "name": "Emly blunt",
            "major": "CE",
            "starting_year": 2020,
            "total-Attendance": 16,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2023-12-12 08:51:04"
    },    "963852":
        {
            "name": "Elon musk",
            "major": "Robotics",
            "starting_year": 2021,
            "total-Attendance": 5,
            "standing": "Bad",
            "year": 3,
            "last_attendance_time": "2023-12-01 09:36:54"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
