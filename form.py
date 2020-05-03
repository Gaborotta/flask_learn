from flask_wtf import FlaskForm
from wtforms import StringField, FieldList
from wtforms.validators import DataRequired, ValidationError

class Thema_form(FlaskForm):
    thema = StringField('テーマ')
    
    def validate_thema(self, thema):
        # バリデーション内容
        # 1.未入力は禁止
        if thema.data == '':
            raise ValidationError('テーマを入力してください。')
        # print(thema.data)

class Sub_Thema_form(FlaskForm):
    sub_themas = FieldList(StringField('テーマ'), min_entries=8, max_entries=8)
    
    def validate_sub_themas(self, sub_themas):
        for thm in sub_themas:
            if thm.data == '':
                raise ValidationError('テーマを入力してください。')
            
    