from polymorphic.managers import PolymorphicManager


class ResourceBaseManager(PolymorphicManager):
    # TODO: revisar si es necesario ver si hay superusers

    def get_queryset(self):
        return super().get_queryset().non_polymorphic()

    def polymorphic_queryset(self):
        return super().get_queryset()
