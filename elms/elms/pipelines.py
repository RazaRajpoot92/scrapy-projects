import sqlite3


class ElmsPipeline:

    def __init__(self):
        self.conn = sqlite3.connect("elements.db")
        self.cur = self.conn.cursor()


    def open_spider(self, spider):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS periodic_elements(

            symbol TEXT PRIMARY KEY,
            name TEXT,
            atomic_number INTEGER,
            atomic_mass REAL,
            chemical_group TEXT

        )
        """)

        self.conn.commit()

    def process_item(self, item, spider):
        self.cur.execute("INSERT OR IGNORE INTO periodic_elements VALUES(?,?,?,?,?)",
                         (item["symbol"],
                          item["name"],
                          item["atomic_number"],
                          item["atomic_mass"],
                          item["chemical_group"]
                          )
                         )
        self.conn.commit()
        return item


    def close_spider(self, spider):
        self.conn.close()

