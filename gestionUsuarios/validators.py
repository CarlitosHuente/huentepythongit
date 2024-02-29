from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class NumericPasswordValidator:
    def validate(self, password, user=None):
        if not password.isdigit() or len(password) != 4:
            raise ValidationError(
                _("La contraseña debe ser de 4 dígitos numéricos."),
                code='password_no_numeric',
            )

    def get_help_text(self):
        return _("Tu contraseña debe contener exactamente 4 dígitos numéricos.")
