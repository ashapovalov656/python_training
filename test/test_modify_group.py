from model.group import Group


def test_modify_group_all_fields(app):
    app.group.modify_first_group(Group(name="new_name", header="new_header", footer="new_footer"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="GroupName"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="NewHeader"))
