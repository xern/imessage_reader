#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from os import scandir
from imessage_reader.create_sqlite import CreateDatabase
from imessage_reader.fetch_data import MessageData


@pytest.fixture()
def create_directory(tmpdir):
    directory = tmpdir.mkdir('sub/')
    yield directory


def message_data_one_row():
    message_data_list = [MessageData(user_id='max.mustermann@icloud.com',
                                     text='Hello Max!',
                                     date='2021-04-11 17:02:34',
                                     service='iMessage')]
    return message_data_list


def test_create_sqlite(create_directory):
    db_file_path = create_directory + '/db-'
    test_database = CreateDatabase(message_data_one_row(), db_file_path)
    test_database.create_sqlite_db()

    file_name = ''
    dir_entries = scandir(create_directory)
    for entry in dir_entries:
        if entry.is_file():
            file_name = entry.name

    expected_file_name = 'db-' + 'iMessage-Data.sqlite'

    assert len(create_directory.listdir()) == 1
    assert file_name == expected_file_name
