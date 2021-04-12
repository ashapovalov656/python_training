Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <mid_name> and <lastname>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname | mid_name   | lastname  |
  | Имя_1     | Отчество_1 | Фамилия_1 |
  | Имя_2     | Отчество_2 | Фамилия_2 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact


Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a modified random contact with the new <firstname> and <lastname>
  When I modify the contact
  Then the new contact list is equal to the old list with the modified contact

    Examples:
  | firstname       | lastname          |
  | Modified Name   | Modified Lastname |