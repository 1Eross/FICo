import logging
logging.basicConfig(level=logging.INFO, filename="common/log/py_log.log",filemode="w+")
from common.db.database import dataBase

class Category:
    def __init__(self, category_id, icon, name):
        self._category_id = category_id
        self._icon = icon
        self._name = name

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, new_category_id):
        is_updated = dataBase.edit_category(self.id, name_column='category_id', data=new_category_id)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Category ID updated successfully to {new_category_id}")
            self._category_id = new_category_id
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update Category ID to {new_category_id}")
            return False

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, new_icon):
        is_updated = dataBase.edit_category(self.id, name_column='icon', data=new_icon)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Icon updated successfully to {new_icon}")
            self._icon = new_icon
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update Icon to {new_icon}")
            return False

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        is_updated = dataBase.edit_category(self.id, name_column='name', data=new_name)
        if is_updated:
            # Логирование успешного обновления
            logging.info(f"Name updated successfully to {new_name}")
            self._name = new_name
            return True
        else:
            # Логирование неудачного обновления
            logging.error(f"Failed to update Name to {new_name}")
            return False

    def add_new_category(self, new_category, name):
        is_added = dataBase.add_new_category(new_category, name)
        if is_added:
            logging.info(f"New category added successfully: {new_category}")
            return True
        else:
            logging.error(f"Failed to add new category: {new_category}")
            return False

    def delete(self):
        is_deleted = dataBase.delete_category(self.id)
        if is_deleted:
            logging.info(f"Category deleted successfully. Category ID: {self._category_id}")
            return True
        else:
            logging.error(f"Failed to delete Category. Category ID: {self._category_id}")
            return False