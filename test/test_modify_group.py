from model.group import Group

"""
def test_modify_group_all_fields(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_groups_list()
    app.group.modify_first_group(Group(name="new_name", header="new_header", footer="new_footer"))
    new_groups = app.group.get_groups_list()
    assert len(new_groups) == len(old_groups)
"""


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_groups_list()
    group = Group(name="GroupName")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""
def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_groups_list()
    app.group.modify_first_group(Group(header="NewHeader"))
    new_groups = app.group.get_groups_list()
    assert len(new_groups) == len(old_groups)
"""
