#!/usr/bin/env python
import unittest
import application

class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = application.app.test_client()

    def testIndex(self):
        resp = self.app.get("/")
        assert resp.status_code == 200

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
