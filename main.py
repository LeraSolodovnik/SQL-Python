import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='43625')

try:
    connection.cursor().execute(""" my_db""")
except:
    pass
create="""CREATE DATABASE IF NOT EXISTS my_db; use my_db"""
for element in create.split(';'):
    try:
        connection.cursor().execute(element)
        connection.commit()
    except:
        print("FAIL IN " + str(element))
connection.close()

con = pymysql.connect(host='localhost',
                             user='root',
                             password='43625',
                             db='my_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with con.cursor() as cursor:
    cursor.execute("""CREATE TABLE IF NOT EXISTS `students` (
  `Номер` INT NOT NULL AUTO_INCREMENT,
  `Фамилия` VARCHAR(45) NULL,
  `Имя` VARCHAR(45) NULL,
  `Отчество` VARCHAR(45) NULL,
  PRIMARY KEY (`Номер`))
ENGINE = InnoDB;""")

def func():
    with con.cursor() as cursor:
        print('Выберите что нужно сделать(цифру):'"\n"
              '1. Добавить данные'"\n"
              '2. Обновить данные'"\n"
              '3. Удалить данные'"\n"
              '4. Вывести таблицу'"\n"
              '0. Выход')
        a = int(input())
        if a == 1:
            fio = "INSERT INTO `students` (`Фамилия`, `Имя`, `Отчество`)" + " values ( %s, %s, %s);"

            print('Введите Фамилию')
            f = str(input())

            print('Введите Имя')
            name = str(input())

            print('Введите Отчество')

            ot = str(input())

            cursor.execute(fio, (f, name, ot))
            con.commit()
            func()
        if a == 2:
            print('Что вы хотите изменить?''\n'
                  '1. Фамилию студента''\n'
                  '2. Имя студента''\n'
                  '3. Отчество студента''\n'
                  '4. ФИО студента''\n'
                  '5. Номер студента(ток на тот которого нет)'
                  )
            up = int(input())
            if up == 1:
                print('Номер студента информацию о котором нужно изменить?')
                num1 = input()
                print('На какую фамилию нужно изменить?')
                num2 = input()
                update = "UPDATE `students` SET `Фамилия` =%s WHERE `Номер` =%s"
                cursor.execute(update, (num2, num1))
                con.commit()
            if up == 2:
                print('Номер студента информацию о котором нужно изменить?')
                num1 = input()
                print('На какое имя нужно изменить?')
                num2 = input()
                update = "UPDATE `students` SET `Имя` =%s WHERE `Номер` =%s"
                cursor.execute(update, (num2, num1))
                con.commit()
            if up == 3:
                print('Номер студента информацию о котором нужно изменить?')
                num1 = input()
                print('На какое отчество нужно изменить?')
                num2 = input()
                update = "UPDATE `students` SET `Отчество` =%s WHERE `Номер` =%s"
                cursor.execute(update, (num2, num1))
                con.commit()
            if up == 4:
                print('Номер студента информацию о котором нужно изменить?')
                num1 = input()

                print('На какую фамилию нужно изменить?')
                num2 = input()

                print('На какое имя нужно изменить?')
                num3 = input()

                print('На какое отчество нужно изменить?')
                num4 = input()

                update = "UPDATE `students` SET `Фамилия` = %s, `Имя` = %s, `Отчество` = %s WHERE `Номер` =%s"
                cursor.execute(update, (num2, num3, num4, num1))
                con.commit()
            if up == 5:
                print('Номер студента информацию о котором нужно изменить?')
                num1 = input()
                print('На какой номер нужно изменить?')
                num2 = input()
                update = "UPDATE `students` SET `Номер` =%s WHERE `Номер` =%s"
                cursor.execute(update, (num2, num1))
                con.commit()
            func()
        if a == 3:
            print('Номер студента информацию о котором нужно удалить?')
            n = input()
            delete = "DELETE FROM `my_db`.`students` WHERE `Номер` = %s"
            cursor.execute(delete, (n))
            con.commit()
            func()
        if a == 4:
            cursor.execute("""SELECT * FROM students;""")
            print(cursor.fetchall())
            func()
con.close



func()


