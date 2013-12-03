                                            RepositoryError,
                                            TwoFactorAuthCodeRequiredError)
from reviewboard.scmtools.errors import (FileNotFoundError,
                                         InvalidChangeNumberError,
                                         SCMError)
    supports_two_factor_auth = True
                  two_factor_auth_code=None, local_site_name=None,
                  *args, **kwargs):
            headers = {}

            if two_factor_auth_code:
                headers['X-GitHub-OTP'] = two_factor_auth_code

                headers=headers,
                response_info = e.info()
                x_github_otp = response_info.get('X-GitHub-OTP', '')

                if x_github_otp.startswith('required;'):
                    raise TwoFactorAuthCodeRequiredError(
                        _('Enter your two-factor authentication code '
                          'and re-enter your password to link your account. '
                          'This code will be sent to you by GitHub.'))

            try:
                commit = self._api_get(url)[0]
            except Exception as e:
                raise SCMError(six.text_type(e))
        try:
            comparison = self._api_get(url)
        except Exception as e:
            raise SCMError(six.text_type(e))
            try:
                patch = file['patch']
            except KeyError:
                continue