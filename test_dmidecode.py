from dmidecode import DMIDCode
import unittest
class DMIDecodeTest(unittest.TestCase):
    def setUp(self):
        data = """# dmidecode 3.1
        Getting SMBIOS data from sysfs.
        SMBIOS 2.6 present.

        Handle 0x0001, DMI type 1, 27 bytes
        Bios Information
                Vendor: LENOVO
                Version: 29CN40WW(V2.17)
                Release Date: 04/13/2011
                ROM Size: 2048 kB
                Characteristics:
                        PCI is supported
                        BIOS is upgradeable
                        BIOS shadowing is allowed
                        Boot from CD is supported
                BIOS Revision: 1.40
        """
        self.dmide=DMIDCode(data)

    def test_singleParameter(self):
        self.assertEqual(self.dmide.getValue("Vendor"),"LENOVO")
        self.assertEqual(self.dmide.getValue("Version"),"29CN40WW(V2.17)")
        self.assertEqual(self.dmide.getValue("Release Date"),"04/13/2011")
        self.assertEqual(self.dmide.getValue("ROM Size"),"2048 kB")

if __name__ == '__main__':
    unittest.main()