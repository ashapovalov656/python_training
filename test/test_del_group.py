from model.group import Group
import random


def test_del_some_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="default group", header="default header", footer="default footer"))
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = orm.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
