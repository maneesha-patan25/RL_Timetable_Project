import random

DAYS = 5
PERIODS = 6

class TimetableEnv:

    def __init__(self, subjects, teachers, rooms):

        self.subjects = subjects
        self.teachers = teachers
        self.rooms = rooms

        self.num_subjects = len(subjects)
        self.num_teachers = len(teachers)
        self.num_rooms = len(rooms)

    def generate_timetable(self):

        timetable = [["-" for _ in range(PERIODS)] for _ in range(DAYS)]

        subject_count = {s:0 for s in self.subjects}
        teacher_busy = [[False]*PERIODS for _ in range(DAYS)]
        room_busy = [[False]*PERIODS for _ in range(DAYS)]

        for subject in self.subjects:

            classes = 0
            attempts = 0

            while classes < 3 and attempts < 100:

                day = random.randint(0,4)
                period = random.randint(0,5)

                # avoid same subject twice in same day
                already_today = False
                for p in range(PERIODS):
                    if timetable[day][p] != "-" and subject in timetable[day][p]:
                        already_today = True

                if already_today:
                    attempts+=1
                    continue

                teacher = random.randint(0,self.num_teachers-1)
                room = random.randint(0,self.num_rooms-1)

                if timetable[day][period] == "-" and not teacher_busy[day][period] and not room_busy[day][period]:

                    timetable[day][period] = f"{subject} | T{teacher+1} | R{room+1}"

                    teacher_busy[day][period] = True
                    room_busy[day][period] = True

                    subject_count[subject]+=1
                    classes+=1

                attempts+=1

        return timetable
