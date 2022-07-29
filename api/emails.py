import environ
import os
from email.policy import default
from django.contrib.auth.tokens import default_token_generator
from djoser import utils
from templated_mail.mail import BaseEmailMessage
from django.conf import settings

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.read_env(os.path.join(BASE_DIR, '.env'))


class EmailManager(BaseEmailMessage):
    def send(self, to, *args, **kwargs):
        self.render()
        self.to = to
        self.cc = kwargs.pop('cc', [])
        self.bcc = kwargs.pop('bcc', [])
        self.reply_to = kwargs.pop('reply_to', [])
        self.from_email = kwargs.pop(
            'from_email',
            'marese <' + settings.DEFAULT_FROM_EMAIL + '>'
        )
        super(BaseEmailMessage, self).send(*args, **kwargs)


class ActivationEmail(EmailManager):
    template_name = 'api/activation.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = ctx.get('user')
        ctx['name'] = user.email
        ctx['uid'] = utils.encode_uid(user.pk)
        ctx['token'] = default_token_generator.make_token(user)
        ctx['url'] = settings.DJOSER["ACTIVATION_URL"].format(**ctx)
        ctx['host'] = env('APP_HOST')
        return ctx


class ConfirmationEmail(EmailManager):
    template_name = 'api/confirmation.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = ctx.get('user')
        ctx['name'] = user.username
        return ctx


class PasswordResetEmail(EmailManager):
    template_name = 'api/password_reset.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = ctx.get('user')
        ctx['name'] = user.username
        ctx['uid'] = utils.encode_uid(user.pk)
        ctx['token'] = default_token_generator.make_token(user)
        ctx['url'] = settings.DJOSER["PASSWORD_RESET_CONFIRM_URL"].format(
            **ctx)
        ctx['host'] = env('APP_HOST')
        return ctx


class PasswordChangedConfirmationEmail(EmailManager):
    # auth/users/set_password/
    template_name = 'api/password_changed_confirmaion.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = ctx.get('user')
        ctx['name'] = user.username
        return ctx


class UsernameResetEmail(EmailManager):
    template_name = 'api/username_reset.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = ctx.get('user')
        ctx['name'] = user.username
        ctx['uid'] = utils.encode_uid(user.pk)
        ctx['token'] = default_token_generator.make_token(user)
        ctx['url'] = settings.DJOSER["USERNAME_RESET_CONFIRM_URL"].format(
            **ctx)
        ctx['host'] = env('APP_HOST')
        return ctx


class UsernameChangedConfirmationEmail(EmailManager):
    template_name = 'api/username_changed_confirmaion.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = ctx.get('user')
        ctx['name'] = user.username
        return ctx
