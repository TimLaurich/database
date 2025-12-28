class ReportService:

    def __init__(self, conn):
        self.conn = conn

    def objednavky(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM view_objednavky_detail")
        return cur.fetchall()
