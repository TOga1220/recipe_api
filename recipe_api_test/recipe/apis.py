from .models import Recipe                          # モデル呼出
from rest_framework.generics import ListCreateAPIView    # API
from .serializers import SampleSerializer                # APIで渡すデータをJSON,XML変換

class RecipeList(ListCreateAPIView):
    # 対象とするモデルのオブジェクトを定義
    queryset = Recipe.objects.all()

    # APIがデータを返すためのデータ変換ロジックを定義
    serializer_class = SampleSerializer

    # 認証
    permission_classes = []