from django.db.backends.postgresql.base import DatabaseWrapper as PostgresWrapper


class DatabaseWrapper(PostgresWrapper):
    def _cursor(self, *args, **kwargs):
        """
        Check for a connection then checks to see if it is usable. If it is not we remove the connection and the
        default postgres wrapper will automatically reconnect in its _cursor() function.
        """
        if self.connection:
            if not self.is_usable():
                self.connection.close()
                self.connection = None
        return super(DatabaseWrapper, self)._cursor(*args, **kwargs)
