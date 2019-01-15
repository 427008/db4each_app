class MydbRouter:
    """
        A router to control all database operations on models in the
        auth application.
    """
    @property
    def name(self):
        return ['mydb']

    def db_for_read(self, model, **hints):
        """
        Attempts to read models go to app's db.
        """
        # if model._meta.app_label == self.name:
        #     return self.name
        return model._meta.app_label

    def db_for_write(self, model, **hints):
        """
        Attempts to write models go to app's db.
        """
        # if model._meta.app_label == self.name:
        #     return self.name
        return model._meta.app_label

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app is involved.
        """
        # if obj1._state.db == obj2._state.db:
        return True
        # return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the app's models only appears in the app's database.
        """
        if db == app_label and app_label in self.name:
            # print('---', model_name)
            return True
        if db not in self.name and app_label not in self.name:
            # print('+++', model_name)
            return True
        return False
