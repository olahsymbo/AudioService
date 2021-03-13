import requests
from app import app
import unittest


class AudioTest(unittest.TestCase):

    def test_create_song(self):
        tester = app.test_client(self)
        payload = {'audioFileType': 'song',
                   'audioFileMetadata': '{"name": "mark le point", '
                                        '"duration": "10", '
                                        '"uploaded_at": "20210220"}'}

        response = tester.post("http://127.0.0.1:5000/create",
                               data=payload)

        self.assertEqual(200, response.status_code)

    def test_create_podcast(self):
        tester = app.test_client(self)
        payload = {'audioFileType': 'podcast',
                   'audioFileMetadata': '{"name": "mark le point", '
                                        '"duration": "100", '
                                        '"host": "remy", '
                                        '"participants":["morgan","kln","ijhg", "morgan","kln","ijhg"], '
                                        '"uploaded_at": "20210220"}'}
        response = tester.post("http://127.0.0.1:5000/create",
                               data=payload)

        self.assertEqual(200, response.status_code)

    def test_create_audiobook(self):
        tester = app.test_client(self)
        payload={'audioFileType': 'audiobook',
        'audioFileMetadata': '{"title": "new adventure", '
                             '"duration": "100", '
                             '"author": "remy", '
                             '"narrator": "delan", '
                             '"uploaded_at": "20210220"}'}
        response = tester.post("http://127.0.0.1:5000/create",
                               data=payload)

        self.assertEqual(200, response.status_code)

    def test_delete_song(self):
        tester = app.test_client(self)
        response = tester.delete("http://127.0.0.1:5000/delete/song/10")

        self.assertEqual(200, response.status_code)

    def test_delete_podcast(self):
        tester = app.test_client(self)
        response = tester.delete("http://127.0.0.1:5000/delete/podcast/10")

        self.assertEqual(200, response.status_code)

    def test_delete_audiobook(self):
        tester = app.test_client(self)
        response = tester.delete("http://127.0.0.1:5000/delete/audiobook/10")

        self.assertEqual(200, response.status_code)

    def test_update_song(self):
        tester = app.test_client(self)
        payload = {
            'audioFileMetadata':
                '{"name": "mark le point", '
                '"duration": "100"}'
        }
        response = tester.put("http://127.0.0.1:5000/update/song/8",
                               data=payload)

        self.assertEqual(200, response.status_code)

    def test_update_podcast(self):
        tester = app.test_client(self)
        payload = {
            'audioFileMetadata':
                '{"name": "mpoint", '
                '"duration": "90", '
                '"host": "remy", '
                '"participants":["morgan","kln","ijhg", "morgan"]}'
        }
        response = tester.put("http://127.0.0.1:5000/update/podcast/8",
                               data=payload)

        self.assertEqual(200, response.status_code)

    def test_update_audiobook(self):
        tester = app.test_client(self)
        payload = {
            'audioFileMetadata': '{"title": "new enture", '
                             '"duration": "10", '
                             '"author": "remy", '
                             '"narrator": "delan"}'
        }
        response = tester.put("http://127.0.0.1:5000/update/audiobook/8",
                               data=payload)

        self.assertEqual(200, response.status_code)

    def test_get_song(self):
        tester = app.test_client(self)
        response = tester.get('http://127.0.0.1:5000/get/song/7')
        self.assertEqual(200, response.status_code)

    def test_get_podcast(self):
        tester = app.test_client(self)
        response = tester.get('http://127.0.0.1:5000/get/podcast/7')
        self.assertEqual(200, response.status_code)

    def test_get_audiobook(self):
        tester = app.test_client(self)
        response = tester.get('http://127.0.0.1:5000/get/audiobook/7')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
