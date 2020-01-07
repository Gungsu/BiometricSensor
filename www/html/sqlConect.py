import mysql.connector as mysql

conf = {
        "host": "localhost",
        "user": "phpprincipal",
        "passwd": "sql12345",
        "database": "bancoNomesFinger",
        "tabela": "cadastro",
        "colHexFinger": "finger",
        "ident": "id"
}

db = mysql.connect(
        host = conf["host"],
        user = conf["user"],
        passwd = conf["passwd"],
        database = conf["database"]
)
cursor = db.cursor()


def searchFdb(fingerHex):
    global conf
    global cursor
    cmdSql = 'SELECT '+str(conf["colHexFinger"])+' FROM '+str(conf["tabela"])+' WHERE '+str(conf["colHexFinger"])+' = '+"\'"+str(fingerHex)+"\'"
    cursor.execute(cmdSql)
    countRow = 0
    for row in cursor: countRow += 1
    r = [False,True][countRow>0]
    return (r)

def addFingerDb(fingerHex, id):
    global cursor
    global conf
    global db
    cmdSql = 'UPDATE '+str(conf["tabela"])+' SET '+str(conf["colHexFinger"])+' = '+"\'"+str(fingerHex)+"\'"+' WHERE '+str(conf["ident"])+' = '+str(id)
    cursor.execute(cmdSql)
    db.commit()
    return True

def verId(id):
    global cursor
    global conf
    cmdSql = 'SELECT '+str(conf["ident"])+' FROM '+str(conf["tabela"])+' WHERE '+str(conf["ident"])+' = '+str(id)
    cursor.execute(cmdSql)
    countRow = 0
    for row in cursor: countRow += 1
    r = [False,True][countRow>0]
    return (r)
