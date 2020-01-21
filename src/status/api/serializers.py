from rest_framework import serializers

from status.models import Status 

'''

JSON: JavaScript Object Notation
Serializer -> JSON
Serializer -> Validation
'''

class StatusSerializer(serializers.ModelSerializer):

	class Meta:
		model = Status
		fields = [
			'user',
			'content',
			'image'
		]
