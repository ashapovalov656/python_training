from model.group import Group
from random import randrange

"""
def test_modify_group_all_fields(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_groups_list()
    app.group.modify_first_group(Group(name="new_name", header="new_header", footer="new_footer"))
    new_groups = app.group.get_groups_list()
    assert len(new_groups) == len(old_groups)
"""


def test_modify_group_name(app, orm, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = orm.get_group_list()
    index = randrange(len(old_groups))
    group = Group(id=old_groups[index].id, name="GroupName")
    app.group.modify_group_by_id(group, group.id)
    assert len(old_groups) == len(orm.get_group_list())
    new_groups = orm.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)

"""
def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_groups_list()
    app.group.modify_first_group(Group(header="NewHeader"))
    new_groups = app.group.get_groups_list()
    assert len(new_groups) == len(old_groups)
"""
