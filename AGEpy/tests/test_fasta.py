import unittest

import unittest.mock as mock

from AGEpy import fasta


class TestFasta(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch('AGEpy.fasta.open', new_callable=mock.mock_open(), create=True)
    def test_writeFasta_empty_sequence(self, mock_open):
        # setting up the mocks, fakes and connections
        fake_sequence_name = "fake_name"
        fake_output_file = mock.sentinel.output_file
        fake_sequence = "fs"
        mock_file_handler = mock.MagicMock()
        mock_open.return_value = mock_file_handler

        # doing the call after everything has been stubbed out
        fasta.writeFasta(fake_sequence, fake_sequence_name, fake_output_file)

        # validating through assertions

        # verify open was called on the file
        mock_open.assert_called_once_with(fake_output_file, "w")
        # verify that `f` has been used to call `write` 2 times, once for the sequence name and once for the new line character
        mock_file_handler.write.assert_has_calls([
            mock.call(">"+str(fake_sequence_name)+"\n"),
            mock.call(fake_sequence+"\n"),
        ])
        # verify f.close was called
        mock_open.return_value.close.assert_called_once_with()