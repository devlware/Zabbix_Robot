import telnetlib


class Zabbix(object):

    _tn = None

    def __init__(self, h, p, t):
        """ """

        try:
            self._tn = telnetlib.Telnet(h, p, t)
        except Exception as e:
            raise e

    def send_command(self, cmd):
        """   """

        try:
            self._tn.write(cmd.encode('ascii') + '\r\n'.encode('ascii'))
        except Exception as e:
            raise e

        try:
            return self._tn.read_until(b"\r", timeout=2.5).decode('ascii').strip()
        except Exception as e:
            raise e

    def close_conn(self):
        """ """

        self._tn.close()

    def test(self):
        """   """

        return "Zabbix Test"
