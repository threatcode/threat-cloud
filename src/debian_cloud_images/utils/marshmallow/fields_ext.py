from marshmallow import fields, ValidationError


class NestedRegistry(fields.Nested):
    @property
    def registry(self):
        return self.parent.context['registry']

    def _deserialize(self, value, attr, data):
        errors = {}
        valid_data = []
        for index, item in enumerate(value):
            try:
                valid_data.append(self.registry.load(item, unknown=self.unknown))
            except ValidationError as exc:
                valid_data.append(exc.valid_data)
                errors[index] = exc.messages
        if errors:
            raise ValidationError(errors, data=data, valid_data=valid_data)
        return valid_data

    def _serialize(self, value, attr, obj):
        errors = {}
        valid_data = []
        for index, item in enumerate(value):
            try:
                valid_data.append(self.registry.dump(item))
            except ValidationError as exc:
                valid_data.append(exc.valid_data)
                errors[index] = exc.messages
        if errors:
            raise ValidationError(errors, data=obj, valid_data=valid_data)
        return valid_data
