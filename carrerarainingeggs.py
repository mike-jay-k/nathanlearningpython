    from carreralib import ControlUnit
    cu = CrontrolUnit("D4:8B:C6:FC:D8:07")
    cu.version()
b"5331"
    cu.request()
Status(fuel=(15, 15, 15, 15, 15, 15, 0, 0), start=0, mode=6
       pit=(False, False, False, False, False, False, False, False),
       display=8)
    cu.start()
    cu.request()
Timer(address=1, timestamp=243019, sector=1)
    cu.request()
Timer(address=0, timestamp=245704, sector=1)
