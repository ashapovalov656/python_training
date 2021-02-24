from model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="default group", header="default header", footer="default footer"))
    app.group.delete_first_group()

