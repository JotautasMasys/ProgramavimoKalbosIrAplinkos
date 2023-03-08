from flask import Flask, render_template, request
import sqlite3

variable=0
array=[]

app = Flask(__name__,static_url_path='/')

@app.route("/")
def mano_funkcija():
    return ("Labas")

@app.route("/test")
def test_route():
    if (request.args.get("name")):
        plus_one()
    return render_template('./index.html', var=plus_one())

@app.route("/debug")
def plus_one():
    global variable
    variable = variable + 1
    return str(variable)

@app.route("/notes", methods=["GET","POST"])
def notes():
    if(request.method == "POST"):
        global array
        args = request.form.get("note2")
        if(args):
            array.append(args)
            print(array)
        return render_template('./notes.html', note=array)
    else:
        return render_template('./notes.html', note=array)

def creationDB():
    connection=sqlite3.connect("C:\\Users\\1538848\\Dekstop\\NotesDataBase.db")
    cursor=connection.cursor()

    createTableString="""CREATE TABLE IF NOT EXISTS Sheets (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL
    )"""

    createNotesTableString="""CREATE TABLE IF NOT EXISTS Notes (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        SheetId INTEGER PRIMARY KEY AUTOINCREMENT,
        Header TEXT,
        Text TEXT,
        FOREIGN KEY (SheetId) REFERENCES Sheets(Id)
    )"""

    cursor.execute(createTableString)
    cursor.execute(createNotesTableString)


def insert_into_db():
    global connection
    queryString="""
        INSERT INTO Sheets (Name) VALUES (?) test
    """
    cur = connection.cursor()
    cur.execute(queryString, ('test',))


if __name__ =="__main__":
    creationDB()
    insert_into_db()
    app.run(debug="true")