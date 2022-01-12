# -*- coding: utf-8 -*-
from model.group import Group
import time

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="123", header="123", footer="123"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

