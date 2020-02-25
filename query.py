import mysql.connector
import coffeemaschine

COFFEE_PRICE = 0.7
ESPRESSO = 1.0
MAX_DEBT = 21.0


def main():
    connection = connect()
    curr_card = read_card()
    auth = authenticate(connection, curr_card)

    if not auth:
        disconnect(connection)
        return print("Card not in database")

    id, fname, lname, cnumber, pref, debt = get_person_entries(connection, curr_card)
    print(debt)

    # HIER AUF EINGABE WARTEN mit IF Abfrage oder so UND GETRÄNK SPEZIFIZIEREN
    # allowed = genug GELD
    allowed = is_allowed(debt)
    if not allowed:
        print("Please pay your debt")
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
    test = query_handler(mydb, "SELECT * from USER WHERE cardnumber = " + card + ";")

    p_id = test[0][0]
    p_fname = test[0][1]
    p_lname = test[0][2]
    p_cnumber = str(test[0][4])
    p_pref = test[0][5]
    p_debt = test[0][6]

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
#         command = "SELECT schulden FROM USER where cardnumber = " + card + ";"
#         debt = query_handler(mydb, command)
#         return debt[0][0]
#     else:
#         return False


def authenticate(mydb, given_card):
    sql = "SELECT cardnumber FROM USER;"
    dbcard = query_handler(mydb, sql)
    print(dbcard)
    i = 0

    for card in dbcard:
        print("card: ",card)
        print("given card: ",given_card)
        print(type(given_card))
        shortened = card[0]
        #shortened=int(shortened)
        print("shortened: ",shortened)
        print(type(shortened))
        if given_card == shortened:
            return True
        i += 1

    return False


def is_allowed(person_debt):
    if person_debt + COFFEE_PRICE > MAX_DEBT:
        return False
    return True


def get_coffee(card, what_coffee):
    coffeemaschine.brew_coffee(what_coffee)
    pass


def update_debt(mydb, card, debt, drink):
    new_debt = debt + drink
    new_debt = round(new_debt, 1)
    sql = "UPDATE USER SET schulden = " + str(new_debt) + " WHERE cardnumber =" + card + ";"
    update_handler(mydb, sql)


if __name__ == '__main__':
    main()
