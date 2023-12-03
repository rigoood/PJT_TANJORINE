from rest_framework import serializers
from .models import Article, Comment, Category
from django.contrib.auth import get_user_model

User = get_user_model()



class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'email')
    
    user = UserSerializer(read_only=True)

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', 'pk')

    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user')


class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'email')
    
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ('pk', 'name',)

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Article
        # fields = ('pk', 'user', 'title', 'content', 'comments')
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)
    
    user = UserSerializer(read_only=True)
    # comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    # like_count = serializers.IntegerField()

    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ('pk', 'name',)
    
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Article
        # fields = ('id', 'title', 'user', 'comment_count', 'like_count', 'created_at',)
        fields = ('id', 'title', 'content', 'user', 'created_at', 'category')

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name',)