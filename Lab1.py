from flask import Flask, render_template, request
import sqlite3

variable=0
array=[]
connection=sqlite3.connect("./NotesDatabase.db")
#connection=sqlite3.connect("./NotesDatabase.db")
app = Flask(__name__,static_url_path='/')

#Pirma svetaine
@app.route("/")
def mano_funkcija():
    return ("Labas")

#Antra svetaine
@app.route("/test")
def test_route():
    if (request.args.get("name")):
        plus_one()
    return render_template('./index.html', var=plus_one())

#trecia svetaine
@app.route("/debug")
def plus_one():
    global variable
    variable = variable + 1
    return str(variable)

#Ketvirta svetaine
@app.route("/notes", methods=["GET","POST"])
def notes():
    if(request.method == "POST"):
        global array
        args = request.form.get("note2")
        if(args):
            array.append(args)
            insert_into_db(args)
            print(array)
        return render_template('./notes.html', note=select_from_db())
    else:
        return render_template('./notes.html', note=select_from_db())

def creationDB():
    global connection
    cursor=connection.cursor()
    createTableString="""CREATE TABLE IF NOT EXISTS Sheets (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL
    )"""

    createNotesTableString="""CREATE TABLE IF NOT EXISTS Notes (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        SheetId INTEGER ID,
        Header TEXT,
        Text TEXT,
        FOREIGN KEY (SheetId) REFERENCES Sheets(Id)
    )"""

    cursor.execute(createTableString)
    cursor.execute(createNotesTableString)

def insert_into_db(note):
    conn=sqlite3.connect("./NotesDatabase.db")
    queryString="""
        INSERT INTO Sheets (Name) VALUES (?)
    """
    cur = conn.cursor()
    cur.execute(queryString, (note,))
    conn.commit()


def select_from_db():
    conn=sqlite3.connect("./NotesDatabase.db")
    queryString="""
        SELECT name FROM Sheets
    """
    cur = conn.cursor()
    cur.execute(queryString).fetchall()
    return array

#Penkta svetaine
@app.route("/register")
def register():
    if(request.method == "POST"):
        global array
        args = request.form.get("reg1")
        if(args):
            array.append(args)
            insert_into_REG(args)
            print(array)
            return render_template('./register.html', note=select_from_REG())
    else:
        return render_template('./register.html', note=select_from_REG())

def creationREG():
    global connection
    cursor=connection.cursor()
    createRegTableString="""CREATE TABLE IF NOT EXISTS Sheets (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL
    )"""

    cursor.execute(createRegTableString)
    cursor.execute(createRegNotesTableString)

createRegNotesTableString="""CREATE TABLE IF NOT EXISTS register (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        SheetId INTEGER ID,
        Header TEXT,
        Text TEXT,
        FOREIGN KEY (SheetId) REFERENCES Sheets(Id)
    )"""

def insert_into_REG(note):
    conn=sqlite3.connect("./RegNotesDatabase.db")
    queryString="""
        INSERT INTO Sheets (Name) VALUES (?)
    """
    cur = conn.cursor()
    cur.execute(queryString, (note,))
    conn.commit()

def select_from_REG():
    conn=sqlite3.connect("./RegNotesDatabase.db")
    queryString="""
        SELECT name FROM Sheets
    """
    cur = conn.cursor()
    cur.execute(queryString).fetchall()
    return array

#Svetainiu ijungimo kodas:
if __name__ =="__main__":
    creationDB()
    #creationREG()
    app.run(debug="true")