import os
import time
import requests

from multiprocessing import Pool


class MacacaServer:
    def __init__(self, runs):
        self._runs = runs
        self._cmd = 'macaca server -p %s --verbose'
        self._url = 'http://127.0.0.1:%s/wd/hub/status'
        self._file = 'macaca_server_port_%s.log'
        self._kill = 'kill -9 %d'
        # self._kill = 'taskkill /PID %d /F'
        self._pids = []

    @staticmethod
    def server_url(port):
        server_url = {
            'hostname': '127.0.0.1',
            'port': port,
        }

        return server_url

    def start_server(self):
        pool = Pool(processes=len(self._runs))

        for run in self._runs:
            pool.apply_async(self._run_server, args=(run,))

        pool.close()

        # after start macaca server, macaca server process can not return, so should not join
        # p.join()

        for run in self._runs:
            while not self.is_running(run.get_port()):
                print('wait macaca server all ready...')
                time.sleep(1)
        print('macaca server all ready')

        for run in self._runs:
            file = str(run.get_path() + '/' + self._file) % run.get_port()
            with open(file, 'r') as f:
                line = f.read()
                start = line.find('pid:')
                end = line[start:].find(' ')

                pid = line[start:][4:end]
                self._pids.append(int(pid))

    def _run_server(self, run):
        port = run.get_port()
        cmd = str(self._cmd + ' > ' + run.get_path() + '/' + self._file) % (port, port)
        os.system(cmd)

    def is_running(self, port):
        url = self._url % port

        response = None
        try:
            response = requests.get(url, timeout=0.1)

            if str(response.status_code).startswith('2'):
                # data = json.loads((response.content).decode("utf-8"))
                # if data.get("staus") == 0:
                return True

            return False
        except requests.exceptions.ConnectionError:
            return False
        except requests.exceptions.ReadTimeout:
            return False
        finally:
            if response:
                response.close()

    def kill_macaca_server(self):
        for pid in self._pids:
            os.popen(self._kill % pid)
