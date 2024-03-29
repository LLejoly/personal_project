import MySQLdb


class QueryDB:
    def __init__(self, connection: MySQLdb.connection):
        self.connection = connection

    def get_query_db(self, query, args=(), one=False, header=False):
        """
        To manage the GET mysql query and its output format.
        :param query: a MySQL query
        :param args: a list of arguments passed to the query
        :param one: A boolean to say that we only want the first result of
        the query which is a simple dict or list in case of several outputs
        :param header: A boolean to specify if we want the header associated to the data
        :return: A list of elements
        """
        cursor = self.connection.cursor()
        cursor.execute(query, args)
        head = []
        if header:
            head = [descr[0] for descr in cursor.description]

        if one and header:
            data = cursor.fetchone()
            cursor.close()
            if data:
                return dict(zip(head, data))
            return data

        elif one:
            data = cursor.fetchone()
            cursor.close()
            return data

        data = cursor.fetchall()

        rv = []
        # format the output of the data collected
        for row in data:
            # add the header with the data
            if header:
                rv.append(dict(zip(head, row)))
            else:
                rv.append(row)

        self.connection.commit()  # to be sure to have the last value stored in the database and not a local variable
        cursor.close()
        return rv

    def insert_query_db(self, query, args=()):
        """
        Manage the POST request.
        :param query: a MySQL query
        :param args: a list of arguments passed to the query
        :return:
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, args)
            cursor.close()
            return True
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            cursor.close()
            return False
