from iconApi import models


class AuditTrailMixin(models.BaseTimestampedModel,
                   models.BaseUserMetadataModel):

    """
    Mixin that provides audit trail fields to any model via:
        - BaseTimestampedModel
        - BaseUserMetadataModel
        - BaseTimestampedModel
    """
    class Meta:
        abstract = True


class GuidFieldMixin(models.BaseGuidModel):
    """
    Mixin for adding a UUID type 4 field to a model named 'guid'
    """
    class Meta:
        abstract = True


class ApiMappableMixin(models.BaseApiMappableModel):
    """
    Mixin that allows you to store an object_id field that maps to
    the equivalent object in an external API
    """
    class Meta:
        abstract = True
