#  APIの出力をJSON,XMLデータに変換
from rest_framework import serializers
from .models import Recipe

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe                      # 呼び出すモデル
        fields = ["id", "title", "making_time", "serves", "ingredients", "cost"]  # API上に表示するモデルのデータ項目
 