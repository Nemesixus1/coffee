import mysql.connector
import coffeemaschine
from datetime import datetime

MAX_DEBT = 21.0


def main():
    connection = connect()
    curr_card = read_card()
    auth = authenticate(connection, curr_card)

    if not auth:
        disconnect(connection)
        return 

    id, fname, lname, cnumber, pref, debt = get_person_entries(connection, curr_card)
    
    # allowed = genug GELD
    allowed = is_allowed(debt)
    if not allowed:
       
        return False
    else:
        get_coffee(cnumber, "espresso")
        update_debt(connection, '12345678', debt, COFFEE_PRICE)
    # new_debt = get_debt(connection, '12345678')
    # print(new_debt)

    # test = query_handler(connection, "SELECT * from USER WHERE cardnumber = '12345678';")
    # print(type(test))
    get_person_entries(connection, "12345678")

    disconnect(connection)


def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        db="USER",
        user="root", passwd="coffee"
    )
    return mydb


def disconnect(mydb):
    mydb.close()


#def read_card():
#    return '12345678'


def get_person_entries(mydb, card):
    test = query_handler(mydb, "SELECT * from USERS,RFIDCHIP WHERE USERS.id=RFIDCHIP.userID AND RFIDCHIP.chipID =" + card + ";")

    p_id = test[0][0]
    p_fname = test[0][1]
    p_lname = test[0][2]
    p_pref = test[0][4]
    p_debt = test[0][5]
    p_cnumber = str(test[0][6])

    return p_id, p_fname, p_lname, p_cnumber, p_pref, p_debt


def query_handler(mydb, sql):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    result = mycursor.fetchall()  # [0][0]
    mycursor.close()

    return result


def update_handler(mydb, sql):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mycursor.close()
    mydb.commit()


# def get_debt(mydb, card):
#     if authenticate(mydb, card):
#         command = "SELECT debt FROM USER where cardnumber = " + card + ";"
#         debt = query_handler(mydb, command)
#         return debt[0][0]
#     else:
#         return False


def authenticate(mydb, given_card):
    sql = "SELECT chipID FROM RFIDCHIP;"
    dbcard = query_handler(mydb, sql)
    i = 0

    for card in dbcard:
        shortened = card[0]
        if given_card == shortened:
            return True
        i += 1

    return False


def is_allowed(person_debt,price):

    if person_debt + price > MAX_DEBT:
        return False
    return True


def get_coffee(card, what_coffee):
    coffeemaschine.brew_coffee(what_coffee)
    pass


def update_debt(mydb, card, debt, drink):
    new_debt = debt + drink
    new_debt = round(new_debt, 1)
    sql = "UPDATE USERS,RFIDCHIP SET debt = " + str(new_debt) + " WHERE USERS.id=RFIDCHIP.userID AND chipID =" + card + ";"
    update_handler(mydb, sql)
    #datenow=datetime.now()
    #sql2= "Insert into TRANSACTIONS (chipID,productID,timestamp) VALUES("+card+",1,"+str(datenow)+");"
    #update_handler(mydb,sql2)

if __name__ == '__main__':
    main()
