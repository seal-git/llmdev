from authenticator import Authenticator
import pytest

def test_register():
  authenticator = Authenticator()
  authenticator.register("testuser", "password123")
  assert authenticator.users["testuser"] == "password123"

def test_register_existing_user():
  authenticator = Authenticator()
  authenticator.register("testuser", "password123")
  with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
    authenticator.register("testuser", "newpassword")

def test_login():
  authenticator = Authenticator()
  authenticator.register("testuser", "password123")
  result = authenticator.login("testuser", "password123")
  assert result == "ログイン成功"

def test_login_invalid_user():
  authenticator = Authenticator()
  authenticator.register("testuser", "password123")
  with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"): 
    authenticator.login("testuser", "wrongpassword")
