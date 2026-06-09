try:
    import MySQLdb  # noqa: F401 — mysqlclient (used in Docker/Linux)
except ImportError:
    import pymysql
    pymysql.install_as_MySQLdb()
