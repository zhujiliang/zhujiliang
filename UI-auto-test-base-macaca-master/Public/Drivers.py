import time

from multiprocessing import Pool

from macaca import WebDriver

from Public.Ports import Ports
from Public.Devices import Devices
from Public.MacacaServer import MacacaServer
from Public.RunCases import RunCases
from Public.ReportPath import ReportPath
from Public.Log import Log
from Public.BasePage import BasePage


class Drivers:

    @staticmethod
    def _run_cases(server_url, run, cases, index):
        log = Log()
        log.set_logger(run.get_device()['udid'], run.get_path() + '/' + 'client.log')

        log.i('platformName: %s', run.get_device()['platformName'])
        log.i('udid: %s', run.get_device()['udid'])
        log.i('app: %s', run.get_device()['app'])
        log.i('reuse: %s\n', run.get_device()['reuse'])
        # log.i('autoAcceptAlerts: %s', run.get_device()['autoAcceptAlerts'])
        log.i('macaca server port: %d\n', run.get_port())

        # init driver
        driver = WebDriver(run.get_device(), server_url)
        driver.init()

        # set cls.path, it must be call before operate on any page
        path = ReportPath()
        path.set_path(run.get_path())

        # login_status = LoginStatus()
        # login_status.set_status(False)

        # set cls.driver, it must be call before operate on any page
        base_page = BasePage()
        base_page.set_driver(driver)
        base_page.set_index(index)

        try:
            # run cases
            run.run(cases)
        except AssertionError as e:
            log.e('AssertionError, %s', e)

        # quit driver
        driver.quit()

    def run(self, cases):
        # read all devices on this PC
        devices = Devices().get_devices()
        print("devices的列表：")
        print(devices)

        # read free ports on this PC
        ports = Ports().get_ports(len(devices))
        print('ports的列表：')
        print(ports)

        if not len(devices):
            print('there is no device connected this PC')
            return

        runs = []
        for i in range(len(devices)):
            runs.append(RunCases(devices[i], ports[i]))
        print('runs的列表：')
        print(runs)

        # start macaca server
        macaca_server = MacacaServer(runs)
        macaca_server.start_server()

        # run on every device
        pool = Pool(processes=len(runs))
        index = 0
        for run in runs:
            pool.apply_async(self._run_cases,
                             args=(macaca_server.server_url(run.get_port()), run, cases, index,))
            index += 1

            # fix bug of macaca, android driver can not init in the same time
            time.sleep(2)

        pool.close()
        pool.join()

        macaca_server.kill_macaca_server()




