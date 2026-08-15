# -*- coding: utf-8 -*-
"""Delete task log files older than a given date.

DB credentials come from environment variables (never hardcode secrets):
  MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
"""
import os
import sys

try:
    import MySQLdb
except ImportError:
    import pymysql as MySQLdb


def get_db_config():
    password = os.environ.get("MYSQL_PASSWORD")
    if not password:
        raise SystemExit(
            "MYSQL_PASSWORD is required. Also set MYSQL_HOST / MYSQL_PORT / "
            "MYSQL_USER / MYSQL_DB as needed."
        )
    return {
        "host": os.environ.get("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.environ.get("MYSQL_PORT", "3306")),
        "user": os.environ.get("MYSQL_USER", "root"),
        "passwd": password,
        "db": os.environ.get("MYSQL_DB", "escheduler"),
        "charset": "utf8",
    }


def clean_logs(start_date):
    conn = MySQLdb.connect(**get_db_config())
    cursor = conn.cursor()
    try:
        sql = (
            "SELECT log_path FROM t_escheduler_task_instance "
            "WHERE start_time < %s"
        )
        cursor.execute(sql, (start_date,))
        count = 0
        for row in cursor.fetchall():
            log_path = row[0]
            try:
                if log_path and os.path.exists(log_path):
                    count += 1
                    print("remove log path:", log_path)
                    os.remove(log_path)
            except OSError as exc:
                print(exc)
        print("clean log end! already clean %d logs" % count)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python CleanLog.py <closing-date YYYY-MM-DD>")
        sys.exit(1)
    print("clean logs before:", sys.argv[1])
    clean_logs(start_date=sys.argv[1])
