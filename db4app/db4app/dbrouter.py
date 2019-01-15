class PrimaryRouter:

    @property
    def exceptions(self):
        return ['mydb']

    @property
    def name(self):
        return 'default'

    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        if model._meta.app_label == self.name:
            return self.name
        return None

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        if model._meta.app_label == self.name:
            return self.name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        if obj1._meta.app_label == self.name and obj2._meta.app_label == self.name:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All default models end up in this pool.
        """
        if db in self.exceptions or app_label in self.exceptions:
            return False

        print('+++', db, model_name, hints)
        return True
