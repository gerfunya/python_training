def test_open_closepage(app):
    app.session.login(username="admin", password="secret")
    app.session.logout()