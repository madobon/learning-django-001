from django import forms
from post.models import Post

# class PostForm(forms.Form):
class PostForm(forms.ModelForm):
    # keyword = forms.CharField(required=True) # キーワード
    # page = forms.IntegerField()

    # キーワードを必須項目として扱う
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        # self.fields['keyword'].required = True
        self.fields['keyword'].widget.attrs['class'] = 'form-control'
    def clean_keyword(self):
        keyword = self.cleaned_data['keyword']
        if keyword:
            # raise forms.ValidationError("Unko")
            pass

        return keyword

    class Meta:
        model = Post
        # 除外するフィールド
        exclude = ('ip','page')
