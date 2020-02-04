REST_FRAMEWORK = {
	'DEFLAULT_AUTHENTICATION_CLASSES': [
				#'rest_framwork.authentication.BasicAuthentication',
				'rest_framework.authentication.SessionAuthentication',
		],

	'DEFAULT_PERMISSION_CLASSES': [
				'rest_framework.permissions.IsAuthenticated',
	]
}