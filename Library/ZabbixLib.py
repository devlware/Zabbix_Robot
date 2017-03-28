from Zabbix import Zabbix


class ZabbixLib(object):
    """ """

    _result = None
    _zb = None

    def __init__(self, host, port, timeout=1.0):
        """ """

        self._zb = Zabbix(str(host), int(port), float(timeout))

    def send_command(self, cmd):
        """ """

        self._result = self._zb.send_command(cmd)

    def close_connection(self):
        """ """

        self._zb.close_conn()

    def result_in_range(self, range_min, range_max):
        """   """

        val = float(self._result)

        if val < float(range_min) or val > float(range_max):
            raise AssertionError('%s != (%s, %s)' % (val, range_min, range_max))

    def result_should_be(self, expected):
        """   """

        if expected != self._result:
            raise AssertionError('%s != %s\n' % (self._result, expected))
        else:
            return True

    def test(self):
        """   """

        self._result = self._zb.test()


if __name__ == '__main__':
    zb = ZabbixLib('192.168.2.2', 10050, 2.5)
    zb.send_command('agent.ping')

    if (zb.result_should_be('pong')):
        print("Test agent.ping Ok")
