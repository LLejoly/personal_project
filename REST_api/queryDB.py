import MySQLdb


class QueryDB:
    def __init__(self, connection: MySQLdb.connection, encode='latin-1', decode='utf-8'):
        self.connection = connection
        self.encode = encode
        self.decode = decode

    def get_query_db(self, query, args=(), one=False, header=False):
        cursor = self.connection.cursor()
        cursor.execute(query, args)
        head = []
        if header:
            head = [descr[0] for descr in cursor.description]

        if one and header:
            data = cursor.fetchone()
            cursor.close()
            return dict(zip(head, data))
        elif one:
            data = cursor.fetchone()
            cursor.close()
            return data

        data = cursor.fetchall()

        rv = []
        for row in data:
            tmp = []
            for idx, value in enumerate(row):
                # latin to utf-8
                if type(value) is str:
                    tmp.append(value.encode(self.encode).decode(self.decode))
                else:
                    tmp.append(value)

            if header:
                rv.append(dict(zip(head, tmp)))
            else:
                rv.append(tmp)

        self.connection.commit()  ## to be sure to have the last value stored in the database and not a local variable
        cursor.close()
        return rv

    def insert_query_db(self, query, args=()):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, args)
            cursor.close()
            return True
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            cursor.close()
            return False
