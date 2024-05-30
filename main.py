import data_prep as dp
import classes
import algorithm as a

if __name__ == '__main__':

    dp.preparing_database("Course data 2024.xlsx")

    professors = dp.pars_profs()

    courses, professors = dp.pars_lectures(professors,33)

    a.schedule_classes(courses,professors,33)



    exit()

